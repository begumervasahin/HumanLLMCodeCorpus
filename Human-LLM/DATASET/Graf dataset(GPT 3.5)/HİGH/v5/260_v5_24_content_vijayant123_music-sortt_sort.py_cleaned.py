import os
import sys
from os import listdir
from os.path import isfile, join
from pygame import mixer
b1 = "/home/error-404/Desktop/songs"
b2 = "/home/error-404/Desktop/dance"
b3 = "/home/error-404/Desktop/others"
def fonk1(directory):
    return [f for f in listdir(directory) if isfile(join(directory, f))]
def fonk2(src, dest):
    os.rename(src, join(dest, os.path.basename(src)))
def fonk3():
    b4 = fonk1(b1)
    mixer.init()
    for song_file in b4:
        print(song_file)
        mixer.music.load(join(b1, song_file))
        mixer.music.play(0, 40)
        while True:
            b5 = input()
            if b5 = = 'q':
                sys.exit(0)
            elif b5.isdigit():
                mixer.music.rewind()
                mixer.music.play(0, int(b5) * 10)
            elif not b5:
                mixer.music.stop()
                fonk2(join(b1, song_file), b3)
                break
            elif b5 = = '/':
                mixer.music.stop()
                fonk2(join(b1, song_file), b2)
                break
            elif b5 = = 'p':
                if mixer.music.get_busy():
                    if mixer.music.get_pos() > 0:
                        mixer.music.pause()
                    else:
                        mixer.music.unpause()
if b6 = = "__main__":
    fonk3()