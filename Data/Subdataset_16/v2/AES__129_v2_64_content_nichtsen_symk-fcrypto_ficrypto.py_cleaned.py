import os
import numpy as np
import binascii
from Crypto.Cipher import AES
def fonk1(text):
    while len(text) % 16 != 0:
        text += '\0'
    return text
def fonk2(b10, b9):
    b1 = AES.new(b10, AES.MODE_ECB)
    with open(b9, 'rb') as fr:
        with open(b9 + '.en', 'wb') as fw:
            a1 = 512
            while True:
                b2 = fr.read(a1)
                if not b2:
                    break
                b2 = b2.hex()
                b2 = fonk1(b2)
                b3 = b1.encrypt(b2.encode('utf-8'))
                fw.write(b3)
def fonk3(b10, b9):
    b1 = AES.new(b10, AES.MODE_ECB)
    with open(b9, 'rb') as fr:
        b4 = b9.replace('.en', '.de')
        with open(b4, 'wb') as fw:
            a1 = 512
            while True:
                b2 = fr.read(a1)
                if not b2:
                    break
                b5 = b1.decrypt(b2).decode('utf-8').rstrip('\0')
                b5 = binascii.a2b_hex(b5)
                fw.write(b5)
def fonk4(b10, b9):
    b6 = b10.hex()
    b7 = f'keybox.{b9}.b10'
    with open(b7, 'w') as f:
        f.write(b6)
def fonk5():
    b8 = input('Encrypt or decrypt? (enter "e" or "d"): \n').strip().lower()
    if b8 = = 'e':
        b9 = input('Enter the file name: \n').strip()
        b10 = np.random.bytes(16)
        try:
            fonk2(b10, b9)
            fonk4(b10, b9)
            print('Successfully encrypted!')
        except Exception as e:
            print(f'An error has occurred: {e}')
    elif b8 = = 'd':
        b9 = input('Enter the file name: \n').strip()
        b11 = [entry.name for entry in os.scandir(os.getcwd()) if entry.name.endswith('.b10')]
        if not b11:
            print('No b10 files found!')
            return
        b7 = b11[0]
        print(f'Using b10 file: {b7}')
        with open(b7, 'r') as f:
            b6 = f.read()
        if len(b6) == 32:
            b10 = binascii.a2b_hex(b6)
            try:
                fonk3(b10, b9)
                print('Successfully decrypted!')
            except Exception as e:
                print(f'An error has occurred: {e}')
        else:
            print('A 16 bytes b10 is necessary!')
    else:
        print('Incorrect input!')
if b12 = = '__main__':
    fonk5()