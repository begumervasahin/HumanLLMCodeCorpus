import random
import sys
def sum_of_numbers(input_num):
    num = int(input_num)
    if num != 0:
        num += sum_of_numbers(num - 1)
    return num
def is_member(array, value, size):
    if size != 0:
        if value == array[size]:
            return True
        else:
            is_member(array, value, size - 1)
        if size == 0:
            return False
def string_reverser(temp_string, size):
    if size != -1:
        print(temp_string[size], end=" ")
        string_reverser(temp_string, size - 1)
def is_palindrome(test_str):
    if len(test_str) == 1:
        return True
    if test_str[0] == test_str[len(test_str) - 1]:
        is_palindrome(test_str[0:len(test_str) - 2])
        return True
    return False
def multiply(x, y):
    if x != 1:
        y += multiply(x - 1, y)
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
    choice = int(input())
    while choice < 1 or choice > 6:
        print('Input valid choice 1-6')
        choice = int(input())
    if choice == 6:
        sys.exit()
    if choice == 1:
        print('Please enter a number')
        print("\n\nSUM OF NUMBERS\n")
        num = int(input())
        print(sum_of_numbers(num))
    elif choice == 2:
        array = []
        for i in range(9):
            array = array + [random.randint(1, 100)]
        print('Is member array function')
        print('Please enter an integer')
        num = int(input())
        print('Here are the array values')
        for i in range(len(array)):
            print(array[i])
        if is_member(array, num, len(array) - 1):
            print('The element was found in the array')
        else:
            print('The element was not found in the array')
    elif choice == 3:
        print('String Reverser')
        print('Enter a string and I will reverse it: ')
        user_string = input()
        string_reverser(user_string, len(user_string) - 1)
    elif choice == 4:
        print("\n\nPALINDROME DETECTOR\n")
        print("Enter a string and I will tell you if it is a palindrome:  ")
        user_string = input()
        user_string.upper()
        user_string.replace(" ", "")
        if is_palindrome(user_string) == 1:
            print('You have entered a palindrome')
        else:
            print('The string you entered is not a palindrome')
    elif choice == 5:
        print('Recursive Multiplication')
        print('Enter the first integer')
        num1 = int(input())
        print('Enter the second integer')
        num2 = int(input())
        print('The product of the two numbers is:', end=" ")
        print(multiply(num1, num2))