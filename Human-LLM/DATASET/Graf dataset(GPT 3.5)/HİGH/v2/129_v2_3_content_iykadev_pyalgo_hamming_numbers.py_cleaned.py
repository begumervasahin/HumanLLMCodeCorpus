import sys
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
def fonk2(b1):
    if b1 = = 1:
        return
    if fonk1(b1):
        print(b1, b5 = ' ')
    fonk2(b1 - 1)
def fonk3():
    sys.stdout.write("Hamming Numbers: ")
    fonk2(9830)
if b6 = = "__main__":
    sys.setrecursionlimit(10000)
    fonk3()