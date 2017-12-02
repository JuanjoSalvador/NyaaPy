import requests
from bs4 import BeautifulSoup
from NyaaPy.utils import Utils as utils

class SukebeiNyaa:
    def search(keyword, **kwargs):
        category = kwargs.get('category', 0)
        subcategory = kwargs.get('subcategory', 0)
        filters = kwargs.get('filters', 0)
        page = kwargs.get('page', 0)

        if page > 0:
            r = requests.get("{}/?f={}&c={}_{}&q={}&p={}".format("http://sukebei.nyaa.si", filters, category, subcategory, keyword, page))
        else:
            r = requests.get("{}/?f={}&c={}_{}&q={}".format("http://sukebei.nyaa.si", filters, category, subcategory, keyword))

        soup = BeautifulSoup(r.text, 'html.parser')
        rows = soup.select('table tr')

        return utils.parse_nyaa(rows, limit=None)

    def get(id):
        r = requests.get("http://sukebei.nyaa.si/view/{}".format(id))
        soup = BeautifulSoup(r.text, 'html.parser')
        content = soup.findAll("div", { "class": "panel", "id": None})
        
        return utils.parse_single(content)

    def get_user(username):
        r = requests.get("http://sukebei.nyaa.si/user/{}".format(username))
        soup = BeautifulSoup(r.text, 'html.parser')

        return utils.parse_nyaa(soup.select('table tr'), limit=None)

    def news(number_of_results):
        r = requests.get("http://sukebei.nyaa.si/")
        soup = BeautifulSoup(r.text, 'html.parser')
        rows = soup.select('table tr')

        return utils.parse_sukebei(rows, limit=number_of_results + 1)

class SukebeiPantsu:
    BASE_URL = "https://sukebei.pantsu.cat/api"

    # Torrents - GET
    def search(keyword, **kwargs):
        request = requests.get("{}/search{}".format(SukebeiPantsu.BASE_URL, utils.query_builder(keyword, kwargs)))
        
        return request.json()

    def view(item_id):
        request = requests.get("{}/view/{}".format(SukebeiPantsu.BASE_URL, item_id))

        return request.json()

    # Torrents - POST

    def upload():
        return "Work in progress!"

    def update():
        return "Work in progress!"

    # Users

    def login(username, password):
        login = requests.post("{}/login/".format(SukebeiPantsu.BASE_URL), data={'username': username, 'password': password})

        return login.json()

    def profile(user_id):
        profile = requests.post("{}/profile/".format(SukebeiPantsu.BASE_URL), data={'id': user_id})

        return profile.json()