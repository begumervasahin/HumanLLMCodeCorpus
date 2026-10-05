import os
import sys
from os import listdir
from os.path import isfile, join
from pygame import mixer
SONGS_DIR = "/home/error-404/Desktop/songs"
SAVE_DIR = "/home/error-404/Desktop/dance"
ALT_DIR = "/home/error-404/Desktop/others"
def get_song_files(directory):
    return [f for f in listdir(directory) if isfile(join(directory, f))]
def move_file(src, dest):
    os.rename(src, join(dest, os.path.basename(src)))
def main():
    song_files = get_song_files(SONGS_DIR)
    mixer.init()
    for song_file in song_files:
        print(song_file)
        mixer.music.load(join(SONGS_DIR, song_file))
        mixer.music.play(0, 40)
        while True:
            user_input = input()
            if user_input == 'q':
                sys.exit(0)
            elif user_input.isdigit():
                mixer.music.rewind()
                mixer.music.play(0, int(user_input) * 10)
            elif not user_input:
                mixer.music.stop()
                move_file(join(SONGS_DIR, song_file), ALT_DIR)
                break
            elif user_input == '/':
                mixer.music.stop()
                move_file(join(SONGS_DIR, song_file), SAVE_DIR)
                break
            elif user_input == 'p':
                if mixer.music.get_busy():
                    if mixer.music.get_pos() > 0:
                        mixer.music.pause()
                    else:
                        mixer.music.unpause()
if __name__ == "__main__":
    main()