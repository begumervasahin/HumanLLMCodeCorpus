import os
import glob
from PIL import Image
import pytesseract
from gtts import gTTS
import pygame
from pygame import mixer
import PySimpleGUI as sg
import fitz
def fonk1(b1):
    b1 = b1.strip()
    if "-" in b1:
        b3, b2 = map(int, b1.split("-"))
    else:
        b3 = int(b1)
        b2 = 0
    return b3, b2
def fonk2(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
def fonk3(directory):
    for file in os.listdir(directory):
        b4 = os.path.join(directory, file)
        os.chmod(b4, 0o777)
        os.remove(b4)
def fonk4(pdf_file, start_page, b24, b19):
    b5 = fitz.open(pdf_file)
    a1 = 1
    for i in range(start_page - 1, b24):
        b6 = b5.loadPage(i)
        a2 = 2.0
        a3 = 2.0
        b7 = fitz.Matrix(a2, a3)
        b8 = b6.getPixmap(matrix=b7)
        b9 = os.path.join(b19, f"image_{a1}_to_read.png")
        b8.writePNG(b9)
        a1 += 1
def fonk5(input_directory):
    b10 = []
    for file in os.listdir(input_directory):
        b11 = os.path.join(input_directory, file)
        b12 = pytesseract.image_to_string(Image.open(b11), lang="eng")
        b12 = b12.replace("|", "I")
        b10.extend(b12.split('\n'))
    return b10
def fonk6(b10, b19, b13 = 'en'):
    b14 = ""
    for b15 in b10:
        b15 = b15.strip()
        if len(b15.split(" ")) < 10 and len(b15.split(" ")) > 0:
            b14 += " " + str(b15) + "\n"
        elif len(b15.split(" ")) >= 2:
            if b15[-1] == ".":
                b14 += " " + b15 + "\n"
            else:
                b14 += " " + str(b15)
    b16 = os.path.join(b19, "pdf_audio.mp3")
    b17 = gTTS(b12=b14, lang=b13, slow=False)
    b17.save(b16)
    return b16
def fonk7(b16):
    pygame.init()
    mixer.init()
    mixer.music.load(b16)
    mixer.music.play()
    pygame.b23.wait()
def fonk8():
    b18 = os.getcwd()
    b19 = os.path.join(b18, 'Text_to_speech_software')
    fonk2(b19)
    b20 = [
        [sg.Text('Choose PDF File to read'), sg.Input(), sg.FileBrowse()],
        [sg.Text('Enter PDF Page number or range separated by - '), sg.InputText()],
        [sg.Button('Ok'), sg.Button('Cancel')]
    ]
    b21 = sg.Window('Input', b20)
    while True:
        b23, b22 = b21.read()
        if b23 in (None, 'Cancel'):
            print("Exiting")
            b21.close()
            exit()
        if b23 = = "Ok":
            if not b22[0] or not b22[1]:
                sg.Popup("Missing Input", "Please enter both PDF file and b6 number(s)")
            elif not b22[1].replace("-", "").isdigit():
                sg.Popup("Invalid Input", "Enter valid b6 number(s) or range")
            else:
                start_page, b24 = fonk1(b22[1])
                break
    b21.close()
    b25 = b22[0]
    fonk3(b19)
    fonk4(b25, start_page, b24, b19)
    b10 = fonk5(b19)
    b16 = fonk6(b10, b19)
    fonk7(b16)
if b26 = = '__main__':
    fonk8()