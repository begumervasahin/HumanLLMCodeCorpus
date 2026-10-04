import os
import sys
from os import listdir
from os.path import isfile, join
from pygame import mixer
b1 = "/home/error-404/Desktop/songs"
b2 = "/home/error-404/Desktop/dance"
b3 = "/home/error-404/Desktop/others"
b4 = [f for f in listdir(b1) if isfile(join(b1, f))]
mixer.init()
a1 = 0
for f in b4:
    print(f)
    mixer.music.load(join(b1, f))
    mixer.music.play(0, 40)
    while True:
        b5 = input()
        if b5 = = 'q':
            sys.exit(0)
        elif b5.isdigit() and '0' <= b5 <= '9':
            mixer.music.rewind()
            mixer.music.play(0, int(b5) * 10)
        elif b5 = = '':
            mixer.music.stop()
            os.rename(join(b1, f), join(b3, f))
            break
        elif b5 = = '/':
            mixer.music.stop()
            os.rename(join(b1, f), join(b2, f))
            break
        elif b5 = = 'p':
            if a1 = = 0:
                mixer.music.pause()
                a1 = 1
            else:
                mixer.music.unpause()
                a1 = 0