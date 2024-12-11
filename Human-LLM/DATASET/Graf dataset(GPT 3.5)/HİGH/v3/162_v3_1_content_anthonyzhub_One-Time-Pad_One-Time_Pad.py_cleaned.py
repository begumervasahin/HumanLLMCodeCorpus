from random import randint
b1 = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ,./\\;:"[]{}()_-!@'
def fonk1(b9, b10):
    for b12 in range(b9):
        with open(f"otp{b12}.txt", "w") as f:
            for _ in range(b10):
                f.write(str(randint(0, len(b1) - 1)) + "\n")
def fonk2(b11):
    with open(b11, "r") as f:
        b2 = f.read().splitlines()
    return b2
def fonk3():
    b3 = input('Enter your message: ')
    return b3
def fonk4(b11):
    with open(b11, 'r') as f:
        b2 = f.read()
    return b2
def fonk5(b11, data):
    with open(b11, 'w') as f:
        f.write(data)
def fonk6(b6, b12):
    b4 = ''
    for position, character in enumerate(b6):
        if character not in b1:
            b4 += character
        else:
            b5 = (b1.index(character) + int(b12[position])) % len(b1)
            b4 += b1[b5]
    return b4
def fonk7(b4, b12):
    b6 = ''
    for position, character in enumerate(b4):
        if character not in b1:
            b6 += character
        else:
            b7 = (b1.index(character) - int(b12[position])) % len(b1)
            b6 += b1[b7]
    return b6
def fonk8():
    while True:
        print('1. Generate one-time pads')
        print('2. Encrypt a message')
        print('3. Decrypt a message')
        print('4. Quit program')
        b8 = input('Enter number: ')
        if b8 = = '1':
            b9 = int(input('How many OTPs should be generated? '))
            b10 = int(input('What will be the maximum message b10? '))
            fonk1(b9, b10)
        elif b8 = = '2':
            b11 = input('Enter b11 of the OTP you want to use: ')
            b12 = fonk2(b11)
            b6 = fonk3()
            b4 = fonk6(b6, b12)
            b11 = input('Enter name of b5 file: ')
            fonk5(b11, b4)
        elif b8 = = '3':
            b11 = input('Enter b11 of the OTP you want to use: ')
            b12 = fonk2(b11)
            b11 = input('Type the name of the file to be b7: ')
            b4 = fonk4(b11)
            b6 = fonk7(b4, b12)
            print('Decrypted Message: \n' + b6)
        elif b8 = = '4':
            break
fonk8()