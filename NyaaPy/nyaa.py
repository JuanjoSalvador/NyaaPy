import requests
import xmltodict


class Nyaa():
    def search(keyword):
        nyaa_baseurl = "https://nyaa.si/?page=rss&c=1_0&f=0&q="

        request  = requests.get(nyaa_baseurl + keyword)
        response = xmltodict.parse(request.text)

        try:
            results = response['rss']['channel']['item']
        except KeyError as ex:
            results = {}

        return results

class NyaaPantsu():
    def search(keyword):
        nyaapantsu_baseurl = "https://nyaa.pantsu.cat/feed?c=_&s=0&max=99999&userID=0&q="

        request  = requests.get(nyaapantsu_baseurl + keyword)
        response = xmltodict.parse(request.text)

        try:
            results = response['rss']['channel']['item']
        except KeyError as ex:
            results = {}

        return results
