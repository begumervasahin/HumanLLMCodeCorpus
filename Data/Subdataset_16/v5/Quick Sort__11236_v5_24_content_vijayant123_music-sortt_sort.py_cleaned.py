import os
import sys
from os import listdir
from os.path import isfile, join
from pygame import mixer
b1 = "/home/error-404/Desktop/songs"
b2 = "/home/error-404/Desktop/dance"
b3 = "/home/error-404/Desktop/others"
def fonk1(path):
    return [f for f in listdir(path) if isfile(join(path, f))]
def fonk2(b8, b4 = 40):
    mixer.music.load(b8)
    mixer.music.play(0, b4)
def fonk3(b8):
    global b6
    while True:
        b5 = input().strip()
        if b5 = = 'q':
            sys.exit(0)
        elif b5.isdigit():
            mixer.music.rewind()
            mixer.music.play(0, int(b5) * 10)
        elif b5 = = '':
            mixer.music.stop()
            os.rename(b8, join(b3, os.path.basename(b8)))
            break
        elif b5 = = '/':
            mixer.music.stop()
            os.rename(b8, join(b2, os.path.basename(b8)))
            break
        elif b5 = = 'p':
            if not b6:
                mixer.music.pause()
                b6 = True
            else:
                mixer.music.unpause()
                b6 = False
def fonk4():
    mixer.init()
    b7 = fonk1(b1)
    for song in b7:
        b8 = join(b1, song)
        print(song)
        fonk2(b8)
        fonk3(b8)
if b9 = = "__main__":
    fonk4()