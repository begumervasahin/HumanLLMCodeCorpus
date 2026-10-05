import os
import PySimpleGUI as sg
import pyAesCrypt
BUFFER_SIZE = 64 * 1024
PASSWORD = "your_password_here"
def encrypt_file(file_path):
    try:
        output_file_path = file_path + ".ltt"
        pyAesCrypt.encryptFile(file_path, output_file_path, PASSWORD, BUFFER_SIZE)
        print(f"File encrypted: {file_path}")
        try:
            os.remove(file_path)
        except PermissionError:
            print(f"Cannot remove {file_path}: File is in use")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
def decrypt_file(file_path):
    if file_path.endswith('ltt'):
        original_file_path = file_path[:-4]
        try:
            pyAesCrypt.decryptFile(file_path, original_file_path, PASSWORD, BUFFER_SIZE)
            print(f"File decrypted: {file_path}")
        except OSError:
            pass
        try:
            os.remove(file_path)
        except FileNotFoundError:
            print(f"File not found: {file_path}")
sg.change_look_and_feel('BluePurple')
layout = [
    [sg.Text('Click on Action you wish to perform')],
    [sg.Text('File path/name', size=(18, 1)), sg.Input(key="chosen_file"), sg.FileBrowse()],
    [sg.Text(size=(15, 1), key='OUTPUT')],
    [sg.Button('Encrypt'), sg.Button('Decrypt')],
    [sg.Button('Exit')]
]
window = sg.Window('LUTTA Enc/Decryptor', layout)
while True:
    event, values = window.read()
    if event in (None, 'Exit'):
        break
    if event == 'Encrypt':
        file_path = values["chosen_file"]
        if file_path:
            encrypt_file(file_path)
            window['OUTPUT'].update("File Encrypted")
        else:
            window['OUTPUT'].update("No file supplied")
    if event == 'Decrypt':
        file_path = values["chosen_file"]
        if file_path:
            decrypt_file(file_path)
            window['OUTPUT'].update("File Decrypted")
        else:
            window['OUTPUT'].update("No file supplied")
window.close()