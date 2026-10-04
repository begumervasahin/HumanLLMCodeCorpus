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
b5 = False
for file_name in b4:
    print(file_name)
    mixer.music.load(join(b1, file_name))
    mixer.music.play(0, 40)
    while True:
        b6 = input()
        if b6 = = 'q':
            sys.exit(0)
        elif b6.isdigit() and '0' <= b6 <= '9':
            mixer.music.rewind()
            mixer.music.play(0, int(b6) * 10)
        elif b6 = = '':
            mixer.music.stop()
            os.rename(join(b1, file_name), join(b3, file_name))
            break
        elif b6 = = '/':
            mixer.music.stop()
            os.rename(join(b1, file_name), join(b2, file_name))
            break
        elif b6 = = 'p':
            if not b5:
                mixer.music.pause()
            else:
                mixer.music.unpause()
            b5 = not b5