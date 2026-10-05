import os
import pyAesCrypt
import PySimpleGUI as sg
b1 = 64 * 1024
b2 = "your_password_here"
def fonk1(file_path):
    try:
        b3 = file_path + ".ltt"
        pyAesCrypt.encryptFile(file_path, b3, b2, b1)
        print(f"File '{file_path}' has been encrypted")
        try:
            os.remove(file_path)
        except PermissionError:
            print(f"Unable to remove '{file_path}' because it is in use")
    except FileNotFoundError:
        print(f"File '{file_path}' does not exist")
def fonk2(file_path):
    if file_path.endswith('.ltt'):
        b4 = file_path[:-4]
        print(f"Decrypting '{file_path}' to '{b4}'")
        try:
            pyAesCrypt.decryptFile(file_path, b4, b2, b1)
            print(f"File '{file_path}' has been decrypted")
        except OSError:
            pass
        try:
            os.remove(file_path)
        except FileNotFoundError:
            print(f"Encrypted file '{file_path}' not found")
sg.change_look_and_feel('BluePurple')
b5 = [
    [sg.Text('Click on the action you wish to perform')],
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
            b7['OUTPUT'].update("File encrypted successfully")
        else:
            b7['OUTPUT'].update("No file selected")
    if b9 = = 'Decrypt':
        b10 = b8["chosen_file"]
        if b10:
            fonk2(b10)
            b7['OUTPUT'].update("File decrypted successfully")
        else:
            b7['OUTPUT'].update("No file selected")
b7.close()