'''
Requirements Specification:
    Write a program find all perfect numbers below 10,000.
    Time the program.
System Analysis:
    Formulas:
        number % a1
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
b1 = time.clock()
for number in range(1, 10000):
    b2 = []
    a1 = 1
    while a1 < number:
        if number % a1 = = 0:
            b2.append(a1)
        a1 += 1
    if sum(b2) == number:
        print(number)
print(time.clock() - b1, "seconds")
'''
Test:
    Only needs to do one test since there is not input.
    Output:
        6
        28
        496
        8128
'''