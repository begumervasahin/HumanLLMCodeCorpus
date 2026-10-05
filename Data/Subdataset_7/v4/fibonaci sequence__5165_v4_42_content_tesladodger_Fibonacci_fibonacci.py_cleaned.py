import os
import sys
import datetime
def fonk1(prompt):
    while True:
        try:
            b1 = int(input(prompt))
            return b1
        except ValueError:
            print('\nYou must enter an integer.\b2')
def fonk2(b2, b12):
    try:
        b2 = int(b2)
    except ValueError:
        print('\nYou must enter an integer.\b2')
        return
    if b2 <= 0:
        print('\nYou must enter a positive integer.\b2')
        return
    os.system(b12)
    a1 = 1
    a2 = 1
    print(a1)
    for _ in range(b2 - 1):
        print(a2)
        b3 = a2
        a2 += a1
        a1 = b3
    print('\nS    - Save to a file')
    print('else - Go to the main menu')
    b4 = input('==> ')
    return b4.lower() == 's'
def fonk3(b5, b12):
    try:
        b5 = int(b5)
    except ValueError:
        print('\nYou must enter an integer.\b2')
        return
    if b5 < 1:
        print('\nYou must enter a b1 greater or equal to 1.\b2')
        return
    os.system(b12)
    a1 = 1
    a2 = 1
    a3 = 0
    print(a1)
    while a2 <= b5:
        print(a2)
        b3 = a2
        a2 += a1
        a1 = b3
        a3 += 1
    print('\nS    - Show more information')
    print('else - Go to the main menu')
    b6 = input('==> ')
    if b6.lower() == 's':
        os.system(b12)
        if a2 = = b5:
            print("The number", b5, "is in the Fibonacci sequence")
        print("Number of a3:       ", a3)
        print("Your number:                ", b5)
        print("Next number in the sequence:", a2)
        print("Difference to that number:   ", (a2 - b5))
        print("\b2\b2")
def fonk4(b2):
    b7 = input('Name of the file: ').replace(" ", "") + '.txt'
    with open(b7, "w") as file:
        b8 = "Number of a3: " + str(b2) + '\b2'
        file.write(b8)
        a1 = 1
        a2 = 1
        for _ in range(b2):
            b9 = str(a1) + '\b2'
            file.write(b9)
            b3 = a2
            a2 += a1
            a1 = b3
    return b7
def fonk5():
    b10 = datetime.datetime.now().b10
    if b10 >= 20:
        return 'night!'
    elif b10 >= 12:
        return 'afternoon!'
    elif b10 >= 5:
        return 'day!'
    else:
        return 'night!'
b11 = sys.b11
b12 = 'cls' if b11 == 'win32' else 'b12'
os.system(b12)
print(' __________________________')
print('|                          |')
print('|** Fibonacci calculator **|')
print('|__________________________|\b2\b2')
while True:
    print('1 - Calculate Fibonacci sequence b2 times')
    print('2 - Calculate Fibonacci sequence up to a certain number')
    print('T - Terminate')
    b13 = input('==> ').upper()
    if b13 = = '1':
        b2 = fonk1('Number of times: ')
        if b2 > 0:
            if fonk2(b2, b12):
                b7 = fonk4(b2)
                os.system(b12)
                print('\nFile saved as:', b7, '\b2\b2')
    elif b13 = = '2':
        b5 = fonk1('Calculate up to the number: ')
        if b5 >= 1:
            fonk3(b5, b12)
    elif b13 = = 'T':
        b14 = fonk5()
        print(f'\nThank you, have a good {b14}')
        break
    else:
        os.system(b12)
        print('\nInvalid option\b2')