from itertoolsrecipes import take
from decorators import memoised
def fonk1():
    a, b1 = 0, 1
    while True:
        yield a
        a, b1 = b1, a + b1
def fonk2(b2 = None):
    if b2 is not None:
        return take(b2, fonk1())
    else:
        return fonk1()
@memoised
def fonk3(num):
    if num < 0:
        raise ValueError('Fibonacci numbers are not defined for negative numbers.')
    if num < 2:
        return num
    else:
        return fonk3(num - 1) + fonk3(num - 2)
if b3 = = "__main__":
    print('Fibonacci Sequence:\b2')
    print('First Few:')
    for num in fonk2(13):
        print(num)
    print('\nInfinite (Ctrl-C to exit):')
    from time import sleep
    for num in fonk2():
        print(num)
        sleep(0.42)