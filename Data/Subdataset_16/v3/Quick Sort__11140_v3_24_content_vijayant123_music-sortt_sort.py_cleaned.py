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
def fonk2(file_path, start_time):
    mixer.music.load(file_path)
    mixer.music.play(0, start_time)
def fonk3(src, dest):
    os.rename(src, join(dest, os.path.basename(src)))
def fonk4(file_name):
    global b5
    while True:
        b4 = input()
        if b4 = = 'q':
            sys.exit(0)
        elif b4.isdigit() and 0 <= int(b4) <= 9:
            mixer.music.rewind()
            fonk2(join(b1, file_name), int(b4) * 10)
        elif b4 = = '':
            mixer.music.stop()
            fonk3(join(b1, file_name), b3)
            break
        elif b4 = = '/':
            mixer.music.stop()
            fonk3(join(b1, file_name), b2)
            break
        elif b4 = = 'p':
            if not b5:
                mixer.music.pause()
            else:
                mixer.music.unpause()
            b5 = not b5
def fonk5():
    b6 = fonk1(b1)
    mixer.init()
    for file_name in b6:
        print(file_name)
        fonk2(join(b1, file_name), 40)
        fonk4(file_name)
if b7 = = "__main__":
    b5 = False
    fonk5()