# 8.8 user akbums

def make_album(artist_name, album_name, no_of_tracks=''):
    all_albums = {'Artist Name':artist_name, 'Album name': album_name}
    if no_of_tracks:
        all_albums['Number of tracks'] = no_of_tracks
    return all_albums


while True:
    name = input("\nWhat is your name? ")
    album_name = input("What is the name of your album? ")
    final = make_album(name, album_name)
    print(final)

    check = input("Do you wnat to continue or quit the program? (yes/no) ")
    if check == 'no':
        break