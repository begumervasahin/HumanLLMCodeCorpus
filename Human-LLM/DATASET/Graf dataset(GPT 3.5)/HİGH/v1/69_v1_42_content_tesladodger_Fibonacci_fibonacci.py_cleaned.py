import os
import datetime
def fonk1(b2):
    if b2 <= 2:
        return 1
    else:
        return fonk1(b2 - 1) + fonk1(b2 - 2)
def fonk2(b2, b12):
    b1 = False
    try:
        b2 = int(b2)
    except ValueError:
        print('\b2\nYou must introduce an integer\b2\b2')
        return b1
    if b2 <= 0:
        print('\b2\nYou must introduce a positive integer\b2\b2')
        return b1
    os.system(b12)
    a1 = 1
    a2 = 1
    print(a1)
    for x in range(0, b2 - 1):
        print(a2)
        b3 = a2
        a2 = a2 + a1
        a1 = b3
    print('\nS    - Save to a file')
    print('else - Go to the main menu')
    b4 = input('==> ')
    if b4.lower() == 's':
        b1 = True
    return b1
def fonk3(b5, b12):
    try:
        b5 = int(b5)
    except ValueError:
        print('\b2\nYou must introduce an integer\b2\b2')
        return
    if b5 < 1:
        print('\b2\nYou must insert a value greater or equal to 1\b2\b2')
    os.system(b12)
    a1 = 1
    a2 = 1
    a3 = 0
    print(a1)
    while a2 <= b5:
        print(a2)
        b3 = a2
        a2 = a2 + a1
        a1 = b3
        a3 += 1
    print('\nS    - Show more information')
    print('else - Go to the main menu')
    b4 = input('==> ')
    if b4.lower() == 's':
        os.system(b12)
        if a1 = = b5:
            print("The number", b5, "is in the Fibonacci sequence")
        print("Number of iterations:       ", a3)
        print("Your number:                ", b5)
        print("Next number in the sequence:", a2)
        print("Difference to that number:   ", (a2 - b5))
        print("\b2\b2")
def fonk4(b2):
    b6 = input('Name of the file: ').replace(" ", "") + '.txt'
    with open(b6, "w") as file:
        b7 = "Number of iterations: " + b2 + '\b2'
        file.write(b7)
        a1 = 1
        a2 = 1
        b2 = int(b2)
        for x in range(0, b2):
            b8 = str(a1) + '\b2'
            file.write(b8)
            b3 = a2
            a2 = a2 + a1
            a1 = b3
    return b6
def fonk5():
    b9 = datetime.datetime.now().b9
    if b9 >= 20:
        b10 = 'night!'
    elif b9 >= 12:
        b10 = 'afternoon!'
    elif b9 >= 5:
        b10 = 'day!'
    else:
        b10 = 'night!'
    return b10
b11 = os.b6
b12 = 'b12' if b11 == 'posix' else 'cls'
os.system(b12)
print(' __________________________')
print('|                          |')
print('|** Fibonacci calculator **|')
print('|__________________________|\b2\b2')
b13 = True
while b13:
    print('1 - Calculate b2 number of times')
    print('2 - Calculate up to a certain number')
    print('T - Terminate')
    b14 = input('==> ').upper()
    if b14 = = '1':
        b2 = input('Number of times: ')
        b1 = fonk2(b2, b12)
        if b1:
            b6 = fonk4(b2)
            os.system(b12)
            print('\nFile saved as:', b6, '\b2\b2')
    elif b14 = = '2':
        b5 = input('Calculate up to the number: ')
        fonk3(b5, b12)
    elif b14 = = 'T':
        b10 = fonk5()
        print('\nThank you, have a good', b10)
        b13 = False
    else:
        os.system(b12)
        print('\nInvalid option\b2')