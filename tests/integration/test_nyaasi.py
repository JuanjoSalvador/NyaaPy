from nyaapy.nyaasi.nyaa import Nyaa
from nyaapy.torrent import Torrent

def test_nyaa_last_uploads():
    request = Nyaa.last_uploads(number_of_results=10)
    torrent = request[0]

    assert isinstance(torrent, Torrent) == True
    assert len(request) == 10


def test_nyaa_search():
    request = Nyaa.search(keyword="koe no katachi")
    torrent = request[0]

    assert isinstance(torrent, Torrent) == True


def test_nyaa_get_single():
    request = Nyaa.get(view_id='1847113')

    assert isinstance(request, Torrent) == True


def test_nyaa_get_from_user():
    request = Nyaa.get_from_user(username="Erai-raws")
    torrent = request[0]

    assert isinstance(torrent, Torrent) == True
    assert len(request) <= 75