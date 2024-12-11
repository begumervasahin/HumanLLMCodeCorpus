import time
import math
def fonk1(arr, b3):
    if len(arr) == 0:
        return False
    else:
        b1 = len(arr)
        if arr[b1] == b3:
            return True
        elif arr[b1] < b3:
            return fonk1(arr[b1 + 1:], b3)
        else:
            return fonk1(arr[:b1], b3)
def fonk2(arr, b3):
    a1 = 0
    b2 = len(arr) - 1
    while a1 <= b2:
        b1 = (a1 + b2)
        if arr[b1] == b3:
            return b1
        elif arr[b1] < b3:
            a1 = b1 + 1
        else:
            b2 = b1 - 1
    return None
def fonk3(arr, b3):
    for i, num in enumerate(arr):
        if b3 = = num:
            return i
    return None
def fonk4():
    for i in range(10, 19):
        b4 = range(0, int(math.pow(10, i)))
        b3 = (int(math.pow(10, i)) - 3)
        b5 = f"{len(b4)};"
        print(f"\n-> Quantity: {b3 + 3} (10 to the power of {i})")
        print("Linear search: null")
        b5 += "null;"
        b6 = time.time()
        print("Binary search:", fonk2(b4, b3))
        b7 = time.time() - b6
        print("Time taken for Binary search:", b7)
        b5 += f"{b7};"
        b6 = time.time()
        print("Recursive binary search:", fonk1(b4, b3))
        b7 = time.time() - b6
        print("Time taken for Recursive binary search:", b7)
        b5 += f"{b7}"
        with open("data.csv", "a") as file:
            file.write(b5 + "\n")
fonk4()