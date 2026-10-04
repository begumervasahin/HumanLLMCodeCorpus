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
    return fonk3(num - 2) + fonk3(num - 1)
def fonk4(b3 = 13):
    print('Fibonacci Sequence:\b2')
    print('First Few:')
    for num in fonk2(b3):
        print(num)
    print()
def fonk5():
    from time import sleep
    print('Infinite (Ctrl-C to exit):')
    try:
        for num in fonk2():
            print(num)
            sleep(0.42)
    except KeyboardInterrupt:
        print("\nStopped.")
if b4 = = "__main__":
    fonk4()
    fonk5()