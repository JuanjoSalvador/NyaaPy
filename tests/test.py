from NyaaPy import Nyaa, NyaaPantsu

# Nyaa.si results
def nyaa_search():
    nyaa_query = Nyaa.search(keyword='koe no katachi 1080', category=1, subcategory=0, filters=0, page=0)

    for nyaa in nyaa_query:
        print(nyaa)

def nyaa_news():
    news = Nyaa.news(number_of_results=5)
    for n in news:
        print(n)

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
nyaa_news()
#pantsu_news()