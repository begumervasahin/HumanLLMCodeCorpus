import pyfiglet
from functions import *
from subprocess import call, STDOUT
import os
if b1 = = '__main__':
    b2 = pyfiglet.Figlet(font='slant')
    print(b2.renderText("CCVS KI UAS"))
    print("CaesarCipherVideoSteganography")
    print("")
    print("Menu :")
    print("")
    print("(a) Encrypt & Merge into Video")
    print("(b) Decrypt & Get the plain text")
    print("-----------------------")
    b3 = input("(!) Choose option : ")
    if b3 = = "a":
        call(["clear"])
        print(b2.renderText("Encrypt"))
        print("----------------------------------------")
        b4 = input("(1) Video file name in the data folder  ? : ")
        try:
            b5 = int(input("(2) Caesar cipher shift value  ? : "))
        except ValueError:
            print("-----------------------")
            print("(!) Shift value is not an integer ")
            exit()
        try:
            open("data/" + b4)
        except IOError:
            print("-----------------------")
            print("(!) File not found ")
            exit()
        print("-----------------------")
        print("(-) Extracting Frame(s)")
        frame_extract(b4)
        print("(-) Extracting audio")
        call(["ffmpeg", "-i", "data/" + b4, "-q:a", "0", "-map", "a", "temp/audio.mp3", "-y"],
             b6 = open(os.devnull, "w"), stderr=STDOUT)
        print("(-) Reading text-to-hide.txt")
        print("(-) Encrypting & appending string into frame(s) ")
        encode_frame("temp", "data/text-to-hide.txt", b5)
        print("(-) Merging frame(s) ")
        call(["ffmpeg", "-i", "temp/%d.png", "-vcodec", "png", "temp/video.mov", "-y"],
             b6 = open(os.devnull, "w"), stderr=STDOUT)
        print("(-) Optimizing encode & Merging audio ")
        call(["ffmpeg", "-i", "temp/video.mov", "-i", "temp/audio.mp3", "-codec", "copy",
              "data/enc-" + b4 + ".mov", "-y"], b6 = open(os.devnull, "w"), stderr=STDOUT)
        print("(!) Success , output : enc-" + b4 + ".mov")
    elif b3 = = "b":
        call(["clear"])
        print(b2.renderText("Decrypt"))
        print("----------------------------------------")
        b4 = input("(1) Encrypted video file name in the data folder  ? : ")
        try:
            b5 = int(input("(2) Caesar cipher shift value  ? : "))
        except ValueError:
            print("-----------------------")
            print("(!) Shift value is not an integer ")
            exit()
        try:
            open("data/" + b4)
        except IOError:
            print("-----------------------")
            print("(!) File not found ")
            exit()
        print("-----------------------")
        print("(-) Extracting Frame(s)")
        frame_extract(b4)
        print("(-) Decrypting Frame(s)")
        decode_frame("temp", b5)
        print("(-) Writing to recovered-text.txt")
        print("(!) Success")
    else:
        exit()