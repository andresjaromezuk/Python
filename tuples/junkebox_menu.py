from tuples import albums
SONG_LIST_INDEX = 3
SONG_TITLE_INDEX = 1

while True: 
    print("elije tu álbum:")
    for index, (title, artist, year, songs) in enumerate(albums):
        print(f"{index + 1} {title}")
    choice = int(input())
    if 1<= choice <= len(albums):
        song_list = albums[choice - 1][SONG_LIST_INDEX]
    else:
        break
    for index, (track, song) in enumerate(song_list):
        print(f"{index + 1}. {song}")
    song_choice = int(input())
    if 1 <= song_choice <= len(song_list):
        title = song_list[song_choice - 1][SONG_TITLE_INDEX]
        print(title)