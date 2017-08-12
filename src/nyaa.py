import requests
import xmltodict


class Nyaa:
    '''
     Makes a search query to nyaa.si with the given keyword that returns a
     RSS file converted into a dictionary that we can use.
    '''

    def search(keyword):
        nyaa_baseurl = "https://nyaa.si/?page=rss&c=1_0&f=0&q="

        request  = requests.get(nyaa_baseurl + keyword)
        response = xmltodict.parse(request.text)
        results = response['rss']['channel']['item']

        return results

class NyaaPantsu:
    '''
     Makes a search query to nyaa.pantsu.cat with the given keyword that returns a
     RSS file converted into a dictionary that we can use.
    '''

    def search(keyword):
        nyaa_baseurl = "https://nyaa.pantsu.cat/feed?c=_&s=0&max=99999&userID=0&q="

        request  = requests.get(nyaa_baseurl + keyword)
        response = xmltodict.parse(request.text)
        results = response['rss']['channel']['item']

        return results
