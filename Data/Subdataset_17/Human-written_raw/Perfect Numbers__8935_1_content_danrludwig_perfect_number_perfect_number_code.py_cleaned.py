'''
Requirements Specification:
    Write a program find all perfect numbers below 10,000.
    Time the program.
System Analysis:
    Formulas:
        number % divisor
System Design:
    Input:
        Nothing
    Calculate:
        If the sum of all the divisors of the number equals the original number.
        Set time when started. Minus current time from when started to get how long the program took to run.
    Print:
        All the perfect numbers.
        Time it took to do the calculation.
'''
import time
start = time.clock()
for number in range(1, 10000):
    divisor_list = []
    divisor = 1
    while divisor < number:
        if number % divisor == 0:
            divisor_list.append(divisor)
        divisor += 1
    if sum(divisor_list) == number:
        print(number)
print(time.clock() - start, "seconds")
'''
Test:
    Only needs to do one test since there is not input.
    Output:
        6
        28
        496
        8128
'''