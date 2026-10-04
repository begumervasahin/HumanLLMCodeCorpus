from itertools import islice
from decorators import memoised
def _fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
def take(n, iterable):
    return list(islice(iterable, n))
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
    return fibonacci_number(num - 2) + fibonacci_number(num - 1)
if __name__ == "__main__":
    print('Fibonacci Sequence:\n')
    print('First Few:')
    for num in fibonacci_numbers(13):
        print(num)
    print()
    from time import sleep
    print('Infinite (Ctrl-C to exit):')
    try:
        for num in fibonacci_numbers():
            print(num)
            sleep(0.42)
    except KeyboardInterrupt:
        print("\nStopped.")
qfrom itertools import islice
from decorators import memoised
def _fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
def take(n, iterable):
    return list(islice(iterable, n))
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
    return fibonacci_number(num - 2) + fibonacci_number(num - 1)
if __name__ == "__main__":
    print('Fibonacci Sequence:\n')
    print('First Few:')
    for num in fibonacci_numbers(13):
        print(num)
    print()
    from time import sleep
    print('Infinite (Ctrl-C to exit):')
    try:
        for num in fibonacci_numbers():
            print(num)
            sleep(0.42)
    except KeyboardInterrupt:
        print("\nStopped.")