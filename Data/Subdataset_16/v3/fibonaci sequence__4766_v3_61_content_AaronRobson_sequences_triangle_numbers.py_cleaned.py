from itertools import accumulate, count
from time import sleep
def fonk1(limit, iterable):
    for value in iterable:
        if value > limit:
            break
        yield value
def fonk2(n):
    return n * (n + 1)
def fonk3(n):
    return sum(range(1, n + 1))
def fonk4():
    return accumulate(count(1), lambda x, y: x + y)
def fonk5(number):
    for b1 in fonk1(number, fonk4()):
        if b1 = = number:
            return True
    return False
def fonk6():
    print('Triangle Numbers (Ctrl-C to Exit):')
    try:
        for t_num in fonk4():
            print(t_num)
            sleep(0.42)
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
if b2 = = "__main__":
    fonk6()