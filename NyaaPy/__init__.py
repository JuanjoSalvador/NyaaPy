import requests
import json
from bs4 import BeautifulSoup

# Info about the module
__version__   = '0.4.1'
__author__    = 'Juanjo Salvador'
__email__     = 'juanjosalvador@netc.eu'
__url__       = 'http://juanjosalvador.me'
__copyright__ = '2017 Juanjo Salvador'
__license__   = 'MIT license'

class Nyaa():
    '''
     Return a list of dicts with the results of the query.
    '''
    def search(keyword, category, subcategory, filters, page):
        if page:
            r = requests.get("http://nyaa.si/?f={}&c={}_{}&q={}&p={}".format(filters, category, subcategory, keyword, page))
        else:
            r = requests.get("http://nyaa.si/?f={}&c={}_{}&q={}".format(filters, category, subcategory, keyword))

        soup = BeautifulSoup(r.text, 'html.parser')
        rows = soup.select('table tr')

        torrents = []

        if rows:
            for row in rows:
                block = []

                for td in row.find_all('td'):
                    if td.find_all('a'):
                        for link in td.find_all('a'):
                            if link.get('href')[-9:] != '#comments':
                                block.append(link.get('href'))
                                if link.text.rstrip():
                                    block.append(link.text)

                    if td.text.rstrip():
                        block.append(td.text.rstrip())

                try:
                    c = block[0].replace('/?c=', '')
                    cats = c.split('_')

                    torrent = {
                        'category': cats[0],
                        'subcategory': cats[1],
                        'url': "http://nyaa.si{}".format(block[1]),
                        'name': block[2],
                        'download_url': "http://nyaa.si{}".format(block[4]),
                        'magnet': block[5],
                        'size': block[6],
                        'date': block[7],
                        'seeders': block[8],
                        'leechers': block[9],
                        'completed_downloads': block[10],
                    }
                
                    torrents.append(torrent)
                except IndexError as ie:
                    pass

        return torrents
    '''
     Returns an array of dicts with the n last updates of Nyaa.si
    '''
    def news(n):
        r = requests.get("http://nyaa.si/")
        soup = BeautifulSoup(r.text, 'html.parser')
        rows = soup.select('table tr')

        torrents = []

        for row in rows:
            block = []

            for td in row.find_all('td'):
                if td.find_all('a'):
                    for link in td.find_all('a'):
                        if link.get('href')[-9:] != '#comments':
                            block.append(link.get('href'))
                            if link.text.rstrip():
                                block.append(link.text)

                if td.text.rstrip():
                    block.append(td.text.rstrip())

            try:
                c = block[0].replace('/?c=', '')
                cats = c.split('_')

                torrent = {
                    'category': cats[0],
                    'subcategory': cats[1],
                    'url': "http://nyaa.si{}".format(block[1]),
                    'name': block[2],
                    'download_url': "http://nyaa.si{}".format(block[4]),
                    'magnet': block[5],
                    'size': block[6],
                    'date': block[7],
                    'seeders': block[8],
                    'leechers': block[9],
                    'completed_downloads': block[10],
                }
            
                torrents.append(torrent)
            except IndexError:
                pass

        return torrents[:n]

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
