import requests
from NyaaPy.utils import Utils as utils

class Pantsu:

    BASE_URL = "https://nyaa.pantsu.cat/api"

    # Torrents - GET
    def search(keyword, **kwargs):        
        request = requests.get("{}/search{}".format(Pantsu.BASE_URL, utils.query_builder(keyword, kwargs)))
        return request.json()

    def view(item_id):
        request = requests.get("{}/view/{}".format(Pantsu.BASE_URL, item_id))

        return request.json()

    # Torrents - POST

    def upload():
        return "Work in progress!"

    def update():
        return "Work in progress!"

    # Users

    def login(username, password):
        login = requests.post("{}/login/".format(Pantsu.BASE_URL), data={'username': username, 'password': password})

        return login.json()

    def profile(user_id):
        profile = requests.post("{}/profile/".format(Pantsu.BASE_URL), data={'id': user_id})

        return profile.json()