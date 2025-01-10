import uvloop

from nyaapy.anime_site import AnimeTorrentSiteAsync
from nyaapy.torrent import TorrentSite

uvloop.install()


class Nyaa(AnimeTorrentSiteAsync):
    SITE = TorrentSite.NYAASI
    URL = "https://nyaa.si"
