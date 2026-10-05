import os
import PySimpleGUI as sg
import pyAesCrypt
b1 = 64 * 1024
b2 = "your_password_here"
def fonk1(file):
    try:
        pyAesCrypt.encryptFile(file, file + ".ltt", b2, b1)
        print(file + " has been encrypted")
        try:
            os.remove(file)
        except PermissionError:
            print(file + ' is in use')
    except FileNotFoundError:
        print(file + " does not exist")
def fonk2(f):
    if f.endswith('ltt'):
        b3 = len(f) - 4
        b4 = f[:b3]
        print(b4)
        try:
            pyAesCrypt.decryptFile(f, b4, b2, b1)
            print(f + " has been decrypted")
        except OSError:
            pass
        try:
            os.remove(f)
        except FileNotFoundError:
            print(f + ' not found')
sg.change_look_and_feel('BluePurple')
b5 = [[sg.Text('Click on Action you wish to perform')],
          [sg.Text('File path/name', b6 = (18, 1)), sg.Input(key="chosen_file"), sg.FileBrowse()],
          [sg.Text(b6 = (15, 1), key='OUTPUT')],
          [sg.Button('Encrypt'), sg.Button('Decrypt')],
          [sg.Button('Exit')]]
b7 = sg.Window('LUTTA Enc/Decryptor', b5)
while True:
    b9, b8 = b7.read()
    print(b9, b8)
    if b9 in (None, 'Exit'):
        break
    if b9 = = 'Encrypt':
        b10 = b8["chosen_file"]
        if b10:
            fonk1(b10)
            b7['OUTPUT'].update("File Encrypted")
        else:
            b7['OUTPUT'].update("No file supplied")
    if b9 = = 'Decrypt':
        b10 = b8["chosen_file"]
        if b10:
            fonk2(b10)
            b7['OUTPUT'].update("File Decrypted")
        else:
            b7['OUTPUT'].update("No file supplied")
b7.close()