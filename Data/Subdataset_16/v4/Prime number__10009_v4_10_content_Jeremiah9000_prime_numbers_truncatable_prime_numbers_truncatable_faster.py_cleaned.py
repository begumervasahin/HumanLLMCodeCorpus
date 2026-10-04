import time
import math
def fonk1():
    print('\nElapsed time: ' + str(time.time() - b5))
    quit()
def fonk2(b2):
    print(f'Current time: {time.time() - b5}')
    print(b2)
    if b2 <= 1:
        return False
    if b2 % b1 = = 0:
        return b2 = = b1
    for b3 in range(3, int(math.sqrt(b2)) + 1, b1):
        if b2 % b3 = = 0:
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
def fonk5():
    b4 = int(input('Enter a b2 to see if it is truncatable: \n-> '))
    global b5
    b5 = time.time()
    if b4 <= 1:
        print('The b2 needs to be greater than 1.')
        fonk1()
    if not fonk2(b4):
        print(f"{b4} is not prime.")
        fonk1()
    if '0' in str(b4):
        print(f"{b4} is not truncatable - contains a '0'.")
        fonk1()
    if fonk3(b4):
        print('Left truncatable.')
    else:
        print('Not left truncatable.')
    if fonk4(b4):
        print('Right truncatable.')
    else:
        print('Not right truncatable.')
    print("Finish time: " + str(time.time() - b5))
if b6 = = "__main__":
    fonk5()