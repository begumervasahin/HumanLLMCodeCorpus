from gtts import gTTS
import pygame
from pygame import mixer
from PIL import Image
import pytesseract
import os
import glob
import PySimpleGUI as sg
import tkinter as tk
import fitz
def fonk1(value):
    b1 = value
    b1 = b1.strip()
    if "-" in b1:
        b2 = int(b1.split("-")[0])
        b3 = int(b1.split("-")[1])
    else:
        b2 = int(b1)
        b3 = 0
    return b2,b3
def fonk2():
    global e,b2,b3
    b4 = os.getcwd()
    b5 = os.path.join(b4,r'Text_to_speech_software')
    if not os.path.exists(b5):
        os.makedirs(b5)
    print(b4)
    print(b5)
    b6 = [  [sg.Text('Choose PDF File to read'),sg.Input(),sg.FileBrowse()],
                [sg.Text('Enter PDF Page number or range separated by - '), sg.InputText()],
                [sg.Button('Ok'), sg.Button('Cancel')]
            ]
    b7 = sg.Window('Input', b6)
    b8 = False
    while True:
        b11, b9 = b7.read()
        b10 = b9[0]
        if b11 in (None, 'Cancel'):
            print("Exitting")
            b7.close()
            exit()
        if b11 = = "Ok":
            if b9[0] == "":
                sg.Popup("Enter value", "Enter PDF file to be transcribed ")
            if b9[1] == "":
                sg.Popup("Enter value", "Enter b15 number(s) to be transcribed")
            if b9[0]!="" and b9[1]!="":
                for char in b9[1]:
                    if char.isdigit()==False:
                        sg.Popup("Invalid value","Enter b8 number or numbers separated by -")
                        break
                    else:
                        b8 = True
                        break
        if b8 = =True:
            print('You entered ', b9[1])
            break
    b7.close()
    b2,b3 = fonk1(b9[1])
    b12 = glob.glob(b5)
    for file in os.listdir(b5):
        b13 = os.path.join(b5,file)
        print(b13)
        os.chmod(b13, 0o777)
        os.remove(b13)
    b14 = fitz.open(b10)
    a1 = 1
    if b3 = = 0:
        b15 = b14.loadPage(b2-1)
        a2 = 2.0
        a3 = 2.0
        b16 = fitz.Matrix(a2,a3)
        b17 = b15.getPixmap(matrix=b16)
        b18 = os.path.join(b5, r"image_to_read.png")
        b17.writePNG(b18)
    else:
        for i in range(b2-1,b3):
            b15 = b14.loadPage(i)
            a2 = 2.0
            a3 = 2.0
            b16 = fitz.Matrix(a2,a3)
            b17 = b15.getPixmap(matrix=b16)
            b18 = os.path.join(b5, r"image_"+str(a1)+"_to_read.png")
            b17.writePNG(b18)
            a1+=1
    print("Done")
    b19 = []
    for file in os.listdir(b5):
        b20 = pytesseract.image_to_string(Image.open(os.path.join(b5,file)),lang="eng")
        b20 = b20.replace("|","I")
        b20 = b20.split('\n')
        b19.append(b20)
    b21 = 'en'
    print(b19)
    b22 = ""
    for text in b19:
        for b23 in text:
            b23 = b23.strip()
            if len(b23.split(" ")) < 10 and len(b23.split(" "))>0:
                b22 = b22 + " " + str(b23) + "\n"
            elif len(b23.split(" "))<2:
                pass
            else:
                if b23[-1]!=".":
                    b22 = b22 + " " + str(b23)
                else:
                    b22 = b22 + " " + b23 + "\n"
    print(b22)
    b24 = gTTS(text=b22, lang=b21, slow=False)
    b24.save(os.path.join(b5,"pdf_audio.mp3"))
    pygame.init()
    mixer.init()
    mixer.music.load(os.path.join(b5,"pdf_audio.mp3"))
    mixer.music.play()
    pygame.b11.wait()
if b25 = = '__main__':
    fonk2()