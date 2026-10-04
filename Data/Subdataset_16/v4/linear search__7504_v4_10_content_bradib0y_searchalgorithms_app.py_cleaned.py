import time
import math
def fonk1(lst, target):
    if len(lst) == 0:
        return False
    else:
        b1 = len(lst)
        if lst[b1] == target:
            return True
        elif lst[b1] < target:
            return fonk1(lst[b1 + 1:], target)
        else:
            return fonk1(lst[:b1], target)
def fonk2(lst, target):
    a1 = 0
    b2 = len(lst) - 1
    while a1 <= b2:
        b1 = (a1 + b2)
        if lst[b1] == target:
            return b1
        elif lst[b1] < target:
            a1 = b1 + 1
        else:
            b2 = b1 - 1
    return None
def fonk3(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return None
def fonk4():
    for i in range(10, 19):
        b3 = list(range(int(math.pow(10, i))))
        b4 = int(math.pow(10, i)) - 3
        b5 = f"{len(b3)};"
        print(f"\n-> Quantity: {b4 + 3} (10 to the power of {i})")
        print("Linear search: null")
        b5 += "null;"
        b6 = time.time()
        fonk2(b3, b4)
        b7 = time.time() - b6
        print(f"Binary search: {b7}")
        b5 += f"{b7};"
        b6 = time.time()
        fonk1(b3, b4)
        b8 = time.time() - b6
        print(f"Recursive binary search: {b8}")
        b5 += f"{b8}"
        with open("data.csv", "a") as file:
            file.write(b5 + "\n")
if b9 = = "__main__":
    fonk4()