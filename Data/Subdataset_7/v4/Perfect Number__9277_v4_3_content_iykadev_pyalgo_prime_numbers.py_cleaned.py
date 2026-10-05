import sys
def fonk1(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True
def fonk2(low, high):
    sys.stdout.write("Prime Numbers in range (%s, %s): " % (low, high))
    for i in range(low, high):
        if fonk1(i):
            print(i, b1 = ' ')
def fonk3():
    fonk2(2, 100000)
fonk3()