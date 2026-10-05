import os
import sys
import pygame.mixer as mixer
input_directory = "/home/error-404/Desktop/songs"
save_directory = "/home/error-404/Desktop/dance"
alternative_directory = "/home/error-404/Desktop/others"
audio_files = [file for file in os.listdir(input_directory) if os.path.isfile(os.path.join(input_directory, file))]
mixer.init()
paused = False
for file in audio_files:
    print("Now playing:", file)
    mixer.music.load(os.path.join(input_directory, file))
    mixer.music.play(0, 40)
    while True:
        user_input = input()
        if user_input.isdigit():
            mixer.music.rewind()
            mixer.music.play(0, int(user_input) * 10)
        elif user_input == '':
            mixer.music.stop()
            os.rename(os.path.join(input_directory, file), os.path.join(alternative_directory, file))
            break
        elif user_input == '/':
            mixer.music.stop()
            os.rename(os.path.join(input_directory, file), os.path.join(save_directory, file))
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