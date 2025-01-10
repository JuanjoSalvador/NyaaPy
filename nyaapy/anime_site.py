import aiohttp
import requests

from nyaapy import torrent
from nyaapy.parser import parse_nyaa, parse_nyaa_rss, parse_single


class AnimeTorrentSite:
    SITE = torrent.TorrentSite.NYAASI
    URL = "https://nyaa.si"

    @classmethod
    def last_uploads(cls, number_of_results: int):
        r = requests.get(cls.URL)

        # If anything up with nyaa servers let the user know.
        r.raise_for_status()

        json_data = parse_nyaa(
            request_text=r.text, limit=number_of_results, site=cls.SITE
        )

        return torrent.json_to_class(json_data)

    @classmethod
    def parse_request(cls, keyword, kwargs):
        base_url = cls.URL

        user = kwargs.get("user", None)
        category = kwargs.get("category", 0)
        subcategory = kwargs.get("subcategory", 0)
        filters = kwargs.get("filters", 0)
        page = kwargs.get("page", 0)
        sorting = kwargs.get(
            "sort", "id"
        )  # Sorting by id = sorting by date, this is the default.
        order = kwargs.get("order", "desc")

        user_uri = f"user/{user}" if user else ""

        if page > 0:
            search_uri = "{}/{}?f={}&c={}_{}&q={}&p={}&s={}&o={}".format(
                base_url,
                user_uri,
                filters,
                category,
                subcategory,
                keyword,
                page,
                sorting,
                order,
            )
        else:
            search_uri = "{}/{}?f={}&c={}_{}&q={}&s={}&o={}".format(
                base_url,
                user_uri,
                filters,
                category,
                subcategory,
                keyword,
                sorting,
                order,
            )

        if not user:
            search_uri += "&page=rss"
        return user, search_uri

    @classmethod
    def search(cls, keyword: str, **kwargs):
        user, search_uri = cls.parse_request(keyword, kwargs)

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
        return torrent.json_to_class(json_data)

    @classmethod
    def get(cls, view_id: int):
        r = requests.get(f"{cls.URL}/view/{view_id}")
        r.raise_for_status()

        json_data = parse_single(request_text=r.content, site=cls.SITE)

        return torrent.json_to_class(json_data)

    @classmethod
    def get_from_user(cls, username):
        r = requests.get(f"{cls.URL}/user/{username}")
        r.raise_for_status()

        json_data = parse_nyaa(request_text=r.content, limit=None, site=cls.SITE)
        return torrent.json_to_class(json_data)


class AnimeTorrentSiteAsync(AnimeTorrentSite):
    SITE = torrent.TorrentSite.NYAASI
    URL = "https://nyaa.si"

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

                return torrent.json_to_class(json_data)

    @classmethod
    async def search(cls, keyword: str, **kwargs):
        user, search_uri = cls.parse_request(keyword, kwargs)

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
                return torrent.json_to_class(json_data)

    @classmethod
    async def get(cls, view_id: int):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{cls.URL}/view/{view_id}") as r:
                r.raise_for_status()

                json_data = parse_single(request_text=r.content, site=cls.SITE)

                return torrent.json_to_class(json_data)

    @classmethod
    async def get_from_user(cls, username):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{cls.URL}/user/{username}") as r:
                r.raise_for_status()

                json_data = parse_nyaa(
                    request_text=r.content, limit=None, site=cls.SITE
                )
                return torrent.json_to_class(json_data)
