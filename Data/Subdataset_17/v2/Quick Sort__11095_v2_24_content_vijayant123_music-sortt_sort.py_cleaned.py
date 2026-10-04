import os
import sys
from os import listdir
from os.path import isfile, join
from pygame import mixer
SONG_DIR = "/home/error-404/Desktop/songs"
DANCE_DIR = "/home/error-404/Desktop/dance"
OTHER_DIR = "/home/error-404/Desktop/others"
song_files = [f for f in listdir(SONG_DIR) if isfile(join(SONG_DIR, f))]
mixer.init()
is_paused = False
for file_name in song_files:
    print(file_name)
    mixer.music.load(join(SONG_DIR, file_name))
    mixer.music.play(0, 40)
    while True:
        user_input = input()
        if user_input == 'q':
            sys.exit(0)
        elif user_input.isdigit() and '0' <= user_input <= '9':
            mixer.music.rewind()
            mixer.music.play(0, int(user_input) * 10)
        elif user_input == '':
            mixer.music.stop()
            os.rename(join(SONG_DIR, file_name), join(OTHER_DIR, file_name))
            break
        elif user_input == '/':
            mixer.music.stop()
            os.rename(join(SONG_DIR, file_name), join(DANCE_DIR, file_name))
            break
        elif user_input == 'p':
            if not is_paused:
                mixer.music.pause()
            else:
                mixer.music.unpause()
            is_paused = not is_paused