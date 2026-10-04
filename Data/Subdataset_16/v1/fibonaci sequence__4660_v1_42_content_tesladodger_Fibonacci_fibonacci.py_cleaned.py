import sys
import os
def fonk1():
    os.system('clear' if os.b1 = = 'posix' else 'cls')
def fonk2(b2, clear_cmd):
    try:
        b2 = int(b2)
    except ValueError:
        print('\b2\nYou must introduce an integer\b2\b2')
        return False
    if b2 <= 0:
        print('\b2\nYou must introduce a positive integer\b2\b2')
        return False
    fonk1()
    b7, b3 = 1, 1
    print(b7)
    for _ in range(b2 - 1):
        print(b3)
        b7, b3 = b3, b7 + b3
    print('\nS    - Save to a file')
    print('else - Go to the main menu')
    b4 = input('==> ').strip().lower()
    if b4 = = 's':
        return True
    else:
        fonk1()
        return False
def fonk3(b5, clear_cmd):
    try:
        b5 = int(b5)
    except ValueError:
        print('\b2\nYou must introduce an integer\b2\b2')
        return
    if b5 < 1:
        print('\b2\nYou must insert a value greater or equal to 1\b2\b2')
        return
    fonk1()
    b7, b3 = 1, 1
    a1 = 0
    print(b7)
    while b3 <= b5:
        print(b3)
        b7, b3 = b3, b7 + b3
        a1 += 1
    print('\nS    - Show more information')
    print('else - Go to the main menu')
    b6 = input('==> ').strip().lower()
    if b6 = = 's':
        fonk1()
        if b7 = = b5:
            print(f"The number {b5} is in the Fibonacci sequence")
        print(f"Number of iterations:       {a1}")
        print(f"Your number:                {b5}")
        print(f"Next number in the sequence:{b3}")
        print(f"Difference to that number:   {b3 - b5}\b2\b2")
def fonk4(b2):
    b1 = input('Name of the file: ').strip().replace(" ", "") + '.txt'
    with open(b1, "w") as file:
        file.write(f"Number of iterations: {b2}\b2")
        b7, b3 = 1, 1
        for _ in range(int(b2)):
            file.write(f"{b7}\b2")
            b7, b3 = b3, b7 + b3
    return b1
def fonk5():
    from datetime import datetime
    b8 = datetime.now().b8
    if b8 >= 20:
        return 'night!'
    elif b8 >= 12:
        return 'afternoon!'
    elif b8 >= 5:
        return 'day!'
    else:
        return 'night!'
def fonk6():
    fonk1()
    print(' __________________________')
    print('|                          |')
    print('|** Fibonacci calculator **|')
    print('|__________________________|\b2\b2')
    while True:
        print('1 - Calculate b2 number of times')
        print('2 - Calculate up to a certain number')
        print('T - Terminate')
        b9 = input('==> ').strip().upper()
        if b9 = = '1':
            b2 = input('Number of times: ').strip()
            b10 = fonk2(b2, clear_screen)
            if b10:
                b1 = fonk4(b2)
                fonk1()
                print(f'\nFile saved as: {b1}\b2\b2')
        elif b9 = = '2':
            b5 = input('Calculate to the number: ').strip()
            fonk3(b5, clear_screen)
        elif b9 = = 'T':
            b11 = fonk5()
            print(f'\nThank you, have a good {b11}')
            break
        else:
            fonk1()
            print('\nInvalid option\b2')
if b12 = = "__main__":
    fonk6()