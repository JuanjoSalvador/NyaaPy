from NyaaPy.nyaa import Nyaa
from NyaaPy.nyaa import NyaaPantsu
import json

# Nyaa.si results
nyaa_query = Nyaa.search('koe no katachi 1080')

if len(nyaa_query) > 0:
    for result in nyaa_query:
        print(result['title'])
else:
    print('Nothing here!')

# Nyaa.pantsu.cat results
pantsu_query = NyaaPantsu.search('new game!!')
if len(pantsu_query) > 0:
    for result in pantsu_query:
        print(result['title'])
else:
    print('Nothing here!')
