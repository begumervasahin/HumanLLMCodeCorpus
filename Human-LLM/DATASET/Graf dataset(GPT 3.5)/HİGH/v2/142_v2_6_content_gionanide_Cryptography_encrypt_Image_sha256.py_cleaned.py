from tkinter import *
from tkinter.filedialog import *
import tkinter.messagebox as tkMessageBox
import os
from PIL import Image
import hashlib
def fonk1(a, b):
    return a ^ int(b, 16)
def fonk2(b10):
    b1 = hashlib.sha256(b10.encode()).hexdigest()
    b2 = hashlib.sha256(b1.encode()).hexdigest()
    b3 = [int(b1[i:i+2], 16) for i in range(0, len(b1), 2)]
    b4 = [int(b2[i:i+2], 16) for i in range(0, len(b2), 2)]
    b5 = b3 + b4
    return b5
def fonk3(b9, b10):
    b5 = fonk2(b10)
    b6 = Image.open(b9, mode='r')
    width, b7 = b6.size
    b8 = [b6.getpixel((x, y)) for y in range(b7) for x in range(width)]
    for y in range(b7):
        for x in range(width):
            b6.putpixel((x, y), (0, 0, 0))
    b6.show()
    b6.save('encrypted.jpg')
    with open('b5.txt', 'w') as private_key_file:
        for pixel in b8:
            for val in pixel:
                private_key_file.write(str(fonk1(val, b5.pop(0))))
                private_key_file.write('\n')
def fonk4(b9, b12, b10):
    b5 = fonk2(b10)
    b8 = []
    with open(b12) as pk:
        for f in pk.readlines():
            b8.append(fonk1(int(f), b5.pop(0)))
    b6 = Image.open(b9, mode='r')
    width, b7 = b6.size
    a1 = 0
    for y in range(b7):
        for x in range(width):
            b6.putpixel((x, y), (int(b8[a1]), int(b8[a1+1]), int(b8[a1+2])))
            a1 += 3
    b6.show()
    b6.save('decrypted.jpg')
def fonk5():
    b9 = input('Enter the path of the b6 file: ')
    b10 = input('Enter the b10: ')
    b11 = input('Enter "e" for encryption or "d" for decryption: ')
    if b11 = = 'e':
        fonk3(b9, b10)
    elif b11 = = 'd':
        b12 = input('Enter the path of the private b5 file: ')
        fonk4(b9, b12, b10)
    else:
        print('Input Error')
if b13 = = "__main__":
    fonk5()