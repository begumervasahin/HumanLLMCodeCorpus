import random
import sys
def fonk1(b4):
    if b4 != 0:
        return b4 + fonk1(b4 - 1)
    return b4
def fonk2(b5, b1, size):
    if size != 0:
        if b1 = = b5[size - 1]:
            return True
        else:
            return fonk2(b5, b1, size - 1)
    return False
def fonk3(temp_string, size):
    if size != -1:
        print(temp_string[size], b2 = "")
        fonk3(temp_string, size - 1)
def fonk4(test_str):
    if len(test_str) == 1:
        return True
    if test_str[0] == test_str[-1]:
        return fonk4(test_str[1:-1])
    return False
def fonk5(x, y):
    if x != 1:
        return y + fonk5(x - 1, y)
    return y
def fonk6():
    print("\n\nWhat do you want to do?\n")
    print("\t1.  Sum of Numbers")
    print("\t2.  IsMember Array Function")
    print("\t3.  String Reverser")
    print("\t4.  Palindrome Detector")
    print("\t5.  Recursive Multiplication")
    print("\t6.  End the Program")
    print("CHOOSE 1-6:  ")
def fonk7():
    while True:
        fonk6()
        b3 = int(input())
        while b3 < 1 or b3 > 6:
            print('Input valid b3 1-6')
            b3 = int(input())
        if b3 = = 6:
            sys.exit()
        if b3 = = 1:
            print('Please enter a number')
            b4 = int(input())
            print("Sum of Numbers:", fonk1(b4))
        elif b3 = = 2:
            b5 = [random.randint(1, 100) for _ in range(9)]
            print('IsMember Array Function')
            print('Please enter an integer')
            b4 = int(input())
            print('Here are the b5 values:')
            print(b5)
            if fonk2(b5, b4, len(b5)):
                print('The element was found in the b5')
            else:
                print('The element was not found in the b5')
        elif b3 = = 3:
            print('String Reverser')
            print('Enter a string and I will reverse it:')
            b6 = input()
            fonk3(b6, len(b6) - 1)
            print()
        elif b3 = = 4:
            print("\n\nPalindrome Detector\n")
            print("Enter a string and I will tell you if it is a palindrome:")
            b6 = input().upper().replace(" ", "")
            if fonk4(b6):
                print('You have entered a palindrome')
            else:
                print('The string you entered is not a palindrome')
        elif b3 = = 5:
            print('Recursive Multiplication')
            print('Enter the first integer:')
            b7 = int(input())
            print('Enter the second integer:')
            b8 = int(input())
            print('The product of the two numbers is:', fonk5(b7, b8))
if b9 = = '__main__':
    fonk7()