from NyaaPy import SukebeiNyaa
from pprint import pprint
from datetime import datetime
import json
import sys
import os

# Creating a folder for test_files
# ! not included in github project.
if not os.path.isdir("test_files"):
    os.makedirs("test_files")

nyaa = SukebeiNyaa()

# Get fresh torrents
dt_latest_torrents_begin = datetime.now()
latest_torrents = nyaa.last_uploads(100)
dt_latest_torrents_end = datetime.now()
with open("test_files/sukebei_latest_torrent_test.json", 'w') as f:
    json.dump(latest_torrents, f)

# Search some nasty stuff
dt_search_begin = datetime.now()
test_search = nyaa.search("G Senjou no maou")
dt_search_end = datetime.now()
with open("test_files/sukebei_search_test.json", 'w') as f:
    json.dump(test_search, f)

# Get first torrent from found torrents
dt_single_torrent_begin = datetime.now()
single_torrent = nyaa.get(test_search[0]["id"])
dt_single_torrent_end = datetime.now()
with open("test_files/sukebei_single_torrent_test.json", 'w') as f:
    json.dump(single_torrent, f)

dt_user_begin = datetime.now()
user_torrents = nyaa.get_user("RUNBKK")
dt_user_end = datetime.now()
with open("test_files/sukebei_single_user_test.json", 'w') as f:
    json.dump(user_torrents, f)

print(
    "Latest torrents time:",
    (dt_latest_torrents_end - dt_latest_torrents_begin).microseconds / 1000,
    "msec")
print(
    "Test search time:",
    (dt_search_end - dt_search_begin).microseconds / 1000,
    "msec"
)
print(
    "Single torrent time:",
    (dt_single_torrent_end - dt_single_torrent_begin).microseconds / 1000,
    "msec"
)
print(
    "Single user time:",
    (dt_user_end - dt_user_begin).microseconds / 1000,
    "msec"
)
