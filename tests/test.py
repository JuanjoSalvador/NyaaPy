import json, requests
from NyaaPy import Nyaa, NyaaPantsu

# Nyaa.si results
def nyaa_search():
    nyaa_query = Nyaa.search('koe no katachi 1080', 1, 0, 0, 2)

    for nyaa in nyaa_query:
        print(nyaa['date'])

def nyaa_news():
    news = Nyaa.news(5)

    for result in news:
        print(result['name'])

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

nyaa_search()
#pantsu_search()
nyaa_news()
#pantsu_news()

''' r = requests.get("http://nyaa.si/")
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

        torrents.append(torrent) '''