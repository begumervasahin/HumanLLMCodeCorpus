import time
import math
def fonk1(b5):
    print('\ntime:\n' + str(time.time() - b5))
    quit()
def fonk2(number):
    print(f'current time: {time.time() - b5}')
    print(number)
    if number % b1 = = 0:
        return False
    for b2 in range(3, (int(math.sqrt(number)) + 1), b1):
        if number % b2 = = 0:
            return False
    return True
def fonk3(b2):
    while True:
        try:
            if not fonk2(b2 := int(str(b2)[1:])):
                return False
        except ValueError:
            return True
def fonk4(b2):
    while True:
        try:
            if not fonk2(b2 := int(str(b2)[0:-1])):
                return False
        except ValueError:
            return True
if b3 = = '__main__':
    b4 = int(input('enter number to see if it is truncatable: \n->'))
    b5 = time.time()
    if b4 <= 1:
        print('It needs to be greater than 1')
        fonk1(b5)
    b6 = fonk2(b4)
    if not b6:
        print(f"{b4} is not prime")
        fonk1(b5)
    for b7 in str(b4):
        if b7 = = '0':
            print(f"{b4} not truncatable - contains a '0'")
            fonk1(b5)
    if fonk3(b4):
        print('left truncatable')
    else:
        print('not left truncatable')
    if fonk4(b4):
        print('right truncatable')
    else:
        print('not right truncatable')
    print("finish time: " + str(time.time() - b5))