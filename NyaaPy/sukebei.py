import requests

from sites import TorrentSite
from utils import parse_nyaa, parse_single

class SukebeiNyaa:

    def __init__(self):
        self.SITE = TorrentSite.SUKEBEINYAASI

    def search(self, keyword, **kwargs):
        uri = self.SITE.value
        category = kwargs.get('category', 0)
        subcategory = kwargs.get('subcategory', 0)
        filters = kwargs.get('filters', 0)
        page = kwargs.get('page', 0)

        if page > 0:
            r = requests.get(f"{uri}/?f={filters}&c={category}_{subcategory}&q={keyword}&p={page}")
        else:
            r = requests.get(f"{uri}/?f={filters}&c={category}_{subcategory}&q={keyword}")

        r.raise_for_status()
        return parse_nyaa(r.text, limit=None, site=self.SITE)

    def get(self, id):
        r = requests.get(f"{self.SITE.value}/view/{id}")
        r.raise_for_status()

        return parse_single(r.text, self.SITE)

    def get_user(self, username):
        r = requests.get(f"{self.SITE.value}/user/{username}")
        r.raise_for_status()

        return parse_nyaa(r.text, limit=None, site=self.SITE)

    def last_uploads(self, number_of_results):
        r = requests.get(self.SITE.value)
        r.raise_for_status()

        return parse_nyaa(
            r.text,
            limit=number_of_results + 1,
            site=self.SITE
        )
