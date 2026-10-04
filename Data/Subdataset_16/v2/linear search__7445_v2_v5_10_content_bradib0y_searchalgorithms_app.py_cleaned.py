import time
import math
def fonk1(arr, b5):
    if len(arr) == 0:
        return False
    else:
        b1 = len(arr)
        if arr[b1] == b5:
            return True
        elif arr[b1] < b5:
            return fonk1(arr[b1 + 1:], b5)
        else:
            return fonk1(arr[:b1], b5)
def fonk2(arr, b5):
    a1 = 0
    b2 = len(arr) - 1
    while a1 <= b2:
        b1 = (a1 + b2)
        if arr[b1] == b5:
            return b1
        elif arr[b1] < b5:
            a1 = b1 + 1
        else:
            b2 = b1 - 1
    return None
def fonk3(arr, b5):
    for i, b3 in enumerate(arr):
        if b3 = = b5:
            return i
    return None
def fonk4():
    for i in range(10, 19):
        b4 = list(range(0, int(math.pow(10, i))))
        b5 = int(math.pow(10, i)) - 3
        b6 = f"{len(b4)};"
        print(f"\n-> Quantity: {len(b4)} (10 to the power of {i})")
        print("Linear search: null")
        b6 += "null;"
        b7 = time.time()
        print("Binary search result:", fonk2(b4, b5))
        b8 = time.time() - b7
        print("Time taken for Binary search:", b8)
        b6 += f"{b8};"
        b7 = time.time()
        print("Recursive binary search result:", fonk1(b4, b5))
        b9 = time.time() - b7
        print("Time taken for Recursive binary search:", b9)
        b6 += f"{b9}"
        with open("data.csv", "a") as file:
            file.write(b6 + "\n")
if b10 = = "__main__":
    fonk4()