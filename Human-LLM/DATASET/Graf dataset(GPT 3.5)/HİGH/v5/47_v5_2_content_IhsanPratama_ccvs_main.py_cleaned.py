import pyfiglet
from functions import *
from subprocess import call, STDOUT
import os
def fonk1():
    call(["clear"])
def fonk2():
    fonk1()
    print(b5.renderText("Encrypt"))
    print("----------------------------------------")
    b1 = input("(1) Video file name in the data folder? : ")
    try:
        b2 = int(input("(2) Caesar cipher shift value? : "))
    except ValueError:
        print("-----------------------")
        print("(!) Shift value is not an integer ")
        exit()
    try:
        open("data/" + b1)
    except IOError:
        print("-----------------------")
        print("(!) File not found ")
        exit()
    print("-----------------------")
    print("(-) Extracting Frame(s)")
    frame_extract(b1)
    print("(-) Extracting audio")
    call(["ffmpeg", "-i", f"data/{b1}", "-q:a", "0", "-map", "a", "temp/audio.mp3", "-y"],
         b3 = open(os.devnull, "w"), stderr=STDOUT)
    print("(-) Reading text-to-hide.txt")
    print("(-) Encrypting & appending string into frame(s) ")
    encode_frame("temp", "data/text-to-hide.txt", b2)
    print("(-) Merging frame(s) ")
    call(["ffmpeg", "-i", "temp/%d.png", "-vcodec", "png", "temp/video.mov", "-y"],
         b3 = open(os.devnull, "w"), stderr=STDOUT)
    print("(-) Optimizing encode & Merging audio ")
    call(["ffmpeg", "-i", "temp/video.mov", "-i", "temp/audio.mp3", "-codec", "copy",
          f"data/enc-{b1}.mov", "-y"], b3 = open(os.devnull, "w"), stderr=STDOUT)
    print("(!) Success, output: enc-" + b1 + ".mov")
def fonk3():
    fonk1()
    print(b5.renderText("Decrypt"))
    print("----------------------------------------")
    b1 = input("(1) Encrypted video file name in the data folder? : ")
    try:
        b2 = int(input("(2) Caesar cipher shift value? : "))
    except ValueError:
        print("-----------------------")
        print("(!) Shift value is not an integer ")
        exit()
    try:
        open(f"data/{b1}")
    except IOError:
        print("-----------------------")
        print("(!) File not found ")
        exit()
    print("-----------------------")
    print("(-) Extracting Frame(s)")
    frame_extract(b1)
    print("(-) Decrypting Frame(s)")
    decode_frame("temp", b2)
    print("(-) Writing to recovered-text.txt")
    print("(!) Success")
if b4 = = '__main__':
    b5 = pyfiglet.Figlet(font='slant')
    print(b5.renderText("CCVS KI UAS"))
    print("CaesarCipherVideoSteganography")
    print("")
    print("Menu :")
    print("")
    print("(a) Encrypt & Merge into Video")
    print("(b) Decrypt & Get the plain text")
    print("-----------------------")
    b6 = input("(!) Choose option : ")
    if b6 = = "a":
        fonk2()
    elif b6 = = "b":
        fonk3()
    else:
        exit()