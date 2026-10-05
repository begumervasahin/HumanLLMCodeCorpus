import os
import sys
import pygame.mixer as mixer
input_directory = "/home/error-404/Desktop/songs"
save_directory = "/home/error-404/Desktop/dance"
alternative_directory = "/home/error-404/Desktop/others"
audio_files = [file for file in os.listdir(input_directory) if os.path.isfile(os.path.join(input_directory, file))]
mixer.init()
paused = False
def play_audio(file_path, start_time=0):
    mixer.music.load(file_path)
    mixer.music.play(0, start_time)
def move_and_stop(file_path, target_directory):
    mixer.music.stop()
    os.rename(file_path, os.path.join(target_directory, os.path.basename(file_path)))
for file_name in audio_files:
    print("Now playing:", file_name)
    file_path = os.path.join(input_directory, file_name)
    play_audio(file_path, 40)
    while True:
        user_input = input()
        if user_input.isdigit():
            play_audio(file_path, int(user_input) * 10)
        elif user_input == '':
            move_and_stop(file_path, alternative_directory)
            break
        elif user_input == '/':
            move_and_stop(file_path, save_directory)
            break
        elif user_input == 'q':
            sys.exit(0)
        elif user_input == 'p':
            if paused:
                mixer.music.unpause()
                paused = False
            else:
                mixer.music.pause()
                paused = True