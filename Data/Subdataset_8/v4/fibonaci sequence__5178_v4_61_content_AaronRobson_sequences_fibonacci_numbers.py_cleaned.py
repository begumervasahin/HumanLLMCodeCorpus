from itertoolsrecipes import take
from decorators import memoised
def _fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
def fibonacci_numbers(n=None):
    if n is not None:
        return take(n, _fibonacci())
    else:
        return _fibonacci()
@memoised
def fibonacci_number(num):
    if num < 0:
        raise ValueError('Fibonacci numbers are not defined for negative numbers.')
    if num < 2:
        return num
    else:
        return fibonacci_number(num - 1) + fibonacci_number(num - 2)
if __name__ == "__main__":
    print('Fibonacci Sequence:\n')
    print('First Few:')
    for num in fibonacci_numbers(13):
        print(num)
    print('\nInfinite (Ctrl-C to exit):')
    from time import sleep
    for num in fibonacci_numbers():
        print(num)
        sleep(0.42)