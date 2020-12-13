import requests
from NyaaPy import utils


class Pantsu:

    def __init__(self):
        self.BASE_URL = "https://nyaa.pantsu.cat/api"
        self.SITE = utils.TorrentSite.NYAANET

    def last_uploads(self, number_of_results):
        r = requests.get(self.SITE.value)
        r.raise_for_status()
        with open("test.html", "w") as f:
            f.write(r.text)

        return utils.parse_nyaa(
            request_text=r.text,
            limit=number_of_results + 1,
            site=self.SITE
        )

    # Torrents - GET
    def search(self, keyword, **kwargs):
        request = requests.get("{}/search{}".format(
            self.BASE_URL, utils.query_builder(keyword, kwargs)))
        return request.json()

    def view(self, item_id):
        request = requests.get("{}/view/{}".format(self.BASE_URL, item_id))

        request.raise_for_status()

        return request.json()

    # Torrents - POST
    def upload(self):
        return "Work in progress!"

    def update(self):
        return "Work in progress!"

    # Users
    def login(self, username, password):
        login = requests.post("{}/login/".format(
            self.BASE_URL), data={'username': username, 'password': password})

        return login.json()

    def profile(self, user_id):
        profile = requests.post("{}/profile/".format(
            self.BASE_URL), data={'id': user_id})

        return profile.json()
