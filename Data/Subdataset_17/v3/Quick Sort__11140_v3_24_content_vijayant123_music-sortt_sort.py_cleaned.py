import os
import sys
from os import listdir
from os.path import isfile, join
from pygame import mixer
SONG_DIR = "/home/error-404/Desktop/songs"
DANCE_DIR = "/home/error-404/Desktop/dance"
OTHER_DIR = "/home/error-404/Desktop/others"
def list_files(directory):
    return [f for f in listdir(directory) if isfile(join(directory, f))]
def play_song(file_path, start_time):
    mixer.music.load(file_path)
    mixer.music.play(0, start_time)
def move_file(src, dest):
    os.rename(src, join(dest, os.path.basename(src)))
def process_input(file_name):
    global is_paused
    while True:
        user_input = input()
        if user_input == 'q':
            sys.exit(0)
        elif user_input.isdigit() and 0 <= int(user_input) <= 9:
            mixer.music.rewind()
            play_song(join(SONG_DIR, file_name), int(user_input) * 10)
        elif user_input == '':
            mixer.music.stop()
            move_file(join(SONG_DIR, file_name), OTHER_DIR)
            break
        elif user_input == '/':
            mixer.music.stop()
            move_file(join(SONG_DIR, file_name), DANCE_DIR)
            break
        elif user_input == 'p':
            if not is_paused:
                mixer.music.pause()
            else:
                mixer.music.unpause()
            is_paused = not is_paused
def main():
    song_files = list_files(SONG_DIR)
    mixer.init()
    for file_name in song_files:
        print(file_name)
        play_song(join(SONG_DIR, file_name), 40)
        process_input(file_name)
if __name__ == "__main__":
    is_paused = False
    main()