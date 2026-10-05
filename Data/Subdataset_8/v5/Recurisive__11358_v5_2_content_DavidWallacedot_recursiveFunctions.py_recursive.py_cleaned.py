import random
import sys
def sum_of_numbers(num):
    if num == 0:
        return 0
    return num + sum_of_numbers(num - 1)
def is_member(array, value):
    for element in array:
        if value == element:
            return True
    return False
def reverse_string(string):
    if len(string) == 0:
        return
    print(string[-1], end=" ")
    reverse_string(string[:-1])
def is_palindrome(string):
    string = string.upper().replace(" ", "")
    if len(string) <= 1:
        return True
    if string[0] == string[-1]:
        return is_palindrome(string[1:-1])
    return False
def recursive_multiply(x, y):
    if x == 0 or y == 0:
        return 0
    return y + recursive_multiply(x - 1, y)
while True:
    print("\n\nWhat do you want to do?\n")
    print("\t1. Sum of Numbers")
    print("\t2. IsMember Array Function")
    print("\t3. String Reverser")
    print("\t4. Palindrome Detector")
    print("\t5. Recursive Multiplication")
    print("\t6. End the Program")
    print("CHOOSE 1-6: ", end=" ")
    choice = int(input())
    while choice < 1 or choice > 6:
        print('Input valid choice 1-6')
        choice = int(input())
    if choice == 6:
        sys.exit()
    if choice == 1:
        print('Please enter a number')
        num = int(input())
        print("\nSUM OF NUMBERS")
        print(sum_of_numbers(num))
    elif choice == 2:
        array = [random.randint(1, 100) for _ in range(9)]
        print('Is member array function')
        num = int(input('Please enter an integer: '))
        print('Here are the array values:')
        for element in array:
            print(element)
        if is_member(array, num):
            print('The element was found in the array')
        else:
            print('The element was not found in the array')
    elif choice == 3:
        print('String Reverser')
        user_string = input('Enter a string and I will reverse it: ')
        reverse_string(user_string)
    elif choice == 4:
        print("\nPALINDROME DETECTOR")
        user_string = input("Enter a string and I will tell you if it is a palindrome: ")
        if is_palindrome(user_string):
            print('You have entered a palindrome')
        else:
            print('The string you entered is not a palindrome')
    elif choice == 5:
        print('Recursive Multiplication')
        num1 = int(input('Enter the first integer: '))
        num2 = int(input('Enter the second integer: '))
        print('The product of the two numbers is:', recursive_multiply(num1, num2))