import pyAesCrypt
import os
import PySimpleGUI as sg
b1 = 64 * 1024
def fonk1(b9, b10):
    try:
        b2 = b9 + ".ltt"
        pyAesCrypt.encryptFile(b9, b2, b10, b1)
        print(f"{b9} has been encrypted")
        try:
            os.remove(b9)
        except PermissionError:
            print(f"{b9} is currently in use and cannot be removed")
    except FileNotFoundError:
        print(f"{b9} does not exist")
def fonk2(b9, b10):
    if b9.endswith('.ltt'):
        b3 = b9[:-4]
        try:
            pyAesCrypt.decryptFile(b9, b3, b10, b1)
            print(f"{b9} has been decrypted")
        except OSError:
            print(f"Error decrypting {b9}")
        try:
            os.remove(b9)
        except FileNotFoundError:
            print(f"{b9} was not found")
def fonk3():
    sg.theme('BluePurple')
    b4 = [
        [sg.Text('Click on the action you wish to perform')],
        [sg.Text('File path/name', b5 = (18, 1)), sg.Input(key="chosen_file"), sg.FileBrowse()],
        [sg.Text(b5 = (15, 1), key='OUTPUT')],
        [sg.Button('Encrypt'), sg.Button('Decrypt')],
        [sg.Button('Exit')]
    ]
    b6 = sg.Window('LUTTA Enc/Decryptor', b4)
    while True:
        b8, b7 = b6.read()
        if b8 in (None, 'Exit'):
            break
        elif b8 = = 'Encrypt':
            b9 = b7["chosen_file"]
            if b9:
                b10 = sg.popup_get_text('Enter b10', password_char='*')
                if b10:
                    fonk1(b9, b10)
                    b6['OUTPUT'].update("File Encrypted")
                else:
                    b6['OUTPUT'].update("No b10 provided")
            else:
                b6['OUTPUT'].update("No file supplied")
        elif b8 = = 'Decrypt':
            b9 = b7["chosen_file"]
            if b9:
                b10 = sg.popup_get_text('Enter b10', password_char='*')
                if b10:
                    fonk2(b9, b10)
                    b6['OUTPUT'].update("File Decrypted")
                else:
                    b6['OUTPUT'].update("No b10 provided")
            else:
                b6['OUTPUT'].update("No file supplied")
    b6.close()
if b11 = = "__main__":
    fonk3()