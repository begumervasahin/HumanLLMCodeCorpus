import time
import math
def fonk1(lst, b6):
    if not lst:
        return False
    b1 = len(lst)
    if lst[b1] == b6:
        return True
    elif lst[b1] < b6:
        return fonk1(lst[b1 + 1:], b6)
    else:
        return fonk1(lst[:b1], b6)
def fonk2(lst, b6):
    a1 = 0
    b2 = len(lst) - 1
    while a1 <= b2:
        b1 = (a1 + b2)
        if lst[b1] == b6:
            return b1
        elif lst[b1] < b6:
            a1 = b1 + 1
        else:
            b2 = b1 - 1
    return None
def fonk3(lst, b6):
    for i, b3 in enumerate(lst):
        if b3 = = b6:
            return i
    return None
def fonk4():
    for i in range(10, 19):
        b4 = int(math.pow(10, i))
        b5 = list(range(b4))
        b6 = b4 - 3
        print(f"\n-> Quantity: {b4} (10 to the power of {i})")
        print("Linear search: null")
        b7 = time.time()
        fonk2(b5, b6)
        b8 = time.time() - b7
        print(f"Binary search: {b8:.6f} seconds")
        b7 = time.time()
        fonk1(b5, b6)
        b9 = time.time() - b7
        print(f"Recursive binary search: {b9:.6f} seconds")
        with open("data.csv", "a") as file:
            file.write(f"{b4};null;{b8:.6f};{b9:.6f}\n")
if b10 = = "__main__":
    fonk4()