class Torrent(object):
    def __init__(self, nyaa_item: dict):
        for key in nyaa_item:
            setattr(self, key, nyaa_item[key])



