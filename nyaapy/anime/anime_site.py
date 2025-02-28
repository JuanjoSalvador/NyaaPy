import aiohttp
import requests

from nyaapy.anime.base import BaseTorrentSite
from nyaapy.parser import parse_nyaa, parse_nyaa_rss, parse_single


class AnimeTorrentSite(BaseTorrentSite):

    @classmethod
    def last_uploads(cls, number_of_results: int):
        r = requests.get(cls.URL)

        # If anything up with nyaa servers let the user know.
        r.raise_for_status()

        json_data = parse_nyaa(
            request_text=r.text, limit=number_of_results, site=cls.SITE
        )

        return cls._json_to_class(json_data)

    @classmethod
    def search(cls, keyword: str, **kwargs):
        base_url = cls.URL
        user, search_uri = cls._parse_request(base_url, keyword, kwargs)

        http_response = requests.get(search_uri)
        http_response.raise_for_status()

        if user:
            json_data = parse_nyaa(
                request_text=http_response.content, limit=None, site=cls.SITE
            )
        else:
            json_data = parse_nyaa_rss(
                request_text=http_response.content, limit=None, site=cls.SITE
            )

        # Convert JSON data to a class object
        return cls._json_to_class(json_data)

    @classmethod
    def get(cls, view_id: int):
        r = requests.get(f"{cls.URL}/view/{view_id}")
        r.raise_for_status()

        json_data = parse_single(request_text=r.content, site=cls.SITE)

        return cls._json_to_class(json_data)

    @classmethod
    def get_from_user(cls, username):
        r = requests.get(f"{cls.URL}/user/{username}")
        r.raise_for_status()

        json_data = parse_nyaa(request_text=r.content, limit=None, site=cls.SITE)
        return cls._json_to_class(json_data)


class AnimeTorrentSiteAsync(AnimeTorrentSite):

    @classmethod
    async def last_uploads(cls, number_of_results: int):
        async with aiohttp.ClientSession() as session:
            async with session.get(cls.URL) as r:

                # If anything up with nyaa servers let the user know.
                r.raise_for_status()

                json_data = parse_nyaa(
                    request_text=(await r.text()),
                    limit=number_of_results,
                    site=cls.SITE,
                )

                return cls._json_to_class(json_data)

    @classmethod
    async def search(cls, keyword: str, **kwargs):
        user, search_uri = cls._parse_request(keyword, kwargs)

        async with aiohttp.ClientSession() as session:
            async with session.get(search_uri) as http_response:

                http_response.raise_for_status()

                if user:
                    json_data = parse_nyaa(
                        request_text=await http_response.content.read(),
                        limit=None,
                        site=cls.SITE,
                    )
                else:
                    json_data = parse_nyaa_rss(
                        request_text=await http_response.content.read(),
                        limit=None,
                        site=cls.SITE,
                    )

                # Convert JSON data to a class object
                return cls._json_to_class(json_data)

    @classmethod
    async def get(cls, view_id: int):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{cls.URL}/view/{view_id}") as r:
                r.raise_for_status()

                json_data = parse_single(request_text=r.content, site=cls.SITE)

                return cls._json_to_class(json_data)

    @classmethod
    async def get_from_user(cls, username):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{cls.URL}/user/{username}") as r:
                r.raise_for_status()

                json_data = parse_nyaa(
                    request_text=r.content, limit=None, site=cls.SITE
                )
                return cls._json_to_class(json_data)
