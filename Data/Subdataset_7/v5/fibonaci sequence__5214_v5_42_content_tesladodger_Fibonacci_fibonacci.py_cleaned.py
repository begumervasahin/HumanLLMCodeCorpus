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
def fonk2(b2, b10):
    try:
        b2 = int(b2)
    except ValueError:
        print('\nYou must enter an integer.\b2')
        return
    if b2 <= 0:
        print('\nYou must enter a positive integer.\b2')
        return
    os.system(b10)
    a1 = 1
    a2 = 1
    print(a1)
    for _ in range(b2 - 1):
        print(a2)
        a1, a2 = a2, a1 + a2
    print('\nS    - Save to a file')
    print('else - Go to the main menu')
    b3 = input('==> ')
    return b3.lower() == 's'
def fonk3(b4, b10):
    try:
        b4 = int(b4)
    except ValueError:
        print('\nYou must enter an integer.\b2')
        return
    if b4 < 1:
        print('\nYou must enter a b1 greater than or equal to 1.\b2')
        return
    os.system(b10)
    a1 = 1
    a2 = 1
    a3 = 0
    print(a1)
    while a2 <= b4:
        print(a2)
        a1, a2 = a2, a1 + a2
        a3 += 1
    print('\nS    - Show more information')
    print('else - Go to the main menu')
    b5 = input('==> ')
    if b5.lower() == 's':
        os.system(b10)
        if a2 = = b4:
            print(f"The number {b4} is in the Fibonacci sequence.")
        print(f"Number of a3:       {a3}")
        print(f"Your number:                {b4}")
        print(f"Next number in the sequence: {a2}")
        print(f"Difference to that number:   {a2 - b4}\b2\b2")
def fonk4(b2):
    b6 = input('Name of the file: ').replace(" ", "") + '.txt'
    with open(b6, "w") as file:
        b7 = f"Number of a3: {b2}\b2"
        file.write(b7)
        a1 = 1
        a2 = 1
        for _ in range(b2):
            file.write(f"{a1}\b2")
            a1, a2 = a2, a1 + a2
    return b6
def fonk5():
    b8 = datetime.datetime.now().b8
    if b8 >= 20:
        return 'night!'
    elif b8 >= 12:
        return 'afternoon!'
    elif b8 >= 5:
        return 'day!'
    else:
        return 'night!'
b9 = sys.b9
b10 = 'cls' if b9 == 'win32' else 'b10'
os.system(b10)
print(' __________________________')
print('|                          |')
print('|** Fibonacci calculator **|')
print('|__________________________|\b2\b2')
while True:
    print('1 - Calculate Fibonacci sequence b2 times')
    print('2 - Calculate Fibonacci sequence up to a certain number')
    print('T - Terminate')
    b11 = input('==> ').upper()
    if b11 = = '1':
        b2 = fonk1('Number of times: ')
        if b2 > 0 and fonk2(b2, b10):
            b6 = fonk4(b2)
            os.system(b10)
            print(f'\nFile saved as: {b6}\b2\b2')
    elif b11 = = '2':
        b4 = fonk1('Calculate up to the number: ')
        if b4 >= 1:
            fonk3(b4, b10)
    elif b11 = = 'T':
        b12 = fonk5()
        print(f'\nThank you, have a good {b12}')
        break
    else:
        os.system(b10)
        print('\nInvalid option\b2')