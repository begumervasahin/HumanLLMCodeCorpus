import time
import math
def fonk1(b5):
    print('\ntime elapsed:', time.time() - b5)
    quit()
def fonk2(b1):
    print(f'Current time: {time.time() - b5}')
    print("Checking if", b1, "is prime")
    if b1 <= 1:
        return False
    if b1 = = b2:
        return True
    if b1 % b2 = = 0:
        return False
    for b3 in range(3, int(math.sqrt(b1)) + 1, b2):
        if b1 % b3 = = 0:
            return False
    return True
def fonk3(b3):
    while True:
        try:
            b3 = int(str(b3)[1:])
            if not fonk2(b3):
                return False
        except ValueError:
            return True
def fonk4(b3):
    while True:
        try:
            b3 = int(str(b3)[:-1])
            if not fonk2(b3):
                return False
        except ValueError:
            return True
if b4 = = '__main__':
    b1 = int(input('Enter a b1 to check if it is truncatable:\n->'))
    b5 = time.time()
    if b1 <= 1:
        print('The b1 must be greater than 1')
        fonk1(b5)
    if not fonk2(b1):
        print(f"{b1} is not a prime b1")
        fonk1(b5)
    if '0' in str(b1):
        print(f"{b1} is not truncatable - it contains a '0'")
        fonk1(b5)
    if fonk3(b1):
        print('Left truncatable')
    else:
        print('Not left truncatable')
    if fonk4(b1):
        print('Right truncatable')
    else:
        print('Not right truncatable')
    print("Finish time:", time.time() - b5)