from itertools import accumulate, count
from exceed import until_exceeded
from time import sleep
def triangle_number(n):
    return n * (n + 1)
def triangle_number_alt(n):
    return sum(range(1, n + 1))
def generate_triangle_numbers():
    return accumulate(count(1))
def is_triangle_number(number):
    last_triangle = None
    for triangle in until_exceeded(number, generate_triangle_numbers()):
        last_triangle = triangle
    return number == last_triangle
if __name__ == "__main__":
    print('Triangle Numbers (Ctrl-C to Exit):')
    try:
        for triangle_num in generate_triangle_numbers():
            print(triangle_num)
            sleep(0.42)
    except KeyboardInterrupt:
        print('\nProgram terminated by user.')