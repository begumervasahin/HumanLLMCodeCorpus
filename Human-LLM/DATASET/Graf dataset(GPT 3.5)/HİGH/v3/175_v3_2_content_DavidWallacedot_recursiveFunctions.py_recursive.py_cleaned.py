import random
import sys
def fonk1(b1):
    if b1 = = 0:
        return 0
    return b1 + fonk1(b1 - 1)
def fonk2(b6, b2):
    if not b6:
        return False
    if b2 = = b6[-1]:
        return True
    return fonk2(b6[:-1], b2)
def fonk3(b7):
    if not b7:
        return
    print(b7[-1], b3 = " ")
    fonk3(b7[:-1])
def fonk4(test_str):
    if len(test_str) <= 1:
        return True
    if test_str[0] != test_str[-1]:
        return False
    return fonk4(test_str[1:-1])
def fonk5(b4, y):
    if b4 = = 1:
        return y
    return y + fonk5(b4 - 1, y)
while True:
    print("\n\nWhat do you want to do?\n")
    print("\t1. Sum of Numbers\n")
    print("\t2. IsMember Array Function\n")
    print("\t3. String Reverser\n")
    print("\t4. Palindrome Detector\n")
    print("\t5. Recursive Multiplication\n")
    print("\t6. End the Program\n")
    print("CHOOSE 1-6:  ")
    b5 = int(input())
    while b5 < 1 or b5 > 6:
        print('Input a valid b5 (1-6)')
        b5 = int(input())
    if b5 = = 6:
        sys.exit()
    if b5 = = 1:
        print('\n\nSUM OF NUMBERS\n')
        b1 = int(input('Please enter a number: '))
        print(fonk1(b1))
    elif b5 = = 2:
        b6 = [random.randint(1, 100) for _ in range(9)]
        print('\nIs member b6 function\n')
        b1 = int(input('Please enter an integer: '))
        print('Here are the b6 values:')
        for val in b6:
            print(val)
        if fonk2(b6, b1):
            print('The element was found in the b6')
        else:
            print('The element was not found in the b6')
    elif b5 = = 3:
        print('\nString Reverser\n')
        b7 = input('Enter a string and I will reverse it: ')
        fonk3(b7)
    elif b5 = = 4:
        print("\n\nPALINDROME DETECTOR\n")
        b7 = input("Enter a string and I will tell you if it is a palindrome: ").upper().replace(" ", "")
        if fonk4(b7):
            print('You have entered a palindrome')
        else:
            print('The string you entered is not a palindrome')
    elif b5 = = 5:
        print('\nRecursive Multiplication\n')
        b8 = int(input('Enter the first integer: '))
        b9 = int(input('Enter the second integer: '))
        print('The product of the two numbers is:', b3 = " ")
        print(fonk5(b8, b9)))