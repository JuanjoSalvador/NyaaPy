import requests
from NyaaPy.utils import Utils

utils = Utils()


class Pantsu:

    def __init__(self):
        self.BASE_URL = "https://nyaa.pantsu.cat/api"

    # Torrents - GET
    def search(self, keyword, **kwargs):
        request = requests.get("{}/search{}".format(
            self.BASE_URL, utils.query_builder(keyword, kwargs)))
        return request.json()

    def view(self, item_id):
        request = requests.get("{}/view/{}".format(self.BASE_URL, item_id))

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
