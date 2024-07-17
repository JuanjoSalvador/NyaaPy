from nyaapy.nyaa import Nyaa
from pprint import pprint
from datetime import datetime
import json
import sys
import os

# Creating a folder for test_files
# ! not included in github project.
if not os.path.isdir("test_files"):
    os.makedirs("test_files")

nyaa = Nyaa()

# Get fresh torrents
dt_latest_torrents_begin = datetime.now()
latest_torrents = nyaa.last_uploads(100)
dt_latest_torrents_end = datetime.now()
with open("test_files/nyaa_latest_torrent_test.json", "w") as f:
    for torrent in latest_torrents:
        try:
            # This prints it as byte like objects since unicode is fun
            f.write(str(torrent.name.encode("utf-8")) + "\n")
        except AttributeError:
            f.write("No name found for this torrent")

# Search some nasty stuff
dt_search_begin = datetime.now()
test_search = nyaa.search("kimi no na wa")
dt_search_end = datetime.now()
with open("test_files/nyaa_search_test.json", "w") as f:
    for torrent in test_search:
        try:
            # This prints it as byte like objects since unicode is fun
            f.write(str(torrent.name.encode("utf-8")) + "\n")
        except AttributeError:
            f.write("No name found for this torrent")

# Get first torrent from found torrents
dt_single_torrent_begin = datetime.now()
single_torrent = test_search[0]
dt_single_torrent_end = datetime.now()
with open("test_files/nyaa_single_torrent_test.json", "w") as f:
    try:
        # This prints it as byte like objects since unicode is fun
        f.write(str(torrent.name.encode("utf-8")) + "\n")
    except AttributeError:
        f.write("No name found for this torrent")

dt_user_begin = datetime.now()
user_torrents = nyaa.get_user("HorribleSubs")
dt_user_end = datetime.now()
with open("test_files/nyaa_single_user_test.json", "w") as f:
    for torrent in user_torrents:
        try:
            # This prints it as byte like objects since unicode is fun
            f.write(str(torrent.name.encode("utf-8")) + "\n")
        except AttributeError:
            f.write("No name found for this torrent")

print(
    "Latest torrents time:",
    (dt_latest_torrents_end - dt_latest_torrents_begin).microseconds / 1000,
    "msec",
)
print(
    "Test search time:", (dt_search_end - dt_search_begin).microseconds / 1000, "msec"
)
print(
    "Single torrent time:",
    (dt_single_torrent_end - dt_single_torrent_begin).microseconds / 1000,
    "msec",
)
print("Single user time:", (dt_user_end - dt_user_begin).microseconds / 1000, "msec")
