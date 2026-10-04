import time
import math
def fonk1(arr, b6):
    if not arr:
        return False
    b1 = len(arr)
    if arr[b1] == b6:
        return True
    elif arr[b1] < b6:
        return fonk1(arr[b1 + 1:], b6)
    else:
        return fonk1(arr[:b1], b6)
def fonk2(arr, b6):
    b3, b2 = 0, len(arr) - 1
    while b3 <= b2:
        b1 = (b3 + b2)
        if arr[b1] == b6:
            return b1
        elif arr[b1] < b6:
            b3 = b1 + 1
        else:
            b2 = b1 - 1
    return None
def fonk3(arr, b6):
    for index, b4 in enumerate(arr):
        if b4 = = b6:
            return index
    return None
def fonk4():
    with open("data.csv", "a") as file:
        for exponent in range(1, 8):
            b5 = list(range(0, int(math.pow(10, exponent))))
            b6 = int(math.pow(10, exponent)) - 3
            b7 = f"{len(b5)};"
            print(f"\n-> Quantity: {b6 + 3} (10 to the power of {exponent})")
            print("Linear search: null")
            b7 += "null;"
            b8 = time.time()
            fonk2(b5, b6)
            b9 = time.time() - b8
            print(f"Binary search: {b9}")
            b7 += f"{b9};"
            b8 = time.time()
            fonk1(b5, b6)
            b9 = time.time() - b8
            print(f"Recursive binary search: {b9}")
            b7 += f"{b9}"
            file.write(b7 + "\n")
fonk4()