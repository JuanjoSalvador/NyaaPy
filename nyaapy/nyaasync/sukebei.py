import uvloop

from nyaapy.anime_site import AnimeTorrentSiteAsync
from nyaapy.torrent import TorrentSite

uvloop.install()


class SukebeiNyaa(AnimeTorrentSiteAsync):
    SITE = TorrentSite.SUKEBEINYAASI
    URL = "https://sukebei.nyaa.si"
