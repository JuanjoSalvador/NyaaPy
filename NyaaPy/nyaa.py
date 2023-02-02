import requests
from utils import parse_nyaa, parse_nyaa_rss, parse_single
from torrent import json_to_class
from sites import TorrentSite

class Nyaa:

    def __init__(self):
        self.SITE = TorrentSite.NYAASI
        self.URL = "https://nyaa.si"

    def last_uploads(self, number_of_results):
        r = requests.get(self.URL)

        # If anything up with nyaa servers let the user know.
        r.raise_for_status()

        json_data = parse_nyaa(
            request_text=r.text,
            limit=number_of_results + 1,
            site=self.SITE
        )
        return json_to_class(json_data)

    def search(self, keyword, **kwargs):
        url = self.URL

        user = kwargs.get('user', None)
        category = kwargs.get('category', 0)
        subcategory = kwargs.get('subcategory', 0)
        filters = kwargs.get('filters', 0)
        page = kwargs.get('page', 0)
        sorting = kwargs.get('sort', 'id') # Sorting by id = sorting by date, this is the default.
        order = kwargs.get('order', 'desc')

        if user:
            user_uri = f"user/{user}"
        else:
            user_uri = ""

        if page > 0:
            r = requests.get(
                f"{url}/{user_uri}?f={filters}&c={category}_{subcategory}&q={keyword}&p={page}&s={sorting}&o={order}"
            )
        else:
            r = requests.get(
                f"{url}/{user_uri}?f={filters}&c={category}_{subcategory}&q={keyword}&s={sorting}&o={order}"
            )

        if not user:
            uri += "&page=rss"

        http_response = requests.get(uri)

        http_response.raise_for_status()

        if user:
            json_data = parse_nyaa(
                request_text=http_response.text,
                limit=None,
                site=self.SITE
            )
        else:
            json_data = parse_nyaa_rss(
                request_text=http_response.text,
                limit=None,
                site=self.SITE
            )

        return json_to_class(json_data)

    def get(self, view_id):
        r = requests.get(f'{self.URL}/view/{view_id}')
        r.raise_for_status()

        json_data = parse_single(request_text=r.text, site=self.SITE)

        return json_to_class(json_data)

    def get_user(self, username):
        r = requests.get(f'{self.URL}/user/{username}')
        r.raise_for_status()

        json_data = parse_nyaa(
            request_text=r.text,
            limit=None,
            site=self.SITE
        )
        return json_to_class(json_data)
