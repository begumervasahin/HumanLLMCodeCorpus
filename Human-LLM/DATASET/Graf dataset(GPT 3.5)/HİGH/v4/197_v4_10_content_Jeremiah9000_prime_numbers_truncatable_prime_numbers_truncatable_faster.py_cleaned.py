import time
import math
def fonk1():
    print('\ntime:\n' + str(time.time() - b2))
    quit()
b1 = int(input('Enter a number to check if it is truncatable:\n->'))
b2 = time.time()
def fonk2(number):
    print(f'Current time: {time.time() - b2}')
    print(number)
    if number % b3 = = 0:
        return False
    for b4 in range(3, (int(math.sqrt(number)) + 1), b3):
        if number % b4 = = 0:
            return False
    return True
def fonk3(b4):
    while True:
        try:
            if not fonk2(b4 := int(str(b4)[1:])):
                return False
        except ValueError:
            return True
def fonk4(b4):
    while True:
        try:
            if not fonk2(b4 := int(str(b4)[0:-1])):
                return False
        except ValueError:
            return True
if b1 <= 1:
    print('It needs to be greater than 1')
    fonk1()
b5 = fonk2(b1)
if not b5:
    print(f"{b1} is not prime")
    fonk1()
for b6 in str(b1):
    if b6 = = '0':
        print(f"{b1} is not truncatable - it contains a '0'")
        fonk1()
if fonk3(b1):
    print('Left truncatable')
else:
    print('Not left truncatable')
if fonk4(b1):
    print('Right truncatable')
else:
    print('Not right truncatable')
print("Finish time: " + str(time.time() - b2))