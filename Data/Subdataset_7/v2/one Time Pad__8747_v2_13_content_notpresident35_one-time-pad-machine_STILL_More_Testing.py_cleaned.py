from random import randint
from time import strftime
b1 = 'abcdefghijklmnopqrstuvwxyz'
def fonk1(b8, b9):
    b2 = strftime("%Y-%m-%d-%H-%M-%S")
    for b11 in range(b8):
        with open(f"otp{b11}{b2}.txt", "w") as f:
            for _ in range(b9):
                f.write(f"{randint(0, 26)}\n")
def fonk2(b10):
    with open(b10, "r") as f:
        return f.read().splitlines()
def fonk3():
    return input("Enter the message to be b4: ").lower()
def fonk4(b10):
    with open(b10, "r") as f:
        return f.read()
def fonk5(b10, data):
    with open(b10, 'w') as f:
        f.write(data)
def fonk6(b5, b11):
    b3 = ''
    for position, character in enumerate(b5):
        if character not in b1:
            b3 += character
        else:
            b4 = (b1.index(character) + int(b11[position])) % 26
            b3 += b1[b4]
    return b3
def fonk7(b3, b11):
    b5 = ''
    for position, character in enumerate(b3):
        if character not in b1:
            b5 += character
        else:
            b6 = (b1.index(character) - int(b11[position])) % 26
            b5 += b1[b6]
    return b5
def fonk8():
    while True:
        print('\nWhat would you like to do?')
        print('1. Generate one-time pads')
        print('2. Encrypt a message')
        print('3. Decrypt a message')
        print('4. Quit the program')
        b7 = input('Please type 1, 2, 3, or 4 and press Enter: ')
        if b7 = = "1":
            b8 = int(input('How many one-time pads would you like to generate? '))
            b9 = int(input('What will be your maximum message b9? '))
            fonk1(b8, b9)
        elif b7 = = '2':
            b10 = input('Type in the b10 of the OTP you want to use: ')
            b11 = fonk2(b10)
            b5 = fonk3()
            b3 = fonk6(b5, b11)
            b10 = input('What will be the name of the b4 file? ')
            fonk5(b10, b3)
        elif b7 = = '3':
            b10 = input('Type in the b10 of the OTP you want to use: ')
            b11 = fonk2(b10)
            b10 = input('Type in the name of the file to be b6: ')
            b3 = fonk4(b10)
            b5 = fonk7(b3, b11)
            print('The message reads:')
            print('')
            print(b5)
        elif b7 = = '4':
            print("Exiting the program...")
            break
        else:
            print("Invalid b7. Please try again.")
fonk8()