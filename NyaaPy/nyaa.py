import requests
from NyaaPy import utils


class Nyaa:

    def __init__(self):
<<<<<<< HEAD
        self.SITE = utils.TorrentSite.NYAASI
=======
        self.URI = "https://nyaa.si"
>>>>>>> 5c93e516ba364d448335ebdc6989f8e1724c88c7

    def last_uploads(self, number_of_results):
        r = requests.get(self.SITE.value)

        # If anything up with nyaa servers let the user know.
        r.raise_for_status()

        return utils.parse_nyaa(
            request_text=r.text,
            limit=number_of_results + 1,
            site=self.SITE
        )

    def search(self, keyword, **kwargs):
        url = self.SITE.value

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
                url, user_uri, filters, category, subcategory, keyword,
                page))
        else:
            r = requests.get("{}/{}?f={}&c={}_{}&q={}".format(
                url, user_uri, filters, category, subcategory, keyword))

        r.raise_for_status()

        return utils.parse_nyaa(
            request_text=r.text,
            limit=None,
            site=self.SITE
        )

    def get(self, id):
        r = requests.get("{}/view/{}".format(self.SITE.value, id))
        r.raise_for_status()

        return utils.parse_single(request_text=r.text, site=self.SITE)

    def get_user(self, username):
        r = requests.get("{}/user/{}".format(self.SITE.value, username))
        r.raise_for_status()

        return utils.parse_nyaa(
            request_text=r.text,
            limit=None,
            site=self.SITE
        )
