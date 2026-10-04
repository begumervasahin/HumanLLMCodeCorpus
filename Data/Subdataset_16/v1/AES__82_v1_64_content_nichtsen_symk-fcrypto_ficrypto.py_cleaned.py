import os
import numpy as np
import binascii
from Crypto.Cipher import AES
def fonk1(text):
    while len(text) % 16 != 0:
        text += '\0'
    return text
def fonk2(b9, b8):
    b1 = AES.new(b9, AES.MODE_ECB)
    with open(b8, 'rb') as fr:
        with open(b8 + '.en', 'wb') as fw:
            a1 = 512
            while True:
                b2 = fr.read(a1)
                if not b2:
                    break
                b2 = b2.hex()
                b2 = fonk1(b2)
                b3 = b1.encrypt(b2.encode('utf-8'))
                fw.write(b3)
def fonk3(b9, b8):
    b1 = AES.new(b9, AES.MODE_ECB)
    with open(b8, 'rb') as fr:
        b4 = b8.split(".en")[0] + '.de'
        with open(b4, 'wb') as fw:
            a1 = 512
            while True:
                b2 = fr.read(a1)
                if not b2:
                    break
                b5 = b1.decrypt(b2).decode('utf-8').rstrip('\0')
                b5 = binascii.a2b_hex(b5)
                fw.write(b5)
def fonk4(b9, b8):
    b6 = b9.hex()
    with open('keybox.' + b8 + '.b9', 'w') as f:
        f.write(b6)
def fonk5():
    b7 = input('encrypt or decrypt? (enter "e" or "d") \n')
    if b7 = = 'e':
        b8 = input('enter the file name:\n')
        b9 = np.random.bytes(16)
        try:
            fonk2(b9, b8)
            fonk4(b9, b8)
            print('Successfully encrypted!')
        except Exception as e:
            print(f'An error has occurred: {e}')
    elif b7 = = 'd':
        b8 = input('enter the file name:\n')
        b10 = [entry.name for entry in os.scandir(os.getcwd()) if entry.name.endswith('.b9')]
        if not b10:
            print('No b9 files found!')
            return
        print(b10[0])
        with open(b10[0], 'r') as f:
            b6 = f.read()
        if len(b6) == 32:
            b9 = binascii.a2b_hex(b6)
            try:
                fonk3(b9, b8)
                print('Successfully decrypted!')
            except Exception as e:
                print(f'An error has occurred: {e}')
        else:
            print('A 16 bytes b9 is necessary!')
    else:
        print('Incorrect input!')
if b11 = = '__main__':
    fonk5()