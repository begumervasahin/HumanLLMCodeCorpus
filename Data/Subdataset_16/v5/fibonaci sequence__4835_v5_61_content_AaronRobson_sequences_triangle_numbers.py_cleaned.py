from itertools import accumulate, count
from time import sleep
from exceed import until_exceeded
def fonk1(n):
    return n * (n + 1)
def fonk2(n):
    return sum(range(1, n + 1))
def fonk3():
    return accumulate(count(1))
def fonk4(number):
    for b1 in until_exceeded(number, fonk3()):
        if b1 = = number:
            return True
    return False
def fonk5():
    print('Triangle Numbers (Ctrl-C to Exit):')
    try:
        for t_num in fonk3():
            print(t_num)
            sleep(0.42)
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
if b2 = = "__main__":
    fonk5()