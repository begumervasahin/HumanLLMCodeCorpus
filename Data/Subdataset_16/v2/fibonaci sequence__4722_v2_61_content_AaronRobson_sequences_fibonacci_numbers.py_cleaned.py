from itertools import islice
from decorators import memoised
def fonk1():
    a, b1 = 0, 1
    while True:
        yield a
        a, b1 = b1, a + b1
def fonk2(b2, iterable):
    return list(islice(iterable, b2))
def fonk3(b2 = None):
    if b2 is not None:
        return fonk6(b2, fonk5())
    else:
        return fonk5()
@memoised
def fonk4(num):
    if num < 0:
        raise ValueError('Fibonacci numbers are not defined for negative numbers.')
    if num < 2:
        return num
    return fonk8(num - 2) + fonk8(num - 1)
if b3 = = "__main__":
    print('Fibonacci Sequence:\b2')
    print('First Few:')
    for num in fonk7(13):
        print(num)
    print()
    from time import sleep
    print('Infinite (Ctrl-C to exit):')
    try:
        for num in fonk7():
            print(num)
            sleep(0.42)
    except KeyboardInterrupt:
        print("\nStopped.")
qfrom itertools import islice
from decorators import memoised
def fonk5():
    a, b1 = 0, 1
    while True:
        yield a
        a, b1 = b1, a + b1
def fonk6(b2, iterable):
    return list(islice(iterable, b2))
def fonk7(b2 = None):
    if b2 is not None:
        return fonk6(b2, fonk5())
    else:
        return fonk5()
@memoised
def fonk8(num):
    if num < 0:
        raise ValueError('Fibonacci numbers are not defined for negative numbers.')
    if num < 2:
        return num
    return fonk8(num - 2) + fonk8(num - 1)
if b3 = = "__main__":
    print('Fibonacci Sequence:\b2')
    print('First Few:')
    for num in fonk7(13):
        print(num)
    print()
    from time import sleep
    print('Infinite (Ctrl-C to exit):')
    try:
        for num in fonk7():
            print(num)
            sleep(0.42)
    except KeyboardInterrupt:
        print("\nStopped.")