import os
import sys
import pygame.mixer as mixer
b1 = "/home/error-404/Desktop/songs"
b2 = "/home/error-404/Desktop/dance"
b3 = "/home/error-404/Desktop/others"
b4 = [file for file in os.listdir(b1) if os.path.isfile(os.path.join(b1, file))]
mixer.init()
b5 = False
def fonk1(b7, b6 = 0):
    mixer.music.load(b7)
    mixer.music.play(0, b6)
def fonk2(b7, target_directory):
    mixer.music.stop()
    os.rename(b7, os.path.join(target_directory, os.path.basename(b7)))
for file_name in b4:
    print("Now playing:", file_name)
    b7 = os.path.join(b1, file_name)
    fonk1(b7, 40)
    while True:
        b8 = input()
        if b8.isdigit():
            fonk1(b7, int(b8) * 10)
        elif b8 = = '':
            fonk2(b7, b3)
            break
        elif b8 = = '/':
            fonk2(b7, b2)
            break
        elif b8 = = 'q':
            sys.exit(0)
        elif b8 = = 'p':
            if b5:
                mixer.music.unpause()
                b5 = False
            else:
                mixer.music.pause()
                b5 = True