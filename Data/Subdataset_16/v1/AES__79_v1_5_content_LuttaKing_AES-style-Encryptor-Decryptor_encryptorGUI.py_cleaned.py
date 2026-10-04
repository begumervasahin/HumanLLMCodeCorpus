import pyAesCrypt
import os
import PySimpleGUI as sg
b1 = 64 * 1024
def fonk1(file, b9):
    try:
        pyAesCrypt.encryptFile(file, file + ".ltt", b9, b1)
        print(f"{file} has been encrypted")
        try:
            os.remove(file)
        except PermissionError:
            print(f"{file} is currently in use and cannot be removed")
    except FileNotFoundError:
        print(f"{file} does not exist")
def fonk2(file, b9):
    if file.endswith('.ltt'):
        b2 = file[:-4]
        try:
            pyAesCrypt.decryptFile(file, b2, b9, b1)
            print(f"{file} has been decrypted")
        except OSError:
            pass
        try:
            os.remove(file)
        except FileNotFoundError:
            print(f"{file} was not found")
sg.change_look_and_feel('BluePurple')
b3 = [
    [sg.Text('Click on the action you wish to perform')],
    [sg.Text('File path/name', b4 = (18, 1)), sg.Input(key="chosen_file"), sg.FileBrowse()],
    [sg.Text(b4 = (15, 1), key='OUTPUT')],
    [sg.Button('Encrypt'), sg.Button('Decrypt')],
    [sg.Button('Exit')]
]
b5 = sg.Window('LUTTA Enc/Decryptor', b3)
while True:
    b7, b6 = b5.read()
    print(b7, b6)
    if b7 in (None, 'Exit'):
        break
    if b7 = = 'Encrypt':
        b8 = b6["chosen_file"]
        if b8:
            b9 = sg.popup_get_text('Enter b9', password_char='*')
            if b9:
                fonk1(b8, b9)
                b5['OUTPUT'].update("File Encrypted")
            else:
                b5['OUTPUT'].update("No b9 provided")
        else:
            b5['OUTPUT'].update("No file supplied")
    if b7 = = 'Decrypt':
        b8 = b6["chosen_file"]
        if b8:
            b9 = sg.popup_get_text('Enter b9', password_char='*')
            if b9:
                fonk2(b8, b9)
                b5['OUTPUT'].update("File Decrypted")
            else:
                b5['OUTPUT'].update("No b9 provided")
        else:
            b5['OUTPUT'].update("No file supplied")
b5.close()