from itertools import accumulate, count
from exceed import until_exceeded
from time import sleep
def fonk1(n):
    return n * (n + 1)
def fonk2(n):
    return sum(range(1, n + 1))
def fonk3():
    return accumulate(count(1))
def fonk4(b2):
    b1 = None
    for triangle in until_exceeded(b2, fonk3()):
        b1 = triangle
    return b2 = = b1
if b3 = = "__main__":
    print('Triangle Numbers (Ctrl-C to Exit):')
    try:
        for triangle_num in fonk3():
            print(triangle_num)
            sleep(0.42)
    except KeyboardInterrupt:
        print('\nProgram terminated by user.')