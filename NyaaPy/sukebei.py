import requests
from NyaaPy import utils


class SukebeiNyaa:

    def __init__(self):
        self.SITE = utils.TorrentSite.SUKEBEINYAASI

    def search(self, keyword, **kwargs):
        uri = self.SITE.value
        category = kwargs.get('category', 0)
        subcategory = kwargs.get('subcategory', 0)
        filters = kwargs.get('filters', 0)
        page = kwargs.get('page', 0)

        if page > 0:
            r = requests.get("{}/?f={}&c={}_{}&q={}&p={}".format(
                uri, filters, category, subcategory,
                keyword, page))
        else:
            r = requests.get("{}/?f={}&c={}_{}&q={}".format(
                uri, filters, category, subcategory,
                keyword))

        r.raise_for_status()
        return utils.parse_nyaa(r.text, limit=None, site=self.SITE)

    def get(self, id):
        r = requests.get("{}/view/{}".format(self.SITE.value, id))
        r.raise_for_status()

        return utils.parse_single(r.text, self.SITE)

    def get_user(self, username):
        r = requests.get("{}/user/{}".format(self.SITE.value, username))
        r.raise_for_status()

        return utils.parse_nyaa(r.text, limit=None, site=self.SITE)

    def last_uploads(self, number_of_results):
        r = requests.get(self.SITE.value)
        r.raise_for_status()

        return utils.parse_nyaa(
            r.text,
            limit=number_of_results + 1,
            site=self.SITE
        )
