import random
def find_monisen(n):
    number = 10
    p = 2
    while p < n:
        if all(number % i != 0 for i in range(2, number)):
            p += 1
        number += 1
        m = 2**p - 1
    return number - 1, m
def print_even_numbers():
    even_numbers = [i + 1 for i in range(10) if i % 2 == 0]
    print(even_numbers)
def calculate_sum():
    sumA = 0
    i = 1
    while True:
        sumA += i
        i += 1
        if sumA > 10:
            break
    print('i = {}, sum = {}'.format(i, sumA))
def print_numbers_divisible_by_3():
    i = 1
    while(i % 3):
        print(i, end=' ')
        if (i >= 10):
            break
        i += 1
def convert_base(num, base):
    if(num >= base):
        convert_base(num
    print(num % base, end=' ')
