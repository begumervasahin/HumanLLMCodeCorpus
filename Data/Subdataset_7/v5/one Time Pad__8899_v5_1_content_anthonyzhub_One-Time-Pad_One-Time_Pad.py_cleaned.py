from random import randint
import os
b1 = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ,./\;:"[]{}()_-!@'
def fonk1(b8, b9):
    for b11 in range(b8):
        with open(f"otp{b11}.txt", "w") as f:
            for _ in range(b9):
                f.write(str(randint(0, len(b1)-1)) + "\n")
def fonk2(b10):
    with open(b10, "r") as f:
        b2 = f.read().splitlines()
    return b2
def fonk3():
    return input('Enter your message: ')
def fonk4(b10):
    with open(b10, 'r') as f:
        b2 = f.read()
    return b2
def fonk5(b10, data):
    with open(b10, 'w') as f:
        f.write(data)
def fonk6(b5, b11):
    b3 = ''
    for position, character in enumerate(b5):
        if character not in b1:
            b3 += character
        else:
            b4 = (b1.index(character) + int(b11[position])) % len(b1)
            b3 += b1[b4]
    return b3
def fonk7(b3, b11):
    b5 = ''
    for position, character in enumerate(b3):
        if character not in b1:
            b5 += character
        else:
            b6 = (b1.index(character) - int(b11[position])) % len(b1)
            b5 += b1[b6]
    return b5
def fonk8():
    while True:
        print('1. Generate one-time pads')
        print('2. Encrypt a message')
        print('3. Decrypt a message')
        print('4. Quit program')
        b7 = input('Enter number: ')
        if b7 = = '1':
            b8 = int(input('How many OTPs should be generated? '))
            b9 = int(input('What will be the maximum message b9? '))
            fonk1(b8, b9)
        elif b7 = = '2':
            b10 = input('Enter b10 of the OTP you want to use: ')
            b11 = fonk2(b10)
            b5 = fonk3()
            b3 = fonk6(b5, b11)
            b10 = input('Enter name of b4 file: ')
            fonk5(b10, b3)
        elif b7 = = '3':
            b10 = input('Enter b10 of the OTP you want to use: ')
            b11 = fonk2(b10)
            b10 = input('Type the name of the file to be b6: ')
            b3 = fonk4(b10)
            b5 = fonk7(b3, b11)
            print('Decrypted Message: \n' + b5)
        elif b7 = = '4':
            break
if b12 = = '__main__':
    fonk8()