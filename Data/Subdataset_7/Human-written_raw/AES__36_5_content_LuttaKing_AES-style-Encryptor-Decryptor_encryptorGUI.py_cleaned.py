import pyAesCrypt,os
import PySimpleGUI as sg
b1 = 64*1024
def fonk1(file):
    try:
        pyAesCrypt.encryptFile(file,file + ".ltt", pswd, bffr)
        print(file+" has been been encrypted")
        try:
            os.remove(file)
        except PermissionError:
            print(file + ' is running ')
    except :
        print(file+" does not exist")
def fonk2(f):
     if f.endswith('ltt'):
                b2 = len(f)-4
                b3 = []
                for i in range(b2):
                    b3.append(f[i])
                b4 = "".join(b3)
                print(b4)
                try:
                     pyAesCrypt.decryptFile(f,b4, pswd, bffr)
                     print(f+" has been released")
                except OSError :
                          pass
                try:
                        os.remove(f)
                except FileNotFoundError:
                        print(f + ' NOT foUND')
sg.change_look_and_feel('BluePurple')
b5 = [[sg.Text('Click on Action you wish to perform')],
         [sg.Text('File path/name', b6 = (18, 1)), sg.Input(key="chosen_file"), sg.FileBrowse()],
          [sg.Text( b6 = (15, 1),key='OUTPUT')],
          [sg.Button('Encrypt'), sg.Button('Decrypt')],
          [sg.Button('Exit')]]
b7 = sg.Window('LUTTA Enc/Decryptor', b5)
while True:
    b9, b8 = b7.read()
    print(b9, b8)
    if b9 in  (None, 'Exit'):
        break
    if b9 = = 'Encrypt':
        b10 = b8["chosen_file"]
        if b10:
            fonk1(b10)
            b7['OUTPUT'].update("File Encrypt")
        else:
            b7['OUTPUT'].update("No file Supplied")
    if b9 = = 'Decrypt':
        b10 = b8["chosen_file"]
        if b10:
            fonk2(b10)
            b7['OUTPUT'].update("File Decrypted")
        else:
            b7['OUTPUT'].update("No file Supplied")
b7.close()