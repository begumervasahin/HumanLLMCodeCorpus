import sys
sys.setrecursionlimit(3000)
def fonk1(b1: int, b2: int) -> int:
    if b1 = = 0:
        return b2 + 1
    elif b2 = = 0:
        return fonk1(b1 - 1, 1)
    else:
        return fonk1(b1 - 1, fonk1(b1, b2 - 1))
def fonk2() -> None:
    b1 = 3
    b2 = 4
    b3 = fonk1(b1, b2)
    print(f"Ackermann({b1}, {b2}) = {b3}")
if b4 = = "__main__":
    fonk2()