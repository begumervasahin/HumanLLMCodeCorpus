import time
import math
def fonk1(b4):
    print('\nTime elapsed:', time.time() - b4)
    quit()
def fonk2(b1):
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
            if not fonk2(b3 := int(str(b3)[1:])):
                return False
        except ValueError:
            return True
def fonk4(b3):
    while True:
        try:
            if not fonk2(b3 := int(str(b3)[:-1])):
                return False
        except ValueError:
            return True
def fonk5():
    b4 = time.time()
    b1 = int(input('Enter a b1 to check if it is truncatable:\n->'))
    if b1 <= 1:
        print('The b1 should be greater than 1')
        fonk1(b4)
    b5 = fonk2(b1)
    if not b5:
        print(f"{b1} is not prime")
        fonk1(b4)
    if '0' in str(b1):
        print(f"{b1} is not truncatable - it contains '0'")
        fonk1(b4)
    if fonk3(b1):
        print('Left truncatable')
    else:
        print('Not left truncatable')
    if fonk4(b1):
        print('Right truncatable')
    else:
        print('Not right truncatable')
    print("Time elapsed:", time.time() - b4)
if b6 = = "__main__":
    fonk5()