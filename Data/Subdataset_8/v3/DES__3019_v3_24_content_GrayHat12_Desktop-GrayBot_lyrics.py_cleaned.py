import lyricsgenius
import colorama
colorama.init(autoreset=True)
def initialize_genius():
    genius = lyricsgenius.Genius("---YOUR GENIUS API KEY HERE---")
    genius.verbose = False
    genius.remove_section_headers = True
    genius.skip_non_songs = False
    genius.excluded_terms = ["(Remix)", "(Live)"]
    return genius
def search_by_artist():
    artist_name = input('Enter Artist Name: ')
    max_songs = int(input('Max Songs to Search (based on popularity): '))
    genius = initialize_genius()
    print(f'Searching for songs by {artist_name}...\n')
    artist = genius.search_artist(artist_name, max_songs=max_songs, sort='popularity')
    if artist:
        print('Search Completed!\n')
        print(colorama.Fore.CYAN + f'Songs by {artist_name}:')
        display_songs(artist.songs)
        prompt_song_selection(artist.songs)
def display_songs(songs):
    for index, song in enumerate(songs):
        print(colorama.Fore.RED + f'{index} : {song}')
def prompt_song_selection(songs):
    print('\nSelect a song number to get lyrics or enter "e" to exit.')
    while True:
        song_number = input('Song Number: ')
        if song_number == 'e':
            break
        try:
            song_number = int(song_number)
            if 0 <= song_number < len(songs):
                show_lyrics(songs[song_number])
                break
            else:
                print('Invalid song number. Please try again.')
        except ValueError:
            print('Invalid input. Please enter a valid song number.')
def show_lyrics(song):
    colorama.init(autoreset=True)
    print(colorama.Back.GREEN + colorama.Fore.BLUE + song.lyrics)
def search_by_song():
    song_name = input('Enter Song Name: ')
    artist_name = input('Enter Artist Name (Optional): ')
    genius = initialize_genius()
    print(f'Searching for {song_name} by {artist_name if artist_name else "any artist"}...')
    song = genius.search_song(title=song_name, artist=artist_name)
    if song:
        print(colorama.Back.GREEN + colorama.Fore.BLUE + f'\nLyrics for {song_name}:')
        print(song.lyrics)
        print('\nBy:', song.artist)
    else:
        print('Song not found. Please try again.')
def main():
    print('Select an option:')
    print('a : Search by artist name')
    print('b : Search by song name')
    option = input('Option: ')
    if option == 'a':
        search_by_artist()
    elif option == 'b':
        search_by_song()
    else:
        print('Invalid option. Please try again.')
if __name__ == "__main__":
    main()