import os
import glob
from PIL import Image
import pytesseract
from gtts import gTTS
import pygame
from pygame import mixer
import PySimpleGUI as sg
import fitz
def get_text(value):
    string = value.strip()
    if "-" in string:
        first_page_number, last_page_number = map(int, string.split("-"))
    else:
        first_page_number = int(string)
        last_page_number = 0
    return first_page_number, last_page_number
def main():
    current_directory = os.getcwd()
    final_directory = os.path.join(current_directory, 'Text_to_speech_software')
    if not os.path.exists(final_directory):
        os.makedirs(final_directory)
    layout = [
        [sg.Text('Choose PDF File to read'), sg.Input(), sg.FileBrowse()],
        [sg.Text('Enter PDF Page number or range separated by - '), sg.InputText()],
        [sg.Button('Ok'), sg.Button('Cancel')]
    ]
    window = sg.Window('Input', layout)
    while True:
        event, values = window.read()
        if event in (None, 'Cancel'):
            print("Exiting")
            window.close()
            exit()
        if event == "Ok":
            if not values[0] or not values[1]:
                sg.Popup("Missing Input", "Please enter both PDF file and page number(s)")
            else:
                if not values[1].replace("-", "").isdigit():
                    sg.Popup("Invalid Input", "Enter valid page number(s) or range")
                else:
                    first_page_number, last_page_number = get_text(values[1])
                    break
    window.close()
    pdf_to_read = values[0]
    image_directory = glob.glob(final_directory)
    for file in os.listdir(final_directory):
        filepath = os.path.join(final_directory, file)
        os.chmod(filepath, 0o777)
        os.remove(filepath)
    doc = fitz.open(pdf_to_read)
    k = 1
    if last_page_number == 0:
        page = doc.loadPage(first_page_number - 1)
        zoom_x = 2.0
        zoom_y = 2.0
        mat = fitz.Matrix(zoom_x, zoom_y)
        pix = page.getPixmap(matrix=mat)
        output = os.path.join(final_directory, "image_to_read.png")
        pix.writePNG(output)
    else:
        for i in range(first_page_number - 1, last_page_number):
            page = doc.loadPage(i)
            zoom_x = 2.0
            zoom_y = 2.0
            mat = fitz.Matrix(zoom_x, zoom_y)
            pix = page.getPixmap(matrix=mat)
            output = os.path.join(final_directory, f"image_{k}_to_read.png")
            pix.writePNG(output)
            k += 1
    mytext = []
    for file in os.listdir(final_directory):
        data = pytesseract.image_to_string(Image.open(os.path.join(final_directory, file)), lang="eng")
        data = data.replace("|", "I")
        data = data.split('\n')
        mytext.append(data)
    language = 'en'
    newtext = ""
    for text in mytext:
        for line in text:
            line = line.strip()
            if len(line.split(" ")) < 10 and len(line.split(" ")) > 0:
                newtext += " " + str(line) + "\n"
            elif len(line.split(" ")) < 2:
                pass
            else:
                if line[-1] != ".":
                    newtext += " " + str(line)
                else:
                    newtext += " " + line + "\n"
    myobj = gTTS(text=newtext, lang=language, slow=False)
    myobj.save(os.path.join(final_directory, "pdf_audio.mp3"))
    pygame.init()
    mixer.init()
    mixer.music.load(os.path.join(final_directory, "pdf_audio.mp3"))
    mixer.music.play()
    pygame.event.wait()
if __name__ == '__main__':
    main()