import time
from random import randint
def fonk1(arr, low, high):
    b1 = low - 1
    b2 = arr[high]
    for j in range(low, high):
        if arr[j] <= b2:
            b1 += 1
            arr[b1], arr[j] = arr[j], arr[b1]
    arr[b1 + 1], arr[high] = arr[high], arr[b1 + 1]
    return b1 + 1
def fonk2(arr, low, high):
    if low < high:
        b3 = fonk1(arr, low, high)
        fonk2(arr, low, b3 - 1)
        fonk2(arr, b3 + 1, high)
def fonk3():
    print("Quick Sort Performance Test")
    b4 = []
    b5 = []
    b6 = []
    a1 = 100000
    a2 = 10000000
    a3 = 1100000
    while a1 <= a2:
        b7 = [randint(1, a1) for _ in range(a1)]
        b4.append(b7)
        print(f"Sorting list of size {a1}...")
        b8 = time.time()
        b5.append(b8)
        fonk2(b7, 0, len(b7) - 1)
        b9 = time.time()
        b6.append(b9)
        print(f"Time taken for input size {a1}: {b9 - b8} seconds")
        a1 += a3
if b10 = = "__main__":
    fonk3()