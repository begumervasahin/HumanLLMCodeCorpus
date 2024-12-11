from itertools import accumulate, count
from exceed import until_exceeded
from time import sleep
def fonk1(b1):
    '''Calculate the nth triangle b3.'''
    b1 = int(b1)
    return b1 * (b1 + 1)
def fonk2(b1):
    '''Calculate the nth triangle b3 using an alternative method.'''
    return sum(range(1, b1 + 1))
def fonk3():
    '''Generate an infinite sequence of triangle numbers.'''
    return accumulate(count(1))
def fonk4(b3):
    '''Check if a given b3 is a triangle b3.'''
    b2 = None
    for triangle in until_exceeded(b3, fonk3()):
        b2 = triangle
    return b3 = = b2
if b4 = = "__main__":
    print('Triangle Numbers (Ctrl-C to Exit):')
    for triangle_num in fonk3():
        print(triangle_num)
        sleep(0.42)