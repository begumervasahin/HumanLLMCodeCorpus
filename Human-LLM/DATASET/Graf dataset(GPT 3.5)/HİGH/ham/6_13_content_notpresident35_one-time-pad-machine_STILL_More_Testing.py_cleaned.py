from random import randint
from time import strftime
b1 = 'abcdefghijklmnopqrstuvwxyz'
def fonk1(b10, b11):
    for b13 in range(b10):
        with open("otp" + str(b13) + str(dates) + ".txt", "w") as f:
            for i in range(b11):
                f.write(str(randint(0,26))+"\n")
def fonk2(b12):
    with open(b12, "r") as f:
        b2 = f.read().splitlines()
    return b2
def fonk3():
    b3 = input("Enter the message to be b5")
    return b3.lower()
def fonk4(b12):
    with open(b12, "r") as f:
        b2 = f.read()
    return b2
def fonk5(b12, data):
    with open(b12, 'w') as f:
        f.write(data)
def fonk6(b6, b13):
    b4 = ''
    for position, character in enumerate(b6):
        if character not in b1:
            b4 += character
        else:
            b5 = (b1.index(character) + int(b13[position])) % 26
            b4 += b1[b5]
    return b4
def fonk7(b4, b13):
    b6 = ''
    for position, character in enumerate(b4):
        if character not in b1:
            b6 += character
        else:
            b7 = (b1.index(character) - int(b13[position])) % 26
            b6 += b1[b7]
    return b6
def fonk8():
    b8 = ["1", "2", "3", '4']
    b9 = '0'
    while True:
        while b9 not in b8:
            print('What would you like to do?')
            print('1. Generate one-time pads')
            print('2. Encrypt a message')
            print('3. Decrypt a message')
            print('4. Quit the program')
            b9 = input('Please type 1, 2, 3 or 4 and press Enter ')
            if b9 = = "1":
                b10 = int(input('How many one-time pads would you like to generate? '))
                b11 = int(input('What will be your maximum message b11? '))
                fonk1(b10, b11)
            elif b9 = = '2':
                b12 = input('Type in the b12 of the OTP you want to use ')
                b13 = fonk2(b12)
                b6 = fonk3()
                b4 = fonk6(b6, b13)
                b12 = input('What will be the name of the b5 file? ')
                fonk5(b12, b4)
            elif b9 = = '3':
                b12 = input('Type in the b12 of the OTP you want to use ')
                b13 = fonk2(b12)
                b12 = input('Type in the name of the file to be b7 ')
                b4 = fonk4(b12)
                b6 = fonk7(b4, b13)
                print('The message reads:')
                print('')
                print(b6)
            elif b9 = = '4':
                exit()
                print("failed")
            b9 = '0'
fonk8()