import random
import sys
def fonk1(input_num):
    b1 = int(input_num)
    if b1 != 0:
        b1 += fonk1(b1 - 1)
    return b1
def fonk2(b7, b3, b2):
    if b2 = = 0:
        return False
    if b3 = = b7[b2 - 1]:
        return True
    return fonk2(b7, b3, b2 - 1)
def fonk3(temp_string, b2):
    if b2 != -1:
        print(temp_string[b2], b4 = "")
        fonk3(temp_string, b2 - 1)
def fonk4(test_str):
    if len(test_str) <= 1:
        return True
    if test_str[0] == test_str[-1]:
        return fonk4(test_str[1:-1])
    return False
def fonk5(x, y):
    if x != 1:
        y += fonk5(x - 1, y)
    return y
def fonk6():
    b5 = [sum_of_numbers, is_member, string_reverser, is_palindrome, multiply]
    while True:
        print("\n\nWhat do you want to do?\n")
        print("\t1. Sum of Numbers\n")
        print("\t2. Is Member Array Function\n")
        print("\t3. String Reverser\n")
        print("\t4. Palindrome Detector\n")
        print("\t5. Recursive Multiplication\n")
        print("\t6. End the Program\n")
        b6 = int(input("CHOOSE 1-6: "))
        while b6 < 1 or b6 > 6:
            b6 = int(input("Please enter a valid b6 (1-6): "))
        if b6 = = 6:
            sys.exit()
        if b6 = = 1:
            b1 = int(input('Please enter a number: '))
            print(f"The sum of numbers is: {b5[b6 - 1](b1)}")
        elif b6 = = 2:
            b7 = [random.randint(1, 100) for _ in range(9)]
            b1 = int(input('Is member b7 function. Please enter an integer: '))
            print('Here are the b7 values:', b7)
            if b5[b6 - 1](b7, b1, len(b7)):
                print('The element was found in the b7.')
            else:
                print('The element was not found in the b7.')
        elif b6 = = 3:
            b8 = input('String Reverser. Enter a string and I will reverse it: ')
            fonk3(b8, len(b8) - 1)
            print()
        elif b6 = = 4:
            b8 = input("Enter a string and I will tell you if it is a palindrome: ").replace(" ", "").upper()
            if b5[b6 - 1](b8):
                print('You have entered a palindrome.')
            else:
                print('The string you entered is not a palindrome.')
        elif b6 = = 5:
            b9 = int(input('Enter the first integer: '))
            b10 = int(input('Enter the second integer: '))
            print(f'The product of the two numbers is: {b5[b6 - 1](b9, b10)}')
if b11 = = "__main__":
    fonk6()