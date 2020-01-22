import requests
import urllib.parse
from NyaaPy import utils


class Nyaa:

    def __init__(self):
        self.URI = "http://nyaa.si"

    def last_uploads(self, number_of_results):
        r = requests.get(self.URI)

        # If anything up with nyaa servers let the user know.
        r.raise_for_status()

        return utils.parse_nyaa(
            request_text=r.text,
            limit=number_of_results + 1
        )

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

        r.raise_for_status()

        return utils.parse_nyaa(request_text=r.text, limit=None)

    def get(self, id):
        r = requests.get("{}/view/{}".format(self.URI, id))
        r.raise_for_status()

        return utils.parse_single(request_text=r.text)

    def get_user(self, username):
        r = requests.get("{}/user/{}".format(self.URI, username))
        r.raise_for_status()

        return utils.parse_nyaa(request_text=r.text, limit=None)
