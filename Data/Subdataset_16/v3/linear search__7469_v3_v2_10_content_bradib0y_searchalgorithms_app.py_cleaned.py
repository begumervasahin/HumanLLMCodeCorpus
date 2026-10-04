import time
import math
def fonk1(lst, b8):
    if not lst:
        return False
    b1 = len(lst)
    if lst[b1] == b8:
        return True
    elif lst[b1] < b8:
        return fonk1(lst[b1 + 1:], b8)
    else:
        return fonk1(lst[:b1], b8)
def fonk2(lst, b8):
    b3, b2 = 0, len(lst) - 1
    while b3 <= b2:
        b1 = (b3 + b2)
        if lst[b1] == b8:
            return b1
        elif lst[b1] < b8:
            b3 = b1 + 1
        else:
            b2 = b1 - 1
    return None
def fonk3(lst, b8):
    for i, b4 in enumerate(lst):
        if b4 = = b8:
            return i
    return None
def fonk4(search_func, lst, b8):
    b5 = time.time()
    search_func(lst, b8)
    return time.time() - b5
def fonk5(b6, b9, b10):
    with open("data.csv", "a") as file:
        file.write(f"{b6};null;{b9:.6f};{b10:.6f}\n")
def fonk6():
    for i in range(10, 19):
        b6 = int(math.pow(10, i))
        b7 = list(range(b6))
        b8 = b6 - 3
        print(f"\n-> Quantity: {b6} (10^{i})")
        print("Linear search: null")
        b9 = fonk4(binary_search, b7, b8)
        print(f"Binary search: {b9:.6f} seconds")
        b10 = fonk4(recursive_binary_search, b7, b8)
        print(f"Recursive binary search: {b10:.6f} seconds")
        fonk5(b6, b9, b10)
if b11 = = "__main__":
    fonk6()