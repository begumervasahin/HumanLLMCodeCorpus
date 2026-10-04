import time
import math
def fonk1(arr, b6):
    if len(arr) == 0:
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
    for i, b4 in enumerate(arr):
        if b4 = = b6:
            return i
    return None
def fonk4():
    for exponent in range(10, 19):
        b5 = range(0, int(math.pow(10, exponent)))
        b6 = int(math.pow(10, exponent)) - 3
        print(f"\n-> Quantity: {len(b5)} (10 to the power of {exponent})")
        print("Linear search: null")
        b7 = time.time()
        b8 = fonk2(b5, b6)
        b9 = time.time() - b7
        print(f"Binary search result: {b8}")
        print(f"Time taken for binary search: {b9:.6f} seconds")
        b7 = time.time()
        b10 = fonk1(b5, b6)
        b11 = time.time() - b7
        print(f"Recursive binary search result: {b10}")
        print(f"Time taken for recursive binary search: {b11:.6f} seconds")
        with open("data.csv", "a") as file:
            file.write(f"{len(b5)};null;{b9:.6f};{b11:.6f}\n")
fonk4()