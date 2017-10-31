from NyaaPy import Nyaa

# Nyaa.si results
nyaa_query = Nyaa.search()

nyaa_news = Nyaa.news(5)

if len(nyaa_query) > 0:
    for result in nyaa_query:
        print(result['name'])
else:
    print('Nothing here!')