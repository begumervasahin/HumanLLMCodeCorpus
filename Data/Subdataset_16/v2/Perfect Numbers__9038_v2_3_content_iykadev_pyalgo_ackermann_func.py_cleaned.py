import sys
sys.setrecursionlimit(3000)
def fonk1(b1: int, b2: int) -> int:
    if b1 = = 0:
        return b2 + 1
    elif b2 = = 0:
        return fonk1(b1 - 1, 1)
    else:
        return fonk1(b1 - 1, fonk1(b1, b2 - 1))
if b3 = = "__main__":
    b4 = fonk1(3, 4)
    print(b4)