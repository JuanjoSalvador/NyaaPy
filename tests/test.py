from NyaaPy import Pantsu, Nyaa
from pprint import pprint

# pantsu = Pantsu()
nyaa = Nyaa()

# Get fresh torrents
print("Latest torrents:")
latest_torrents = rnyaa.last_uploads(5)

# I'd like to watch Tenki no ko, but not uploaded yet.
print("Search results for Kimi no Na wa:")
test_search = nyaa.search("Kimi no Na wa")
pprint(test_search)

# Get first torrent from found torrents
print("First result torrent info:")
single_torrent = nyaa.get(test_search[0]["id"])
pprint(single_torrent)

"""
print(pantsu.search(keyword='koe no katachi',
                    lang=["es", "ja"], category=[1, 3]))
"""
