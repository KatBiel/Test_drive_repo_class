from lib.album import *

'''Album construck with title, release_year, artist_id'''

def test_album_constructor():
    album = Album(1, 'Doolittle', 1989, 1)
    assert album.id == 1
    assert album.title == 'Doolittle'
    assert album.release_year == 1989
    assert album.artist_id == 1

def test_equality():
    album_1 = Album(1, 'Doolittle', 1989, 1)
    album_2 = Album(1, 'Doolittle', 1989, 1)
    assert album_1 == album_2

def test_formatting():
    album = Album(1, 'Doolittle', 1989, 1)
    assert str(album) == "Album(1, Doolittle, 1989, 1)"