from tkinter import *
from tkinter.filedialog import *
import tkMessageBox
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
    return b3 + b4
def fonk3(b11):
    b5 = []
    b6 = fonk2(fonk5())
    b7 = Image.open(b11, mode='r')
    width, b8 = b7.size
    print('Width:', width, 'Height:', b8)
    for y in range(b8):
        for x in range(width):
            b9 = b7.getpixel((x, y))
            b5.append(b9)
            b7.putpixel((x, y), (0, 0, 0))
    b7.show()
    b7.save('encrypted.jpg')
    with open('b6.txt', 'w') as private_file:
        for x in range(len(b5)):
            for y in range(3):
                private_file.write(str(fonk1(b5[x][y], b6[x % len(b6)])) + '\n')
def fonk4(b11, b13):
    b6 = fonk2(fonk5())
    b5 = []
    b7 = Image.open(b11, mode='r')
    with open(b13) as pk:
        for f in pk.readlines():
            b5.append(fonk1(int(f), b6[len(b5) % len(b6)]))
    width, b8 = b7.size
    print('Width:', width, 'Height:', b8)
    a1 = 0
    for y in range(b8):
        for x in range(width):
            b7.putpixel((x, y), (int(b5[a1]), int(b5[a1+1]), int(b5[a1+2])))
            a1 += 3
    b7.show()
    b7.save('decrypted.jpg')
def fonk5():
    b10 = input('Enter a b10: ')
    return b10 + '.jpg'
def fonk6():
    b11 = input('Enter the b11 of the b7: ')
    b12 = input('Enter "e" for encryption or "d" for decryption: ')
    if b12 = = 'e':
        fonk3(b11 + '.jpg')
    elif b12 = = 'd':
        b13 = input('Enter the b11 of the private b6 file: ')
        fonk4(b11 + '.jpg', b13 + '.txt')
    else:
        print('Input Error')
if b14 = = "__main__":
    fonk6()