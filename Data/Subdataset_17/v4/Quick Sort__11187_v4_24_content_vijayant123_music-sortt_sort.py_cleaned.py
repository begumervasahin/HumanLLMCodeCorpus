import subprocess
import os
import sys
from os import listdir
from os.path import isfile, join
from pygame import mixer
source_path = "/home/error-404/Desktop/songs"
save_path = "/home/error-404/Desktop/dance"
alt_path = "/home/error-404/Desktop/others"
song_files = [f for f in listdir(source_path) if isfile(join(source_path, f))]
mixer.init()
is_paused = False
for song in song_files:
    print(song)
    mixer.music.load(join(source_path, song))
    mixer.music.play(0, 40)
    while True:
        user_input = input()
        if user_input == 'q':
            sys.exit(0)
        elif user_input.isdigit():
            mixer.music.rewind()
            mixer.music.play(0, int(user_input) * 10)
        elif user_input == '':
            mixer.music.stop()
            os.rename(join(source_path, song), join(alt_path, song))
            break
        elif user_input == '/':
            mixer.music.stop()
            os.rename(join(source_path, song), join(save_path, song))
            break
        elif user_input == 'p':
            if not is_paused:
                mixer.music.pause()
                is_paused = True
            else:
                mixer.music.unpause()
                is_paused = False