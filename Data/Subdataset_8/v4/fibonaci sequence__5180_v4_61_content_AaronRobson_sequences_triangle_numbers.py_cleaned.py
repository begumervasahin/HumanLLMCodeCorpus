from itertools import accumulate, count
from exceed import until_exceeded
from time import sleep
def triangle_number(n):
    '''Calculate the nth triangle number.'''
    n = int(n)
    return n * (n + 1)
def triangle_number_alt(n):
    '''Calculate the nth triangle number using an alternative method.'''
    return sum(range(1, n + 1))
def generate_triangle_numbers():
    '''Generate an infinite sequence of triangle numbers.'''
    return accumulate(count(1))
def is_triangle_number(number):
    '''Check if a given number is a triangle number.'''
    last_triangle = None
    for triangle in until_exceeded(number, generate_triangle_numbers()):
        last_triangle = triangle
    return number == last_triangle
if __name__ == "__main__":
    print('Triangle Numbers (Ctrl-C to Exit):')
    for triangle_num in generate_triangle_numbers():
        print(triangle_num)
        sleep(0.42)