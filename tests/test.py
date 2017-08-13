import json
from NyaaPy import Nyaa, NyaaPantsu

# Nyaa.si results
def nyaa_search():
    nyaa_query = Nyaa.search('koe no katachi 1080')

    if len(nyaa_query) > 0:
        for result in nyaa_query:
            print(result['title'])
    else:
        print('Nothing here!')

def nyaa_news():
    news = Nyaa.news(5)

    for result in news:
        print(result['title'])

# Nyaa.pantsu.cat results
def pantsu_search():
    pantsu_query = NyaaPantsu.search('new game!!')
    if len(pantsu_query) > 0:
        for result in pantsu_query:
            print(result['title'])
    else:
        print('Nothing here!')


def pantsu_news():
    news = NyaaPantsu.news(5)

    for result in news:
        print(result['title'])

# Uncomment whatever you want to test

#nyaa_search()
#pantsu_search()
#nyaa_news()
pantsu_news()
