from nyaapy.anime_site import AnimeTorrentSite
from nyaapy.torrent import TorrentSite


class Nyaa(AnimeTorrentSite):
    SITE = TorrentSite.NYAASI
    URL = "https://nyaa.si"
