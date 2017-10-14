from NyaaPy import Nyaa, NyaaPantsu

# Nyaa.si results
def nyaa_search():
    try:
        nyaa_query = Nyaa.search(keyword='koe no katachi 1080', category=1, subcategory=0, page=0)

        for nyaa in nyaa_query:
            print(nyaa)
    except TypeError as te:
        print(te)

def nyaa_news():
    news = Nyaa.news(number_of_results=5)
    for n in news:
        print(n)

# Nyaa.pantsu.cat results
def pantsu_search():
    pantsu_query = NyaaPantsu.search('new game!!')


def pantsu_news():
    print(NyaaPantsu.news(1))

# Uncomment whatever you want to test

#nyaa_search()
#pantsu_search()
#nyaa_news()
pantsu_news()