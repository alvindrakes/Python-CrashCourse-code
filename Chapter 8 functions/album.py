#8.7 album

def make_album(artist_name, album_name, no_of_tracks=''):
    all_albums = {'Artist Name':artist_name, 'Album name': album_name}
    if no_of_tracks:
        all_albums['Number of tracks'] = no_of_tracks
    return all_albums


album = make_album('Alvin', 'Rock', 23)
print(album)

album = make_album('kon', 'Ynag')
print(album)

album = make_album('Jaden', 'Taka')
print(album)