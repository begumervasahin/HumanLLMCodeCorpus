import pyAesCrypt,os
import PySimpleGUI as sg
ffsdbffr=64*1024
def ecrpt(file):
    try:
        pyAesCrypt.encryptFile(file,file + ".ltt", pswd, bffr)
        print(file+" has been been encrypted")
        try:
            os.remove(file)
        except PermissionError:
            print(file + ' is running ')
    except :
        print(file+" does not exist")
def dcrpt(f):
     if f.endswith('ltt'):
                num=len(f)-4
                lis=[]
                for i in range(num):
                    lis.append(f[i])
                orig_file="".join(lis)
                print(orig_file)
                try:
                     pyAesCrypt.decryptFile(f,orig_file, pswd, bffr)
                     print(f+" has been released")
                except OSError :
                          pass
                try:
                        os.remove(f)
                except FileNotFoundError:
                        print(f + ' NOT foUND')
sg.change_look_and_feel('BluePurple')
layout = [[sg.Text('Click on Action you wish to perform')],
         [sg.Text('File path/name', size=(18, 1)), sg.Input(key="chosen_file"), sg.FileBrowse()],
          [sg.Text( size=(15, 1),key='OUTPUT')],
          [sg.Button('Encrypt'), sg.Button('Decrypt')],
          [sg.Button('Exit')]]
window = sg.Window('LUTTA Enc/Decryptor', layout)
while True:
    event, values = window.read()
    print(event, values)
    if event in  (None, 'Exit'):
        break
    if event == 'Encrypt':
        fname = values["chosen_file"]
        if fname:
            ecrpt(fname)
            window['OUTPUT'].update("File Encrypt")
        else:
            window['OUTPUT'].update("No file Supplied")
    if event == 'Decrypt':
        fname = values["chosen_file"]
        if fname:
            dcrpt(fname)
            window['OUTPUT'].update("File Decrypted")
        else:
            window['OUTPUT'].update("No file Supplied")
window.close()