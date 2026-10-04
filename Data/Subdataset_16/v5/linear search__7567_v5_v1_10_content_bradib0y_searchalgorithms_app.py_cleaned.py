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
    for index, b3 in enumerate(lst):
        if b3 = = b6:
            return index
    return None
def fonk4(b7, b4 = "b7.csv"):
    with open(b4, "a") as file:
        file.write(";".join(map(str, b7)) + "\n")
def fonk5():
    for exponent in range(10, 19):
        b5 = list(range(0, int(math.pow(10, exponent))))
        b6 = int(math.pow(10, exponent)) - 3
        print(f"\n-> Quantity: {len(b5)} (10 to the power of {exponent})")
        print("Linear search: null")
        b7 = [len(b5), "null"]
        b8 = time.time()
        b9 = fonk2(b5, b6)
        b10 = time.time() - b8
        print(b9)
        print(f"Binary search: {b10:.5f} seconds")
        b7.append(f"{b10:.5f}")
        b8 = time.time()
        b11 = fonk1(b5, b6)
        b12 = time.time() - b8
        print(b11)
        print(f"Recursive binary search: {b12:.5f} seconds")
        b7.append(f"{b12:.5f}")
        fonk4(b7)
if b13 = = "__main__":
    fonk5()