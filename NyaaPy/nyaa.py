import requests
import urllib.parse
from bs4 import BeautifulSoup
from NyaaPy import utils

class Nyaa:

    def __init__(self):
        self.URI = "http://nyaa.si"

    def search(self, keyword, **kwargs):
        user = kwargs.get('user', None)
        category = kwargs.get('category', 0)
        subcategory = kwargs.get('subcategory', 0)
        filters = kwargs.get('filters', 0)
        page = kwargs.get('page', 0)

        if user:
            user_uri = "user/{}".format(user)
        else:
            user_uri = ""

        if page > 0:
            r = requests.get("{}/{}?f={}&c={}_{}&q={}&p={}".format(
                self.URI, user_uri, filters, category, subcategory, keyword,
                page))
        else:
            r = requests.get("{}/{}?f={}&c={}_{}&q={}".format(
                self.URI, user_uri, filters, category, subcategory, keyword))

        soup = BeautifulSoup(r.text, 'html.parser')
        rows = soup.select('table tr')

        return utils.parse_nyaa(rows, limit=None)

    def get(self, id):
        r = requests.get("{}/view/{}".format(self.URI, id))
        soup = BeautifulSoup(r.text, 'html.parser')
        content = soup.findAll("div", {"class": "panel", "id": None})

        return utils.parse_single(content)

    def get_user(self, username):
        r = requests.get("{}/user/{}".format(self.URI, username))
        soup = BeautifulSoup(r.text, 'html.parser')

        return utils.parse_nyaa(soup.select('table tr'), limit=None)

    def news(self, number_of_results):
        r = requests.get(self.URI)
        soup = BeautifulSoup(r.text, 'html.parser')
        rows = soup.select('table tr')

        return utils.parse_nyaa(rows, limit=number_of_results + 1)
