from itertools import accumulate, count
from exceed import until_exceeded
from time import sleep
def triangle_number(n):
    return n * (n + 1)
def triangle_number_alt(n):
    return sum(range(1, n + 1))
def triangle_numbers():
    return accumulate(count(1), lambda x, y: x + y)
def is_triangle_number(number):
    last = None
    for num in until_exceeded(number, triangle_numbers()):
        last = num
    return number == last
if __name__ == "__main__":
    print('Triangle Numbers (Ctrl-C to Exit):')
    try:
        for t_num in triangle_numbers():
            print(t_num)
            sleep(0.42)
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")