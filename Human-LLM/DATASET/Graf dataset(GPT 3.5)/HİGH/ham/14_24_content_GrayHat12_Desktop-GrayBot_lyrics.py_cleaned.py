import lyricsgenius
import colorama
b1 = lyricsgenius.Genius("---YOUR GENIUS API KEY HERE---")
b1.b2 = False
b1.b3 = True
b1.b4 = False
b1.b5 = ["(Remix)", "(Live)"]
def fonk1():
    colorama.init(b6 = True)
    b7 = input('Artist Name : ')
    b8 = int(input('Max Songs to search from(based on popularity) : '))
    print('Searching ....../',b9 = '\r')
    b10 = b1.search_artist(b7,max_songs=b8,sort='popularity')
    i,b11 = 0,5
    print('Search Completed ...... )')
    while True:
        print('\n\n\n')
        for a in range(i,b11):
            print(colorama.Fore.RED+colorama.Back.CYAN+str(str(a)+' : '+str(b10.songs[a])),b9 = '\n\n')
        print('n : for more\nb : to move back\nsong number to get lyrics\ne : to quit')
        b12 = input('..> ')
        if b12 = = 'n':
            i+=5
            b11+=5
        elif b12 = = 'b':
            i-=5
            b11-=5
        elif b12 = = 'e':
            break
        else:
            a1 = -1
            try:
                a1 = int(b12)
            except Exception as ex:
                a1 = -1
            if a1 >= i and a1 <b11:
                fonk2(b10.songs[a1])
                break
            else:
                print('Invalid Song number')
                continue
def fonk2(b14):
    colorama.init(b6 = True)
    print(colorama.Back.GREEN+colorama.Fore.BLUE+b14.lyrics)
def fonk3(b14,b10 = ''):
    colorama.init(b6 = True)
    b13 = b1.search_song(title=b14,b10=b10)
    print(colorama.Back.GREEN+colorama.Fore.BLUE+b13.lyrics)
    print('By : ',b13.b10)
print('a : for searching by b10 b7')
print('b : for searching by b14 b7')
b12 = input('...> ')
if b12 = = 'a':
    fonk1()
elif b12 = = 'b':
    b14 = input('Song Name : ')
    b10 = input('Artist Name (Optional) : ')
    fonk3(b14,b10)