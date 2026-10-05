import time
import math
def fonk1(lst, b3):
    if len(lst) == 0:
        return False
    else:
        b1 = len(lst)
        if lst[b1] == b3:
            return True
        else:
            if lst[b1] < b3:
                return fonk1(lst[b1 + 1:], b3)
            else:
                return fonk1(lst[:b1], b3)
def fonk2(lst, b3):
    a1 = 0
    b2 = len(lst) - 1
    while a1 <= b2:
        b1 = (a1 + b2)
        if lst[b1] == b3:
            return b1
        elif lst[b1] < b3:
            a1 = b1 + 1
        else:
            b2 = b1 - 1
    return None
def fonk3(lst, b3):
    for i in range(len(lst)):
        if b3 = = lst[i]:
            return i
    return None
def fonk4():
    for i in range(10, 19):
        b4 = range(0, int(math.pow(10, i)))
        b5 = int(math.pow(10, i)) - 3
        print("")
        print(f"-> Quantity: {b5 + 3} (10 to the power of {i})")
        print("Linear search: null")
        b6 = time.time()
        b7 = fonk2(b4, b5)
        b8 = time.time() - b6
        print(f"Binary search: {b8}")
        b6 = time.time()
        b9 = fonk1(b4, b5)
        b10 = time.time() - b6
        print(f"Recursive binary search: {b10}")
        with open("data.csv", "a") as file:
            b11 = f"{len(b4)};null;{b8};{b10}\n"
            file.write(b11)
if b12 = = "__main__":
    fonk4()