import requests
from bs4 import BeautifulSoup
from NyaaPy.utils import Utils as utils


class NyaaPantsu():
    '''
     Make a query to nyaa.pantsu.cat using keyword as keyword.
     Returns an array of OrderedDict with every result of the query.
     Returns an empty array if no results.
    '''
    def search(keyword):
        nyaapantsu_baseurl = "https://nyaa.pantsu.cat/feed?c=_&s=0&max=99999&userID=0&q="

        request  = requests.get(nyaa_baseurl + keyword)
        response = xmltodict.parse(request.text)

        results = []

        try:
            if type(response['rss']['channel']['item']) is collections.OrderedDict:
                results.append(response['rss']['channel']['item'])
            else:
                results = response['rss']['channel']['item']

        except KeyError as ex:
            results = []

        return results

    '''
     Returns an array of OrderedDict with the n last updates of nyaa.pantsu.cat
    '''
    def news(n):
        nyaa_baseurl = "https://nyaa.pantsu.cat/feed"

        request  = requests.get(nyaa_baseurl)
        response = xmltodict.parse(request.text)

        results = response['rss']['channel']['item']

        return results[:n]