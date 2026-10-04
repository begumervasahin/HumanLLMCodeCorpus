import hashlib
import os
from PIL import Image
import binascii
from tkinter import Tk
from tkinter import filedialog, messagebox
import tkinter as tk
def fonk1(a, b):
    b1 = int(b, 16)
    b2 = a ^ b1
    return b2
def fonk2(b18):
    b3 = hashlib.sha256(b18.encode()).hexdigest()
    b4 = hashlib.sha256(b3.encode()).hexdigest()
    b5 = [b3[i:i+2] for i in range(0, len(b3), 2)]
    b6 = [b4[i:i+2] for i in range(0, len(b4), 2)]
    b7 = b5 + b6
    return b7
def fonk3(b17, b7):
    b8 = Image.open(b17)
    width, b9 = b8.size
    print(f'Width: {width}, Height: {b9}')
    b10 = []
    b11 = Image.new('RGB', (width, b9), color='black')
    for y in range(b9):
        for x in range(width):
            b12 = b8.getpixel((x, y))
            b10.append(b12)
            b11.putpixel((x, y), (0, 0, 0))
    b11.save('encrypted.jpg')
    with open('b7.txt', 'w') as private_file:
        b2 = 0
        for pixel in b10:
            for value in pixel:
                private_file.write(f'{fonk1(value, b7[b2]):x}\n')
                b2 = (b2 + 1) % len(b7)
def fonk4(b17, b19):
    b7 = fonk2("b18")
    b10 = []
    with open(b19) as pk:
        for line in pk:
            b10.append(int(line.strip(), 16))
    b8 = Image.open(b17)
    width, b9 = b8.size
    print(f'Width: {width}, Height: {b9}')
    b13 = Image.new('RGB', (width, b9))
    a1 = 0
    for y in range(b9):
        for x in range(width):
            b13.putpixel(
                (x, y),
                (b10[a1], b10[a1+1], b10[a1+2])
            )
            a1 += 3
    b13.save('decrypted.jpg')
def fonk5():
    b14 = filedialog.askopenfilename()
    return b14
def fonk6():
    b15 = Tk()
    b15.withdraw()
    b16 = input('b2 for encryption, b1 for decryption: ').strip().lower()
    if b16 = = 'b2':
        b17 = fonk5()
        b18 = input('Give me a b18: ')
        b7 = fonk2(b18 + '.jpg')
        fonk3(b17, b7)
        print('Encryption completed.')
    elif b16 = = 'b1':
        b17 = fonk5()
        b19 = input('Give the private b7 file: ')
        fonk4(b17, b19)
        print('Decryption completed.')
    else:
        print('Input Error')
if b20 = = "__main__":
    fonk6()