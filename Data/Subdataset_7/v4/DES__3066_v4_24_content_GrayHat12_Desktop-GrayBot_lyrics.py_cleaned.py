import lyricsgenius
import colorama
b1 = lyricsgenius.Genius("---YOUR GENIUS API KEY HERE---")
b1.b2 = False
b1.b3 = True
b1.b4 = False
b1.b5 = ["(Remix)", "(Live)"]
def fonk1():
    colorama.init(b6 = True)
    b7 = input('Enter Artist Name: ')
    b8 = int(input('Max Songs to search (based on popularity): '))
    print(f'Searching for songs by {b7}...\n')
    b9 = b1.search_artist(b7, b8=b8, sort='popularity')
    if b9:
        print('Search Completed!\n')
        fonk2(b9)
        fonk3(b9.songs)
def fonk2(b9):
    i, b10 = 0, 5
    while True:
        print('\n\n\n')
        for a in range(i, b10):
            print(colorama.Fore.RED + colorama.Back.CYAN + f'{a} : {b9.songs[a]}\n')
        print('n : for more\nb : to move back\nsong number to get lyrics\ne : to quit')
        b11 = input('..> ')
        if b11 = = 'n':
            i += 5
            b10 += 5
        elif b11 = = 'b':
            i -= 5
            b10 -= 5
        elif b11 = = 'e':
            break
        else:
            try:
                b12 = int(b11)
                if i <= b12 < b10:
                    fonk4(b9.songs[b12])
                    break
                else:
                    print('Invalid Song number')
            except ValueError:
                print('Invalid input. Please enter a valid b15 number.')
def fonk3(songs):
    b13 = input('Song Number: ')
    if b13.isdigit():
        b12 = int(b13)
        if 0 <= b12 < len(songs):
            fonk4(songs[b12])
        else:
            print('Invalid b15 number. Please try again.')
    else:
        print('Invalid input. Please enter a valid b15 number.')
def fonk4(b15):
    colorama.init(b6 = True)
    print(colorama.Back.GREEN + colorama.Fore.BLUE + b15.lyrics)
    print('By:', b15.b9)
def fonk5():
    colorama.init(b6 = True)
    b14 = input('Enter Song Name: ')
    b7 = input('Enter Artist Name (Optional): ')
    b15 = b1.search_song(title=b14, b9=b7)
    if b15:
        print(colorama.Back.GREEN + colorama.Fore.BLUE + f'\nLyrics for {b14}:')
        print(b15.lyrics)
        print('By:', b15.b9)
    else:
        print('Song not found. Please try again.')
print('Select an b16:')
print('a : Search by b9 name')
print('b : Search by b15 name')
b16 = input('Option: ')
if b16 = = 'a':
    fonk1()
elif b16 = = 'b':
    fonk5()
else:
    print('Invalid b16. Please try again.')