import requests
from bs4 import BeautifulSoup
from NyaaPy.utils import Utils as utils

class Nyaa():
    '''
     Return a list of dicts with the results of the query.
    '''
    def search(keyword, category, subcategory, filters, page):
        if page > 0:
            r = requests.get("http://nyaa.si/?f={}&c={}_{}&q={}&p={}".format(filters, category, subcategory, keyword, page))
        else:
            r = requests.get("http://nyaa.si/?f={}&c={}_{}&q={}".format(filters, category, subcategory, keyword))

        soup = BeautifulSoup(r.text, 'html.parser')
        rows = soup.select('table tr')

        results = {}

        if rows:
            results = utils.parse_nyaa(rows, limit=None)

        return results
    
    '''
     Returns an array of dicts with the n last updates of Nyaa.si
    '''
    def news(number_of_results):
        r = requests.get("http://nyaa.si/")
        soup = BeautifulSoup(r.text, 'html.parser')
        rows = soup.select('table tr')

        return utils.parse_nyaa(rows, limit=number_of_results)