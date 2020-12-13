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


class SukebeiPantsu:
    BASE_URL = "https://sukebei.pantsu.cat/api"

    # Torrents - GET
    def search(self, keyword, **kwargs):
        request = requests.get("{}/search{}".format(
            SukebeiPantsu.BASE_URL, utils.query_builder(keyword, kwargs)))

        return request.json()

    def view(self, item_id):
        request = requests.get("{}/view/{}".format(
            SukebeiPantsu.BASE_URL, item_id))

        return request.json()

    # Torrents - POST

    def upload(self):
        return "Work in progress!"

    def update(self):
        return "Work in progress!"

    # Users

    def login(self, username, password):
        login = requests.post("{}/login/".format(
            SukebeiPantsu.BASE_URL), data={'username': username,
                                           'password': password})

        return login.json()

    def profile(self, user_id):
        profile = requests.post("{}/profile/".format(
            SukebeiPantsu.BASE_URL), data={'id': user_id})

        return profile.json()
