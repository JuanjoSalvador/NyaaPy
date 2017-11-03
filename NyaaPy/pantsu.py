import requests
from NyaaPy.utils import Utils as utils

class Pantsu:

# Torrents - GET
    def search(keyword, **kwargs):
        print(utils.query_builder(keyword, kwargs))
        request = requests.get("{}/search{}".format("https://nyaa.pantsu.cat/api", utils.query_builder(keyword, kwargs)))
        
        return request.json()

    def view(item_id):
        request = requests.get("/view/{}".format("https://nyaa.pantsu.cat/api", item_id))

        return request.json()

    # Torrents - POST

    # Users

    def login(username, password):
        login = requests.post("{}/login/".format(BASE_URL), data={'username': username, 'password': password})

        return login.json()

    def profile(user_id):
        profile = requests.post("{}/profile/".format(BASE_URL), data={'id': user_id})

        return profile.json()