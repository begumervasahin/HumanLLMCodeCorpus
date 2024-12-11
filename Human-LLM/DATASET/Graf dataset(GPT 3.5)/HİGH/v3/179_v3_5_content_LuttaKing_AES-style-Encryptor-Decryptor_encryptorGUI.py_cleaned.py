import os
import PySimpleGUI as sg
import pyAesCrypt
b1 = 64 * 1024
b2 = "your_password_here"
def fonk1(b10):
    try:
        b3 = b10 + ".ltt"
        pyAesCrypt.encryptFile(b10, b3, b2, b1)
        print(f"File encrypted: {b10}")
        try:
            os.remove(b10)
        except PermissionError:
            print(f"Cannot remove {b10}: File is in use")
    except FileNotFoundError:
        print(f"File not found: {b10}")
def fonk2(b10):
    if b10.endswith('ltt'):
        b4 = b10[:-4]
        try:
            pyAesCrypt.decryptFile(b10, b4, b2, b1)
            print(f"File decrypted: {b10}")
        except OSError:
            pass
        try:
            os.remove(b10)
        except FileNotFoundError:
            print(f"File not found: {b10}")
sg.change_look_and_feel('BluePurple')
b5 = [
    [sg.Text('Click on Action you wish to perform')],
    [sg.Text('File path/name', b6 = (18, 1)), sg.Input(key="chosen_file"), sg.FileBrowse()],
    [sg.Text(b6 = (15, 1), key='OUTPUT')],
    [sg.Button('Encrypt'), sg.Button('Decrypt')],
    [sg.Button('Exit')]
]
b7 = sg.Window('LUTTA Enc/Decryptor', b5)
while True:
    b9, b8 = b7.read()
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