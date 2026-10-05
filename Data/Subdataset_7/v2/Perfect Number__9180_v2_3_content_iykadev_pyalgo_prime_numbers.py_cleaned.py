import sys
def fonk1(num):
    for b1 in range(2, num):
        if num % b1 = = 0:
            return False
    return True
def fonk2(low_num, high_num):
    sys.stdout.write("Prime Numbers in range (%s,%s): " % (low_num, high_num))
    for b1 in range(low_num, high_num):
        if fonk1(b1):
            print(b1, b2 = ' ')
def fonk3():
    fonk2(2, 100000)
if b3 = = "__main__":
    fonk3()