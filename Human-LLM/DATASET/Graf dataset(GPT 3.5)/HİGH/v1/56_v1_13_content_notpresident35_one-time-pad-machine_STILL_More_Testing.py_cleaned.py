from random import randint
from time import strftime
b1 = 'abcdefghijklmnopqrstuvwxyz'
def fonk1(b11, b12):
    b2 = strftime("%Y-%m-%d-%H-%M-%S")
    for b14 in range(b11):
        with open("otp" + str(b14) + str(b2) + ".txt", "w") as f:
            for i in range(b12):
                f.write(str(randint(0, 26)) + "\n")
def fonk2(b13):
    with open(b13, "r") as f:
        b3 = f.read().splitlines()
    return b3
def fonk3():
    b4 = input("Enter the message to be b6: ")
    return b4.lower()
def fonk4(b13):
    with open(b13, "r") as f:
        b3 = f.read()
    return b3
def fonk5(b13, data):
    with open(b13, 'w') as f:
        f.write(data)
def fonk6(b7, b14):
    b5 = ''
    for position, character in enumerate(b7):
        if character not in b1:
            b5 += character
        else:
            b6 = (b1.index(character) + int(b14[position])) % 26
            b5 += b1[b6]
    return b5
def fonk7(b5, b14):
    b7 = ''
    for position, character in enumerate(b5):
        if character not in b1:
            b7 += character
        else:
            b8 = (b1.index(character) - int(b14[position])) % 26
            b7 += b1[b8]
    return b7
def fonk8():
    b9 = ["1", "2", "3", "4"]
    b10 = '0'
    while True:
        while b10 not in b9:
            print('What would you like to do?')
            print('1. Generate one-time pads')
            print('2. Encrypt a message')
            print('3. Decrypt a message')
            print('4. Quit the program')
            b10 = input('Please type 1, 2, 3, or 4 and press Enter: ')
            if b10 = = "1":
                b11 = int(input('How many one-time pads would you like to generate? '))
                b12 = int(input('What will be your maximum message b12? '))
                fonk1(b11, b12)
            elif b10 = = '2':
                b13 = input('Type in the b13 of the OTP you want to use: ')
                b14 = fonk2(b13)
                b7 = fonk3()
                b5 = fonk6(b7, b14)
                b13 = input('What will be the name of the b6 file? ')
                fonk5(b13, b5)
            elif b10 = = '3':
                b13 = input('Type in the b13 of the OTP you want to use: ')
                b14 = fonk2(b13)
                b13 = input('Type in the name of the file to be b8: ')
                b5 = fonk4(b13)
                b7 = fonk7(b5, b14)
                print('The message reads:')
                print('')
                print(b7)
            elif b10 = = '4':
                exit()
                print("failed")
            b10 = '0'
fonk8()