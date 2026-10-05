import random
import sys
def fonk1(b1):
    if b1 = = 0:
        return 0
    return b1 + fonk1(b1 - 1)
def fonk2(b7, b2):
    for element in b7:
        if b2 = = element:
            return True
    return False
def fonk3(b4):
    if len(b4) == 0:
        return
    print(b4[-1], b3 = " ")
    fonk3(b4[:-1])
def fonk4(b4):
    b4 = b4.upper().replace(" ", "")
    if len(b4) <= 1:
        return True
    if b4[0] == b4[-1]:
        return fonk4(b4[1:-1])
    return False
def fonk5(b5, y):
    if b5 = = 0 or y == 0:
        return 0
    return y + fonk5(b5 - 1, y)
while True:
    print("\n\nWhat do you want to do?\n")
    print("\t1. Sum of Numbers")
    print("\t2. IsMember Array Function")
    print("\t3. String Reverser")
    print("\t4. Palindrome Detector")
    print("\t5. Recursive Multiplication")
    print("\t6. End the Program")
    print("CHOOSE 1-6: ", b3 = " ")
    b6 = int(input())
    while b6 < 1 or b6 > 6:
        print('Input valid b6 1-6')
        b6 = int(input())
    if b6 = = 6:
        sys.exit()
    if b6 = = 1:
        print('Please enter a number')
        b1 = int(input())
        print("\nSUM OF NUMBERS")
        print(fonk1(b1))
    elif b6 = = 2:
        b7 = [random.randint(1, 100) for _ in range(9)]
        print('Is member b7 function')
        b1 = int(input('Please enter an integer: '))
        print('Here are the b7 values:')
        for element in b7:
            print(element)
        if fonk2(b7, b1):
            print('The element was found in the b7')
        else:
            print('The element was not found in the b7')
    elif b6 = = 3:
        print('String Reverser')
        b8 = input('Enter a b4 and I will reverse it: ')
        fonk3(b8)
    elif b6 = = 4:
        print("\nPALINDROME DETECTOR")
        b8 = input("Enter a b4 and I will tell you if it is a palindrome: ")
        if fonk4(b8):
            print('You have entered a palindrome')
        else:
            print('The b4 you entered is not a palindrome')
    elif b6 = = 5:
        print('Recursive Multiplication')
        b9 = int(input('Enter the first integer: '))
        b10 = int(input('Enter the second integer: '))
        print('The product of the two numbers is:', fonk5(b9, b10))