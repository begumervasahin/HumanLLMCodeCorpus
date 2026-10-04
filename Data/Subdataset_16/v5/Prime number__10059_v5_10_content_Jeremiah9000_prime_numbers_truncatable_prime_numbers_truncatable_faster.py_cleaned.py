import time
import math
def fonk1(b5):
    return time.time() - b5
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
    b4 = str(b3)
    while b4:
        if not fonk2(int(b4)):
            return False
        b4 = b4[1:]
    return True
def fonk4(b3):
    b4 = str(b3)
    while b4:
        if not fonk2(int(b4)):
            return False
        b4 = b4[:-1]
    return True
def fonk5():
    b1 = int(input('Enter a b1 to check if it is truncatable: \n-> '))
    b5 = time.time()
    if b1 <= 1:
        print('The b1 must be greater than 1.')
        print(f'Elapsed time: {fonk1(b5):.2f} seconds')
        return
    if not fonk2(b1):
        print(f"{b1} is not a prime b1.")
        print(f'Elapsed time: {fonk1(b5):.2f} seconds')
        return
    if '0' in str(b1):
        print(f"{b1} is not truncatable because it contains a '0'.")
        print(f'Elapsed time: {fonk1(b5):.2f} seconds')
        return
    if fonk3(b1):
        print(f'{b1} is a left-truncatable prime.')
    else:
        print(f'{b1} is not a left-truncatable prime.')
    if fonk4(b1):
        print(f'{b1} is a right-truncatable prime.')
    else:
        print(f'{b1} is not a right-truncatable prime.')
    print(f"Total elapsed time: {fonk1(b5):.2f} seconds")
if b6 = = "__main__":
    fonk5()