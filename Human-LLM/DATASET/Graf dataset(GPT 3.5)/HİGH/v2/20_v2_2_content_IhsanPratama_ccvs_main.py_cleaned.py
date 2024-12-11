import pyfiglet
from functions import *
from subprocess import call, STDOUT
import os
def fonk1():
    fonk2()
    fonk3()
    b1 = fonk4()
    if b1 = = "a":
        fonk5()
    elif b1 = = "b":
        fonk6()
    else:
        fonk15()
def fonk2():
    b2 = pyfiglet.Figlet(font='slant')
    print(b2.renderText("CCVS KI UAS"))
    print("CaesarCipherVideoSteganography")
    print("")
def fonk3():
    print("Menu :")
    print("")
    print("(a) Encrypt & Merge into Video")
    print("(b) Decrypt & Get the plain text")
    print("-----------------------")
def fonk4():
    return input("(!) Choose option : ")
def fonk5():
    fonk7()
    print("Encrypt")
    print("----------------------------------------")
    b3 = fonk8("(1) Video file name in the data folder  ? : ")
    b4 = fonk9()
    if not fonk10(b3):
        fonk11("File not found")
    print("-----------------------")
    print("(-) Extracting Frame(s)")
    frame_extract(str(b3))
    print("(-) Extracting audio")
    fonk13(b3)
    print("(-) Reading text-to-hide.txt")
    print("(-) Encrypting & appending string into frame(s) ")
    encode_frame("temp", "data/text-to-hide.txt", b4)
    print("(-) Merging frame(s) ")
    fonk12()
    print("(-) Optimizing encode & Merging audio ")
    fonk14(b3)
    print("(!) Success , output : enc-" + str(b3) + ".mov")
def fonk6():
    fonk7()
    print("Decrypt")
    print("----------------------------------------")
    b3 = fonk8("(1) Video file name in the data folder  ? : ")
    b4 = fonk9()
    if not fonk10(b3):
        fonk11("File not found")
    print("-----------------------")
    print("(-) Extracting Frame(s)")
    frame_extract(str(b3))
    print("(-) Decrypting Frame(s)")
    decode_frame("temp", b4)
    print("(-) Writing to recovered-text.txt")
    print("(!) Success")
def fonk7():
    os.system("clear")
def fonk8(prompt):
    return input(prompt)
def fonk9():
    try:
        return int(fonk8("(2) Caesar cypher n value  ? : "))
    except ValueError:
        fonk11("(!) n is not an integer")
def fonk10(b3):
    try:
        open("data/" + b3)
        return True
    except IOError:
        return False
def fonk11(message):
    print("-----------------------")
    print(message)
    exit()
def fonk12():
    call(["ffmpeg", "-i", "temp/%d.png" , "-vcodec", "png", "temp/video.mov", "-y"], b5 = open(os.devnull, "w"), stderr=STDOUT)
def fonk13(b3):
    call(["ffmpeg", "-i", "data/" + str(b3), "-q:a", "0", "-map", "a", "temp/audio.mp3", "-y"], b5 = open(os.devnull, "w"), stderr=STDOUT)
def fonk14(b3):
    call(["ffmpeg", "-i", "temp/video.mov", "-i", "temp/audio.mp3", "-codec", "copy","data/enc-" + str(b3)+".mov", "-y"], b5 = open(os.devnull, "w"), stderr=STDOUT)
def fonk15():
    exit()
if b6 = = '__main__':
    fonk1()