import random
import sys
def fonk1(input_num):
    b1 = int(input_num)
    if b1 != 0:
        b1 += fonk1(b1 - 1)
    return b1
def fonk2(b6, b2, b3):
    if b3 != 0:
        if b2 = = b6[b3]:
            return True
        else:
            fonk2(b6, b2, b3 - 1)
        if b3 = = 0:
            return False
def fonk3(temp_string, b3):
    if b3 != -1:
        print(temp_string[b3], b4 = " ")
        fonk3(temp_string, b3 - 1)
def fonk4(test_str):
    if len(test_str) == 1:
        return True
    if test_str[0] == test_str[len(test_str) - 1]:
        fonk4(test_str[0:len(test_str) - 2])
        return True
    return False
def fonk5(x, y):
    if x != 1:
        y += fonk5(x - 1, y)
    return y
while True:
    print("\n\nWhat do you want to do?\n")
    print("\t1.  Sum of Numbers\n")
    print("\t2.  IsMember Array Function\n")
    print("\t3.  String Reverser\n")
    print("\t4.  Palindrome Detector\n")
    print("\t5.  Recursive Multiplication\n")
    print("\t6.  End the Program\n")
    print("CHOOSE 1-6:  ")
    b5 = int(input())
    while b5 < 1 or b5 > 6:
        print('Input valid b5 1-6')
        b5 = int(input())
    if b5 = = 6:
        sys.exit()
    if b5 = = 1:
        print('Please enter a number')
        print("\n\nSUM OF NUMBERS\n")
        b1 = int(input())
        print(fonk1(b1))
    elif b5 = = 2:
        b6 = []
        for i in range(9):
            b6 = b6 + [random.randint(1, 100)]
        print('Is member b6 function')
        print('Please enter an integer')
        b1 = int(input())
        print('Here are the b6 values')
        for i in range(len(b6)):
            print(b6[i])
        if fonk2(b6, b1, len(b6) - 1):
            print('The element was found in the b6')
        else:
            print('The element was not found in the b6')
    elif b5 = = 3:
        print('String Reverser')
        print('Enter a string and I will reverse it: ')
        b7 = input()
        fonk3(b7, len(b7) - 1)
    elif b5 = = 4:
        print("\n\nPALINDROME DETECTOR\n")
        print("Enter a string and I will tell you if it is a palindrome:  ")
        b7 = input()
        b7.upper()
        b7.replace(" ", "")
        if fonk4(b7) == 1:
            print('You have entered a palindrome')
        else:
            print('The string you entered is not a palindrome')
    elif b5 = = 5:
        print('Recursive Multiplication')
        print('Enter the first integer')
        b8 = int(input())
        print('Enter the second integer')
        b9 = int(input())
        print('The product of the two numbers is:', b4 = " ")
        print(fonk5(b8, b9))