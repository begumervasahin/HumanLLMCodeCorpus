import time
import math
def fonk1(b5):
    print(f'\nTime elapsed: {time.time() - b5} seconds')
    quit()
def fonk2(b1, b5):
    print(f'Current time: {time.time() - b5} seconds')
    print(f'Checking: {b1}')
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
def fonk3(b3, b5):
    while len(str(b3)) > 1:
        b3 = int(str(b3)[1:])
        if not fonk2(b3, b5):
            return False
    return True
def fonk4(b3, b5):
    while len(str(b3)) > 1:
        b3 = int(str(b3)[:-1])
        if not fonk2(b3, b5):
            return False
    return True
def fonk5():
    b4 = int(input('Enter a b1 to see if it is truncatable: \n-> '))
    b5 = time.time()
    if b4 <= 1:
        print('The b1 needs to be greater than 1')
        fonk1(b5)
    if not fonk2(b4, b5):
        print(f"{b4} is not prime")
        fonk1(b5)
    if '0' in str(b4):
        print(f"{b4} is not truncatable - contains a '0'")
        fonk1(b5)
    if fonk3(b4, b5):
        print('Left truncatable')
    else:
        print('Not left truncatable')
    if fonk4(b4, b5):
        print('Right truncatable')
    else:
        print('Not right truncatable')
    print(f"Finish time: {time.time() - b5} seconds")
if b6 = = "__main__":
    fonk5()