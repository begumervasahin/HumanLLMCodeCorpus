import os
import numpy as np
import binascii
from Crypto.Cipher import AES
def fonk1(text):
    while len(text) % 16 != 0:
        text += '\0'
    return text
def fonk2(b10,b9):
    b1 = AES.new(b10, AES.MODE_ECB)
    b2 = open(b9,'rb')
    b3 = open(b9+'.en', 'wb')
    a1 = 512
    while True:
        b4 = b2.read(a1)
        if not b4:
            break
        b4 = b4.hex()
        b4 = fonk1(b4)
        b4 = b1.encrypt(b4)
        b3.write(b4)
    b2.close()
    b3.close()
def fonk3(b10,b9):
    b1 = AES.new(b10, AES.MODE_ECB)
    b2 = open(b9, 'rb')
    b5 = b9.split(".en")[0] + '.de'
    b3 = open(b5, 'wb')
    print(b9,b5)
    a1 = 512
    while True:
        b4 = b2.read(a1)
        if not b4:
            break
        b4 = b1.decrypt(b4).decode()
        b4 = b4.rstrip('\0')
        b4 = binascii.a2b_hex(b4)
        b3.write(b4)
    b2.close()
    b3.close()
def fonk4(b10,b9):
   b6 = b10.hex()
   b7 = open('keybox.'+ b9 +'.b10', 'w')
   b7.write(b6)
   b7.close()
def fonk5():
    b8 = input('encrypt or decrypt? (enter "e" or "d") \n')
    if (b8 = = 'e'):
        b9 = input('enter the file name:\n')
        b10 = np.random.bytes(16)
        try:
            fonk2(b10,b9)
            fonk4(b10,b9)
            print ('Successfully encypted!')
        except:
            print('A error has occured!')
            input('Enter to exist...')
    elif (b8 = = 'd'):
        b9 = input('enter the file name:\n')
        b11 = os.scandir(os.getcwd())
        b12 = []
        for entry in b11:
            if entry.name.split('.')[-1] == 'b10':
                b12.append(entry.name)
        print(b12[0])
        b7 = open(b12[0],'r')
        b10 = b7.read(512)
        if (len(b10) == 32):
            b10 = binascii.a2b_hex(b10)
            try:
                fonk3(b10,b9)
                print('Successfully decypted!')
            except:
                print('A error has occured!')
                input('Enter to exist...')
            finally:
                b7.close()
        else:
            print(len(b10))
            print('A 16 bytes b10 is neccessary!')
            input('Enter to exist...')
    else:
        print('incorrect input!')
        input('Enter to exist...')
if b13 = = '__main__':
    fonk5()