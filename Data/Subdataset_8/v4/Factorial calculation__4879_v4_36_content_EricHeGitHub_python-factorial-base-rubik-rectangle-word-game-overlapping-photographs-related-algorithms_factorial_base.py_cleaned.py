from sys import exit
import time
from itertools import product
def factorial(n):
    result = 1
    for i in range(n):
        result *= i + 1
    return result
def list_to_integer(lst):
    result = 0
    power = len(lst) - 1
    for digit in lst:
        if not str(digit).isdigit():
            return None
        else:
            result += digit * 10 ** power
            power -= 1
    return result
number = input('Input a nonnegative integer: ')
if not number.isdigit() or number[0] == '0':
    print('Incorrect input, giving up...')
    exit()
number = int(number)
Max = 1
while factorial(Max) <= number:
    Max += 1
Max -= 1
middle_result = 0
factorial_results = []
number_display = number
while number:
    for i in range(Max, 0, -1):
        while middle_result * factorial(i) < number:
            middle_result += 1
        if middle_result * factorial(i) > number:
            middle_result -= 1
        else:
            pass
        factorial_results.append(middle_result)
        number -= middle_result * factorial(i)
        middle_result = 0
print('Decimal {} reads as {} in factorial base.'.format(number_display, list_to_integer(factorial_results)))