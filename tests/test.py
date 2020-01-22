from NyaaPy import Pantsu, Nyaa
from pprint import pprint
from datetime import datetime

# pantsu = Pantsu()
nyaa = Nyaa()

# Get fresh torrents
dt_latest_torrents_begin = datetime.now()
latest_torrents = nyaa.last_uploads(100)
dt_latest_torrents_end = datetime.now()

# I'd like to watch Tenki no ko, but not uploaded yet.
dt_search_begin = datetime.now()
test_search = nyaa.search("Kimi no Na wa")
dt_search_end = datetime.now()
# pprint(test_search)

# Get first torrent from found torrents
# print("First result torrent info:")
dt_single_torrent_begin = datetime.now()
single_torrent = nyaa.get(test_search[0]["id"])
dt_single_torrent_end = datetime.now()
#pprint(single_torrent)

dt_user_begin = datetime.now()
user_torrents = nyaa.get_user("Lilith-Raws")
dt_user_end = datetime.now()
#pprint(user_torrents)

print(
    "Latest torrents time:",
    (dt_latest_torrents_end - dt_latest_torrents_begin).microseconds / 1000,
    "msec")
print(
    "Test search time:", 
    (dt_search_end - dt_search_begin).microseconds/ 1000,
    "msec"
)
print(
    "Single torrent time:",
    (dt_single_torrent_end - dt_single_torrent_begin).microseconds / 1000,
    "msec"
)
print(
    "Single user time:",
    (dt_user_end - dt_user_begin ).microseconds / 1000, 
    "msec"
)

"""
print(pantsu.search(keyword='koe no katachi',
                    lang=["es", "ja"], category=[1, 3]))
"""
