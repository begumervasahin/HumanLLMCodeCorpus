import os
import glob
from PIL import Image
import pytesseract
from gtts import gTTS
import pygame
from pygame import mixer
import PySimpleGUI as sg
import fitz
def fonk1(value):
    b1 = value.strip()
    if "-" in b1:
        b3, b2 = map(int, b1.split("-"))
    else:
        b3 = int(b1)
        b2 = 0
    return b3, b2
def fonk2():
    b4 = os.getcwd()
    b5 = os.path.join(b4, 'Text_to_speech_software')
    if not os.path.exists(b5):
        os.makedirs(b5)
    b6 = [
        [sg.Text('Choose PDF File to read'), sg.Input(), sg.FileBrowse()],
        [sg.Text('Enter PDF Page number or range separated by - '), sg.InputText()],
        [sg.Button('Ok'), sg.Button('Cancel')]
    ]
    b7 = sg.Window('Input', b6)
    while True:
        b9, b8 = b7.read()
        if b9 in (None, 'Cancel'):
            print("Exiting")
            b7.close()
            exit()
        if b9 = = "Ok":
            if not b8[0] or not b8[1]:
                sg.Popup("Missing Input", "Please enter both PDF file and b14 number(s)")
            else:
                if not b8[1].replace("-", "").isdigit():
                    sg.Popup("Invalid Input", "Enter valid b14 number(s) or range")
                else:
                    b3, b2 = fonk1(b8[1])
                    break
    b7.close()
    b10 = b8[0]
    b11 = glob.glob(b5)
    for file in os.listdir(b5):
        b12 = os.path.join(b5, file)
        os.chmod(b12, 0o777)
        os.remove(b12)
    b13 = fitz.open(b10)
    a1 = 1
    if b2 = = 0:
        b14 = b13.loadPage(b3 - 1)
        a2 = 2.0
        a3 = 2.0
        b15 = fitz.Matrix(a2, a3)
        b16 = b14.getPixmap(matrix=b15)
        b17 = os.path.join(b5, "image_to_read.png")
        b16.writePNG(b17)
    else:
        for i in range(b3 - 1, b2):
            b14 = b13.loadPage(i)
            a2 = 2.0
            a3 = 2.0
            b15 = fitz.Matrix(a2, a3)
            b16 = b14.getPixmap(matrix=b15)
            b17 = os.path.join(b5, f"image_{a1}_to_read.png")
            b16.writePNG(b17)
            a1 += 1
    b18 = []
    for file in os.listdir(b5):
        b19 = pytesseract.image_to_string(Image.open(os.path.join(b5, file)), lang="eng")
        b19 = b19.replace("|", "I")
        b19 = b19.split('\n')
        b18.append(b19)
    b20 = 'en'
    b21 = ""
    for text in b18:
        for b22 in text:
            b22 = b22.strip()
            if len(b22.split(" ")) < 10 and len(b22.split(" ")) > 0:
                b21 += " " + str(b22) + "\n"
            elif len(b22.split(" ")) < 2:
                pass
            else:
                if b22[-1] != ".":
                    b21 += " " + str(b22)
                else:
                    b21 += " " + b22 + "\n"
    b23 = gTTS(text=b21, lang=b20, slow=False)
    b23.save(os.path.join(b5, "pdf_audio.mp3"))
    pygame.init()
    mixer.init()
    mixer.music.load(os.path.join(b5, "pdf_audio.mp3"))
    mixer.music.play()
    pygame.b9.wait()
if b24 = = '__main__':
    fonk2()