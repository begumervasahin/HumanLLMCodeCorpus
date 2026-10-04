import os
import sys
from os import listdir
from os.path import isfile, join
from pygame import mixer
SOURCE_PATH = "/home/error-404/Desktop/songs"
SAVE_PATH = "/home/error-404/Desktop/dance"
ALT_PATH = "/home/error-404/Desktop/others"
def get_song_files(path):
    return [f for f in listdir(path) if isfile(join(path, f))]
def play_song(song_path, start_time=40):
    mixer.music.load(song_path)
    mixer.music.play(0, start_time)
def handle_user_input(song_path):
    global is_paused
    while True:
        user_input = input().strip()
        if user_input == 'q':
            sys.exit(0)
        elif user_input.isdigit():
            mixer.music.rewind()
            mixer.music.play(0, int(user_input) * 10)
        elif user_input == '':
            mixer.music.stop()
            os.rename(song_path, join(ALT_PATH, os.path.basename(song_path)))
            break
        elif user_input == '/':
            mixer.music.stop()
            os.rename(song_path, join(SAVE_PATH, os.path.basename(song_path)))
            break
        elif user_input == 'p':
            if not is_paused:
                mixer.music.pause()
                is_paused = True
            else:
                mixer.music.unpause()
                is_paused = False
def main():
    mixer.init()
    song_files = get_song_files(SOURCE_PATH)
    for song in song_files:
        song_path = join(SOURCE_PATH, song)
        print(song)
        play_song(song_path)
        handle_user_input(song_path)
if __name__ == "__main__":
    main()