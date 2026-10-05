from tkinter import *
from tkinter.filedialog import askopenfilename
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
def fonk3(b12):
    b5 = []
    b6 = fonk2(fonk5())
    b7 = Image.open(b12, mode='r')
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
def fonk4(b12, b14):
    b6 = fonk2(fonk5())
    b5 = []
    b7 = Image.open(b12, mode='r')
    with open(b14) as pk:
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
    b11 = Tk()
    b11.withdraw()
    b12 = askopenfilename(title="Select Image for Encryption/Decryption", filetypes=[("Image Files", "*.jpg *.png *.jpeg")])
    if b12:
        b13 = input('Enter "e" for encryption or "d" for decryption: ')
        if b13 = = 'e':
            fonk3(b12)
        elif b13 = = 'd':
            b14 = input('Enter the path of the private b6 file: ')
            fonk4(b12, b14)
        else:
            print('Input Error')
    else:
        print("No b7 selected.")
if b15 = = "__main__":
    fonk6()