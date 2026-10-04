
import hashlib
from PIL import Image
from tkinter import Tk, filedialog, messagebox
def fonk1(b13, key_hex):
    b1 = int(key_hex, 16)
    return b13 ^ b1
def fonk2(b19):
    b2 = hashlib.sha256(b19.encode()).hexdigest()
    b3 = hashlib.sha256(b2.encode()).hexdigest()
    b4 = [b2[i:i+2] for i in range(0, len(b2), 2)]
    b5 = [b3[i:i+2] for i in range(0, len(b3), 2)]
    return b4 + b5
def fonk3(b18, b1):
    b6 = Image.open(b18)
    width, b7 = b6.size
    print(f'Image dimensions: b8 = {width}, Height = {b7}')
    b9 = []
    b10 = Image.new('RGB', (width, b7), color='black')
    for y in range(b7):
        for x in range(width):
            b11 = b6.getpixel((x, y))
            b9.append(b11)
            b10.putpixel((x, y), (0, 0, 0))
    b10.save('encrypted.jpg')
    with open('b1.txt', 'w') as b20:
        a1 = 0
        for b11 in b9:
            for b13 in b11:
                b12 = fonk1(b13, b1[a1])
                b20.write(f'{b12:02x}\n')
                a1 = (a1 + 1) % len(b1)
def fonk4(b18, b20):
    b1 = fonk2("b19")
    b9 = []
    with open(b20) as file:
        for line in file:
            b13 = int(line.strip(), 16)
            b9.append(b13)
    b6 = Image.open(b18)
    width, b7 = b6.size
    print(f'Image dimensions: b8 = {width}, Height = {b7}')
    b14 = Image.new('RGB', (width, b7))
    a1 = 0
    for y in range(b7):
        for x in range(width):
            r, g, b15 = b9[a1:a1+3]
            b14.putpixel((x, y), (r, g, b15))
            a1 += 3
    b14.save('decrypted.jpg')
def fonk5():
    b16 = Tk()
    b16.withdraw()
    return filedialog.askopenfilename()
def fonk6():
    b17 = input('Enter "e" for encryption or "d" for decryption: ').strip().lower()
    if b17 = = 'e':
        b18 = fonk5()
        b19 = input('Enter a b19: ')
        b1 = fonk2(b19 + '.jpg')
        fonk3(b18, b1)
        print('Encryption completed.')
    elif b17 = = 'd':
        b18 = fonk5()
        b20 = input('Enter the b1 file path: ')
        fonk4(b18, b20)
        print('Decryption completed.')
    else:
        print('Invalid input. Please enter "e" for encryption or "d" for decryption.')
if b21 = = "__main__":
    fonk6()