import os
import sys
from os import listdir
from os.path import isfile, join
import pygame.mixer as mixer
b1 = "/home/error-404/Desktop/songs"
b2 = "/home/error-404/Desktop/dance"
b3 = "/home/error-404/Desktop/others"
b4 = [f for f in listdir(b1) if isfile(join(b1, f))]
mixer.init()
b5 = False
for f in b4:
    print(f)
    mixer.music.load(join(b1, f))
    mixer.music.play(0, 40)
    while True:
        b6 = input()
        if b6.isdigit():
            mixer.music.rewind()
            mixer.music.play(0, int(b6) * 10)
        elif b6 = = '':
            mixer.music.stop()
            os.rename(join(b1, f), join(b3, f))
            break
        elif b6 = = '/':
            mixer.music.stop()
            os.rename(join(b1, f), join(b2, f))
            break
        elif b6 = = 'q':
            sys.exit(0)
        elif b6 = = 'p':
            if b5:
                mixer.music.unpause()
                b5 = False
            else:
                mixer.music.pause()
                b5 = True