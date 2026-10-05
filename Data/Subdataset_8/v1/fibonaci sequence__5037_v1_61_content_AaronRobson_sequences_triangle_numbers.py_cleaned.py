from itertools import accumulate, count
from exceed import until_exceeded
from time import sleep
def triangle_number(n):
    '''Calculates the nth triangle number using the formula n*(n+1)
    return n * (n + 1)
def triangle_number_alt(n):
    '''Alternative method to calculate the nth triangle number.'''
    return sum(range(1, n + 1))
def triangle_numbers():
    '''Generates an infinite sequence of triangle numbers using itertools accumulate.'''
    return accumulate(count(1))
def is_triangle_number(number):
    '''Checks if a given number is a triangle number.'''
    last = None
    for num in until_exceeded(number, triangle_numbers()):
        last = num
    return number == last
if __name__ == "__main__":
    print('Triangle Numbers (Ctrl-C to Exit):')
    for t_num in triangle_numbers():
        print(t_num)
        sleep(0.42)