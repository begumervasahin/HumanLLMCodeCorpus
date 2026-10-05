import lyricsgenius
import colorama
colorama.init(b1 = True)
def fonk1():
    b2 = lyricsgenius.Genius("---YOUR GENIUS API KEY HERE---")
    b2.b3 = False
    b2.b4 = True
    b2.b5 = False
    b2.b6 = ["(Remix)", "(Live)"]
    return b2
def fonk2():
    b7 = input('Enter Artist Name: ')
    b8 = int(input('Max Songs to Search (based on popularity): '))
    b2 = fonk1()
    print(f'Searching for songs by {b7}...\n')
    b9 = b2.search_artist(b7, b8=b8, sort='popularity')
    if b9:
        print('Search Completed!\n')
        print(colorama.Fore.CYAN + f'Songs by {b7}:')
        fonk3(b9.songs)
        fonk4(b9.songs)
def fonk3(songs):
    for index, b12 in enumerate(songs):
        print(colorama.Fore.RED + f'{index} : {b12}')
def fonk4(songs):
    print('\nSelect a b12 number to get lyrics or enter "e" to exit.')
    while True:
        b10 = input('Song Number: ')
        if b10 = = 'e':
            break
        try:
            b10 = int(b10)
            if 0 <= b10 < len(songs):
                fonk5(songs[b10])
                break
            else:
                print('Invalid b12 number. Please try again.')
        except ValueError:
            print('Invalid input. Please enter a valid b12 number.')
def fonk5(b12):
    colorama.init(b1 = True)
    print(colorama.Back.GREEN + colorama.Fore.BLUE + b12.lyrics)
def fonk6():
    b11 = input('Enter Song Name: ')
    b7 = input('Enter Artist Name (Optional): ')
    b2 = fonk1()
    print(f'Searching for {b11} by {b7 if b7 else "any b9"}...')
    b12 = b2.search_song(title=b11, b9=b7)
    if b12:
        print(colorama.Back.GREEN + colorama.Fore.BLUE + f'\nLyrics for {b11}:')
        print(b12.lyrics)
        print('\nBy:', b12.b9)
    else:
        print('Song not found. Please try again.')
def fonk7():
    print('Select an b13:')
    print('a : Search by b9 name')
    print('b : Search by b12 name')
    b13 = input('Option: ')
    if b13 = = 'a':
        fonk2()
    elif b13 = = 'b':
        fonk6()
    else:
        print('Invalid b13. Please try again.')
if b14 = = "__main__":
    fonk7()