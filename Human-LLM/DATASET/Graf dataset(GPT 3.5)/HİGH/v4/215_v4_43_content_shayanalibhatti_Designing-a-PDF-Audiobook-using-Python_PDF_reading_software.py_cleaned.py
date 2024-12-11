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
def fonk2(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
def fonk3(directory_path):
    for file_name in os.listdir(directory_path):
        b4 = os.path.join(directory_path, file_name)
        os.chmod(b4, 0o777)
        os.remove(b4)
def fonk4(pdf_path, b3, b2, output_dir):
    b5 = fitz.open(pdf_path)
    a1 = 1
    for page_number in range(b3 - 1, b2):
        b6 = b5.loadPage(page_number)
        a2 = 2.0
        a3 = 2.0
        b7 = fitz.Matrix(a2, a3)
        b8 = b6.getPixmap(b7=b7)
        b9 = os.path.join(output_dir, f"image_{a1}_to_read.png")
        b8.writePNG(b9)
        a1 += 1
def fonk5(input_dir):
    b10 = []
    for file_name in os.listdir(input_dir):
        b11 = os.path.join(input_dir, file_name)
        b12 = pytesseract.image_to_string(Image.open(b11), lang="eng")
        b12 = b12.replace("|", "I")
        b10.extend(b12.split('\n'))
    return b10
def fonk6(b10, output_dir, b13 = 'en'):
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
    b16 = os.path.join(output_dir, "pdf_audio.mp3")
    b17 = gTTS(b12=b14, lang=b13, slow=False)
    b17.save(b16)
    return b16
def fonk7(b25):
    pygame.init()
    mixer.init()
    mixer.music.load(b25)
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
                b3, b2 = fonk1(b22[1])
                break
    b21.close()
    b24 = b22[0]
    fonk3(b19)
    fonk4(b24, b3, b2, b19)
    b10 = fonk5(b19)
    b25 = fonk6(b10, b19)
    fonk7(b25)
if b26 = = '__main__':
    fonk8()