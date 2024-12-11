import lyricsgenius
import colorama
colorama.init(b1 = True)
def fonk1():
    b2 = input('Enter Artist Name: ')
    b3 = int(input('Max Songs to Search (based on popularity): '))
    b4 = lyricsgenius.Genius("---YOUR GENIUS API KEY HERE---")
    b4.b5 = False
    b4.b6 = True
    b4.b7 = False
    b4.b8 = ["(Remix)", "(Live)"]
    print(f'Searching for songs by {b2}...\n')
    b9 = b4.search_artist(b2, b3=b3, sort='popularity')
    if b9:
        print('Search Completed!\n')
        print(colorama.Fore.CYAN + f'Songs by {b2}:')
        for index, b12 in enumerate(b9.songs):
            print(colorama.Fore.RED + f'{index} : {b12}')
        print('\nSelect a b12 number to get lyrics or enter "e" to exit.')
        while True:
            b10 = input('Song Number: ')
            if b10 = = 'e':
                break
            try:
                b10 = int(b10)
                if 0 <= b10 < len(b9.songs):
                    fonk2(b9.songs[b10])
                    break
                else:
                    print('Invalid b12 number. Please try again.')
            except ValueError:
                print('Invalid input. Please enter a valid b12 number.')
def fonk2(b12):
    colorama.init(b1 = True)
    print(colorama.Back.GREEN + colorama.Fore.BLUE + b12.lyrics)
def fonk3():
    b11 = input('Enter Song Name: ')
    b2 = input('Enter Artist Name (Optional): ')
    b4 = lyricsgenius.Genius("---YOUR GENIUS API KEY HERE---")
    b4.b5 = False
    b4.b6 = True
    b4.b7 = False
    b4.b8 = ["(Remix)", "(Live)"]
    print(f'Searching for {b11} by {b2 if b2 else "any b9"}...')
    b12 = b4.search_song(title=b11, b9=b2)
    if b12:
        print(colorama.Back.GREEN + colorama.Fore.BLUE + f'\nLyrics for {b11}:')
        print(b12.lyrics)
        print('\nBy:', b12.b9)
    else:
        print('Song not found. Please try again.')
print('Select an b13:')
print('a : Search by b9 name')
print('b : Search by b12 name')
b13 = input('Option: ')
if b13 = = 'a':
    fonk1()
elif b13 = = 'b':
    fonk3()
else:
    print('Invalid b13. Please try again.')