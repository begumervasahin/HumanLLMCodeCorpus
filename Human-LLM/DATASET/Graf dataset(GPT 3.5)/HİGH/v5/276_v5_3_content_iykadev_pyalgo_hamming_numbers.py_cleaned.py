import sys
sys.setrecursionlimit(10000)
def fonk1(b1):
    if b1 = = 1:
        return True
    if b1 % b2 = = 0:
        return fonk1(b1
    if b1 % b3 = = 0:
        return fonk1(b1
    if b1 % b4 = = 0:
        return fonk1(b1
    return False
def fonk2(limit):
    for num in range(1, limit + 1):
        if fonk1(num):
            print(num, b5 = ' ')
def fonk3():
    sys.stdout.write("Hamming Numbers: ")
    fonk2(9830)
if b6 = = "__main__":
    fonk3()