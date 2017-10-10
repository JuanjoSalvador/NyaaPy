import requests
import json
from bs4 import BeautifulSoup

# Info about the module
__version__   = '0.4'
__author__    = 'Juanjo Salvador'
__email__     = 'juanjosalvador@netc.eu'
__url__       = 'http://juanjosalvador.me'
__copyright__ = '2017 Juanjo Salvador'
__license__   = 'MIT license'

class Nyaa():
    def search(keyword, category, subcategory, filters):
        r = requests.get("http://nyaa.si/?f={}&c={}_{}&q={}".format(filters, category, subcategory, keyword))
        soup = BeautifulSoup(r.text, 'html.parser')
        rows = soup.select('table tr')

        torrents = []

        for row in rows:
            td = row.find_all('td')
            torrent = []

            for i in td:
                if i.find('a'):
                    torrent.append(i.find('a').get('href'))
                    text = i.text.rstrip()
                    if len(text) > 0:
                        torrent.append(text)
                else:
                    text = i.text.rstrip()
                    if len(text) > 0:
                        torrent.append(text)

            torrents.append(torrent)
        
        print(torrents)

        return torrents

    '''
     Returns an array of OrderedDict with the n last updates of Nyaa.si
    '''
    def news(n):
        nyaa_baseurl = "https://nyaa.si/?page=rss"

        request  = requests.get(nyaa_baseurl)
        response = xmltodict.parse(request.text)

        results = response['rss']['channel']['item']

        return results[:n]

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
