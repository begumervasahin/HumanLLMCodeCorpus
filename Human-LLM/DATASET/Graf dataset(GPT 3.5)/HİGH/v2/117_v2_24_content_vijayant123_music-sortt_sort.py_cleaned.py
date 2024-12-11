import os
import sys
import pygame.mixer as mixer
b1 = "/home/error-404/Desktop/songs"
b2 = "/home/error-404/Desktop/dance"
b3 = "/home/error-404/Desktop/others"
b4 = [file for file in os.listdir(b1) if os.path.isfile(os.path.join(b1, file))]
mixer.init()
b5 = False
for file in b4:
    print("Now playing:", file)
    mixer.music.load(os.path.join(b1, file))
    mixer.music.play(0, 40)
    while True:
        b6 = input()
        if b6.isdigit():
            mixer.music.rewind()
            mixer.music.play(0, int(b6) * 10)
        elif b6 = = '':
            mixer.music.stop()
            os.rename(os.path.join(b1, file), os.path.join(b3, file))
            break
        elif b6 = = '/':
            mixer.music.stop()
            os.rename(os.path.join(b1, file), os.path.join(b2, file))
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