import pyAesCrypt
import os
import PySimpleGUI as sg
BUFFER_SIZE = 64 * 1024
def encrypt_file(file_path, password):
    try:
        output_file = file_path + ".ltt"
        pyAesCrypt.encryptFile(file_path, output_file, password, BUFFER_SIZE)
        print(f"{file_path} has been encrypted")
        try:
            os.remove(file_path)
        except PermissionError:
            print(f"{file_path} is currently in use and cannot be removed")
    except FileNotFoundError:
        print(f"{file_path} does not exist")
def decrypt_file(file_path, password):
    if file_path.endswith('.ltt'):
        original_file = file_path[:-4]
        try:
            pyAesCrypt.decryptFile(file_path, original_file, password, BUFFER_SIZE)
            print(f"{file_path} has been decrypted")
        except OSError:
            print(f"Error decrypting {file_path}")
        try:
            os.remove(file_path)
        except FileNotFoundError:
            print(f"{file_path} was not found")
def main():
    sg.theme('BluePurple')
    layout = [
        [sg.Text('Click on the action you wish to perform')],
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
        elif event == 'Encrypt':
            file_path = values["chosen_file"]
            if file_path:
                password = sg.popup_get_text('Enter password', password_char='*')
                if password:
                    encrypt_file(file_path, password)
                    window['OUTPUT'].update("File Encrypted")
                else:
                    window['OUTPUT'].update("No password provided")
            else:
                window['OUTPUT'].update("No file supplied")
        elif event == 'Decrypt':
            file_path = values["chosen_file"]
            if file_path:
                password = sg.popup_get_text('Enter password', password_char='*')
                if password:
                    decrypt_file(file_path, password)
                    window['OUTPUT'].update("File Decrypted")
                else:
                    window['OUTPUT'].update("No password provided")
            else:
                window['OUTPUT'].update("No file supplied")
    window.close()
if __name__ == "__main__":
    main()