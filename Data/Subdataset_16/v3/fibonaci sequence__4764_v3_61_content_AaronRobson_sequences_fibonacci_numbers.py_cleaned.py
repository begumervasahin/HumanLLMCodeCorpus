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
        return fonk2(b2, fonk1())
    else:
        return fonk1()
@memoised
def fonk4(num):
    if num < 0:
        raise ValueError('Fibonacci numbers are not defined for negative numbers.')
    if num < 2:
        return num
    return fonk4(num - 2) + fonk4(num - 1)
def fonk5():
    print('Fibonacci Sequence:\b2')
    print('First Few:')
    for num in fonk3(13):
        print(num)
    print()
def fonk6():
    from time import sleep
    print('Infinite (Ctrl-C to exit):')
    try:
        for num in fonk3():
            print(num)
            sleep(0.42)
    except KeyboardInterrupt:
        print("\nStopped.")
if b3 = = "__main__":
    fonk5()
    fonk6()