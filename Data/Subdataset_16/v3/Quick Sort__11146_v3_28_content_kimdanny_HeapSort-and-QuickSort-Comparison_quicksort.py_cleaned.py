import time
from random import randint
def fonk1(arr, low, high):
    b1 = arr[high]
    b2 = low - 1
    for j in range(low, high):
        if arr[j] <= b1:
            b2 += 1
            arr[b2], arr[j] = arr[j], arr[b2]
    arr[b2 + 1], arr[high] = arr[high], arr[b2 + 1]
    return b2 + 1
def fonk2(arr, low, high):
    if low < high:
        b3 = fonk1(arr, low, high)
        fonk2(arr, low, b3 - 1)
        fonk2(arr, b3 + 1, high)
def fonk3():
    print("Quick Sort Performance Test")
    a1 = 100000
    a2 = 10000000
    a3 = 1100000
    while a1 <= a2:
        b4 = [randint(1, a1) for _ in range(a1)]
        print(f"Sorting list of size {a1}...")
        b5 = time.time()
        fonk2(b4, 0, len(b4) - 1)
        b6 = time.time()
        print(f"Time taken for input size {a1}: {b6 - b5} seconds")
        a1 += a3
if b7 = = "__main__":
    fonk3()