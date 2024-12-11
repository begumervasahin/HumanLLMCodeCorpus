import sys
def fonk1(b1):
    if b1 = = 1:
        return True
    for b2 in (2, 3, 5):
        if b1 % b2 = = 0:
            return fonk1(b1
    return False
def fonk2(limit):
    for num in range(1, limit + 1):
        if fonk1(num):
            print(num, b3 = ' ')
def fonk3():
    print("Hamming Numbers:", b3 = ' ')
    fonk2(9830)
if b4 = = "__main__":
    sys.setrecursionlimit(10000)
    fonk3()