import urllib
from urllib.parse import urlencode
from urllib.parse import quote


def magnet_builder(info_hash, title):
    """
    Generates a magnet link using the info_hash and title of a given file.
    """
    known_trackers = [
        "http://nyaa.tracker.wf:7777/announce",
        "udp://open.stealth.si:80/announce",
        "udp://tracker.opentrackr.org:1337/announce",
        "udp://exodus.desync.com:6969/announce",
        "udp://tracker.torrent.eu.org:451/announce",
    ]

    magnet_link = f"magnet:?xt=urn:btih:{info_hash}&" + urlencode(
        {"dn": title}, quote_via=quote
    )
    for tracker in known_trackers:
        magnet_link += f"&{urlencode({'tr': tracker})}"

    return magnet_link
