import os
import PySimpleGUI as sg
import pyAesCrypt
buffer_size = 64 * 1024
password = "your_password_here"
def encrypt_file(file):
    try:
        pyAesCrypt.encryptFile(file, file + ".ltt", password, buffer_size)
        print(file + " has been encrypted")
        try:
            os.remove(file)
        except PermissionError:
            print(file + ' is in use')
    except FileNotFoundError:
        print(file + " does not exist")
def decrypt_file(f):
    if f.endswith('ltt'):
        num = len(f) - 4
        orig_file = f[:num]
        print(orig_file)
        try:
            pyAesCrypt.decryptFile(f, orig_file, password, buffer_size)
            print(f + " has been decrypted")
        except OSError:
            pass
        try:
            os.remove(f)
        except FileNotFoundError:
            print(f + ' not found')
sg.change_look_and_feel('BluePurple')
layout = [[sg.Text('Click on Action you wish to perform')],
          [sg.Text('File path/name', size=(18, 1)), sg.Input(key="chosen_file"), sg.FileBrowse()],
          [sg.Text(size=(15, 1), key='OUTPUT')],
          [sg.Button('Encrypt'), sg.Button('Decrypt')],
          [sg.Button('Exit')]]
window = sg.Window('LUTTA Enc/Decryptor', layout)
while True:
    event, values = window.read()
    print(event, values)
    if event in (None, 'Exit'):
        break
    if event == 'Encrypt':
        fname = values["chosen_file"]
        if fname:
            encrypt_file(fname)
            window['OUTPUT'].update("File Encrypted")
        else:
            window['OUTPUT'].update("No file supplied")
    if event == 'Decrypt':
        fname = values["chosen_file"]
        if fname:
            decrypt_file(fname)
            window['OUTPUT'].update("File Decrypted")
        else:
            window['OUTPUT'].update("No file supplied")
window.close()