from NyaaPy.nyaa import Nyaa
from NyaaPy.nyaa import NyaaPantsu

# Nyaa.si results

nyaa_query = Nyaa.search('new game')
for result in nyaa_query:
    print(result['title'])

# Nyaa.pantsu.cat results
pantsu_query = NyaaPantsu.search('new game')

for result in pantsu_query:
    print(result['title'])
