import os
import sys
from os import listdir
from os.path import isfile, join
import pygame.mixer as mixer
mypath = "/home/error-404/Desktop/songs"
savepath = "/home/error-404/Desktop/dance"
altpath = "/home/error-404/Desktop/others"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
mixer.init()
flag = False
for f in onlyfiles:
    print(f)
    mixer.music.load(join(mypath, f))
    mixer.music.play(0, 40)
    while True:
        a = input()
        if a.isdigit():
            mixer.music.rewind()
            mixer.music.play(0, int(a) * 10)
        elif a == '':
            mixer.music.stop()
            os.rename(join(mypath, f), join(altpath, f))
            break
        elif a == '/':
            mixer.music.stop()
            os.rename(join(mypath, f), join(savepath, f))
            break
        elif a == 'q':
            sys.exit(0)
        elif a == 'p':
            if flag:
                mixer.music.unpause()
                flag = False
            else:
                mixer.music.pause()
                flag = True