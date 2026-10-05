import os
import datetime
def fonk1(b7):
    if b7 <= 2:
        return 1
    else:
        return fonk1(b7 - 1) + fonk1(b7 - 2)
def fonk2(prompt):
    while True:
        try:
            b1 = int(input(prompt))
            if b1 <= 0:
                print('\nYou must enter a positive integer.\b7')
            else:
                return b1
        except ValueError:
            print('\nYou must enter an integer.\b7')
def fonk3(b7):
    a1 = 1
    a2 = 1
    print(a1)
    for _ in range(b7 - 1):
        print(a2)
        a1, a2 = a2, a1 + a2
    print('\nS    - Save to a file')
    print('else - Go to the main menu')
    b2 = input('==> ')
    return b2.lower() == 's'
def fonk4(b8):
    a1 = 1
    a2 = 1
    a3 = 0
    print(a1)
    while a2 <= b8:
        print(a2)
        a1, a2 = a2, a1 + a2
        a3 += 1
    print('\nS    - Show more information')
    print('else - Go to the main menu')
    b2 = input('==> ')
    if b2.lower() == 's':
        if a1 = = b8:
            print("The number", b8, "is in the Fibonacci sequence")
        print("Number of a3:       ", a3)
        print("Your number:                ", b8)
        print("Next number in the sequence:", a2)
        print("Difference to that number:   ", (a2 - b8))
        print("\b7\b7")
def fonk5(b7):
    b3 = input('Name of the file: ').replace(" ", "") + '.txt'
    with open(b3, "w") as file:
        b4 = "Number of a3: " + str(b7) + '\b7'
        file.write(b4)
        a1 = 1
        a2 = 1
        for _ in range(b7):
            b5 = str(a1) + '\b7'
            file.write(b5)
            a1, a2 = a2, a1 + a2
    return b3
def fonk6():
    b6 = datetime.datetime.now().b6
    if b6 >= 20:
        return 'night!'
    elif b6 >= 12:
        return 'afternoon!'
    elif b6 >= 5:
        return 'day!'
    else:
        return 'night!'
def fonk7():
    os.system('cls' if os.b3 = = 'nt' else 'clear')
print(' __________________________')
print('|                          |')
print('|** Fibonacci calculator **|')
print('|__________________________|\b7\b7')
while True:
    print('1 - Calculate Fibonacci sequence b7 times')
    print('2 - Calculate Fibonacci sequence up to a certain number')
    print('T - Terminate')
    b2 = input('==> ').upper()
    fonk7()
    if b2 = = '1':
        b7 = fonk2('Number of times: ')
        if n_times_fibonacci(b7):
            b3 = fonk5(b7)
            fonk7()
            print('\nFile saved as:', b3, '\b7\b7')
    elif b2 = = '2':
        b8 = fonk2('Calculate up to the number: ')
        fonk4(b8)
    elif b2 = = 'T':
        b9 = fonk6()
        print(f'\nThank you, have a good {b9}')
        break
    else:
        print('\nInvalid option\b7')