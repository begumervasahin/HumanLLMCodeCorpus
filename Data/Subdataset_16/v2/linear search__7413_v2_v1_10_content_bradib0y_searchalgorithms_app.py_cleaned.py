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
    b3, b2 = 0, len(lst) - 1
    while b3 <= b2:
        b1 = (b3 + b2)
        if lst[b1] == b6:
            return b1
        elif lst[b1] < b6:
            b3 = b1 + 1
        else:
            b2 = b1 - 1
    return None
def fonk3(lst, b6):
    for index, b4 in enumerate(lst):
        if b4 = = b6:
            return index
    return None
def fonk4():
    for i in range(10, 19):
        b5 = list(range(int(math.pow(10, i))))
        b6 = int(math.pow(10, i)) - 3
        print(f"\n-> Quantity: {b6 + 3} (10 to the power of {i})")
        print("Linear search: null")
        b7 = f"{len(b5)};null;"
        b8 = time.time()
        b9 = fonk2(b5, b6)
        b10 = time.time() - b8
        print(f"Binary search: {b10}")
        b7 += f"{b10};"
        b8 = time.time()
        b11 = fonk1(b5, b6)
        b12 = time.time() - b8
        print(f"Recursive binary search: {b12}")
        b7 += f"{b12}"
        with open("data.csv", "a") as file:
            file.write(b7 + "\n")
if b13 = = "__main__":
    fonk4()