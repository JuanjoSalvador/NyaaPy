from NyaaPy.nyaa import Nyaa
from NyaaPy import utils

class SukebeiNyaa(Nyaa):

    def __init__(self):
        self.SITE = utils.TorrentSite.SUKEBEINYAASI
        self.URL = utils.TorrentSite.SUKEBEINYAASI.value
