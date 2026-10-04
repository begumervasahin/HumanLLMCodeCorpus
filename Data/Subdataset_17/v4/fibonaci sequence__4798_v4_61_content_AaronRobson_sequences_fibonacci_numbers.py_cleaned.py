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
    return fibonacci_number(num - 2) + fibonacci_number(num - 1)
def display_fibonacci_sequence(count=13):
    print('Fibonacci Sequence:\n')
    print('First Few:')
    for num in fibonacci_numbers(count):
        print(num)
    print()
def display_infinite_fibonacci_sequence():
    from time import sleep
    print('Infinite (Ctrl-C to exit):')
    try:
        for num in fibonacci_numbers():
            print(num)
            sleep(0.42)
    except KeyboardInterrupt:
        print("\nStopped.")
if __name__ == "__main__":
    display_fibonacci_sequence()
    display_infinite_fibonacci_sequence()