from itertools import accumulate, count
from exceed import until_exceeded
from time import sleep
def triangle_number(n):
    '''Calculate the nth triangle number.'''
    return n * (n + 1)
def triangle_number_alt(n):
    '''Calculate the nth triangle number using an alternative method.'''
    return sum(range(1, n + 1))
def generate_triangle_numbers():
    '''Generate an infinite sequence of triangle numbers.'''
    return accumulate(count(1))
def is_triangle_number(number):
    '''Check if a given number is a triangle number.'''
    for num in until_exceeded(number, generate_triangle_numbers()):
        pass
    return number == num
if __name__ == "__main__":
    print('Triangle Numbers (Ctrl-C to Exit):')
    try:
        for t_num in generate_triangle_numbers():
            print(t_num)
            sleep(0.42)
    except KeyboardInterrupt:
        print('\nProgram terminated by user.')