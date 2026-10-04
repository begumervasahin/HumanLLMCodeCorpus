import random
import sys
def fonk1(b3):
    if b3 != 0:
        return b3 + fonk1(b3 - 1)
    return b3
def fonk2(b4, b1, size):
    if size != 0:
        if b1 = = b4[size - 1]:
            return True
        else:
            return fonk2(b4, b1, size - 1)
    return False
def fonk3(temp_string, size):
    if size != -1:
        print(temp_string[size], b2 = "")
        fonk3(temp_string, size - 1)
def fonk4(test_str):
    if len(test_str) <= 1:
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
    print("\t1. Sum of Numbers")
    print("\t2. IsMember Array Function")
    print("\t3. String Reverser")
    print("\t4. Palindrome Detector")
    print("\t5. Recursive Multiplication")
    print("\t6. End the Program")
    print("CHOOSE 1-6:  ")
def fonk7():
    print('Please enter a number:')
    b3 = int(input())
    print("Sum of Numbers:", fonk1(b3))
def fonk8():
    b4 = [random.randint(1, 100) for _ in range(9)]
    print('IsMember Array Function')
    print('Please enter an integer:')
    b3 = int(input())
    print('Here are the b4 values:')
    print(b4)
    if fonk2(b4, b3, len(b4)):
        print('The element was found in the b4')
    else:
        print('The element was not found in the b4')
def fonk9():
    print('String Reverser')
    print('Enter a string and I will reverse it:')
    b5 = input()
    fonk3(b5, len(b5) - 1)
    print()
def fonk10():
    print("\n\nPalindrome Detector\n")
    print("Enter a string and I will tell you if it is a palindrome:")
    b5 = input().upper().replace(" ", "")
    if fonk4(b5):
        print('You have entered a palindrome')
    else:
        print('The string you entered is not a palindrome')
def fonk11():
    print('Recursive Multiplication')
    print('Enter the first integer:')
    b6 = int(input())
    print('Enter the second integer:')
    b7 = int(input())
    print('The product of the two numbers is:', fonk5(b6, b7))
def fonk12():
    while True:
        fonk6()
        b8 = int(input())
        while b8 < 1 or b8 > 6:
            print('Input valid b8 1-6:')
            b8 = int(input())
        if b8 = = 6:
            sys.exit()
        if b8 = = 1:
            fonk7()
        elif b8 = = 2:
            fonk8()
        elif b8 = = 3:
            fonk9()
        elif b8 = = 4:
            fonk10()
        elif b8 = = 5:
            fonk11()
if b9 = = '__main__':
    fonk12()