import random
import sys
def sum_of_numbers(num):
    if num == 0:
        return 0
    return num + sum_of_numbers(num - 1)
def is_member(array, value):
    if not array:
        return False
    if value == array[-1]:
        return True
    return is_member(array[:-1], value)
def string_reverser(user_string):
    if not user_string:
        return
    print(user_string[-1], end=" ")
    string_reverser(user_string[:-1])
def is_palindrome(test_str):
    if len(test_str) <= 1:
        return True
    if test_str[0] != test_str[-1]:
        return False
    return is_palindrome(test_str[1:-1])
def multiply(x, y):
    if x == 1:
        return y
    return y + multiply(x - 1, y)
while True:
    print("\n\nWhat do you want to do?\n")
    print("\t1. Sum of Numbers\n")
    print("\t2. IsMember Array Function\n")
    print("\t3. String Reverser\n")
    print("\t4. Palindrome Detector\n")
    print("\t5. Recursive Multiplication\n")
    print("\t6. End the Program\n")
    print("CHOOSE 1-6:  ")
    choice = int(input())
    while choice < 1 or choice > 6:
        print('Input a valid choice (1-6)')
        choice = int(input())
    if choice == 6:
        sys.exit()
    if choice == 1:
        print('\n\nSUM OF NUMBERS\n')
        num = int(input('Please enter a number: '))
        print(sum_of_numbers(num))
    elif choice == 2:
        array = [random.randint(1, 100) for _ in range(9)]
        print('\nIs member array function\n')
        num = int(input('Please enter an integer: '))
        print('Here are the array values:')
        for val in array:
            print(val)
        if is_member(array, num):
            print('The element was found in the array')
        else:
            print('The element was not found in the array')
    elif choice == 3:
        print('\nString Reverser\n')
        user_string = input('Enter a string and I will reverse it: ')
        string_reverser(user_string)
    elif choice == 4:
        print("\n\nPALINDROME DETECTOR\n")
        user_string = input("Enter a string and I will tell you if it is a palindrome: ").upper().replace(" ", "")
        if is_palindrome(user_string):
            print('You have entered a palindrome')
        else:
            print('The string you entered is not a palindrome')
    elif choice == 5:
        print('\nRecursive Multiplication\n')
        num1 = int(input('Enter the first integer: '))
        num2 = int(input('Enter the second integer: '))
        print('The product of the two numbers is:', end=" ")
        print(multiply(num1, num2)))