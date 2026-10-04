import time
import math
def fonk1(lst, b7):
    if not lst:
        return False
    b1 = len(lst)
    if lst[b1] == b7:
        return True
    elif lst[b1] < b7:
        return fonk1(lst[b1 + 1:], b7)
    else:
        return fonk1(lst[:b1], b7)
def fonk2(lst, b7):
    b3, b2 = 0, len(lst) - 1
    while b3 <= b2:
        b1 = (b3 + b2)
        if lst[b1] == b7:
            return b1
        elif lst[b1] < b7:
            b3 = b1 + 1
        else:
            b2 = b1 - 1
    return None
def fonk3(lst, b7):
    for i, b4 in enumerate(lst):
        if b4 = = b7:
            return i
    return None
def fonk4():
    for i in range(10, 19):
        b5 = int(math.pow(10, i))
        b6 = list(range(b5))
        b7 = b5 - 3
        print(f"\n-> Quantity: {b5} (10^{i})")
        print("Linear search: null")
        b8 = time.time()
        fonk2(b6, b7)
        b9 = time.time() - b8
        print(f"Binary search: {b9:.6f} seconds")
        b8 = time.time()
        fonk1(b6, b7)
        b10 = time.time() - b8
        print(f"Recursive binary search: {b10:.6f} seconds")
        with open("data.csv", "a") as file:
            file.write(f"{b5};null;{b9:.6f};{b10:.6f}\n")
if b11 = = "__main__":
    fonk4()