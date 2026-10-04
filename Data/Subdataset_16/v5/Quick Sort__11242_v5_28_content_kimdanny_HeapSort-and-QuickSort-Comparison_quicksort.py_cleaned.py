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
    b4 = [100000, 1200000, 2300000, 3400000, 4500000, 5600000, 6700000, 7800000, 8900000, 10000000]
    b5 = [fonk4(size) for size in b4]
    for b1, size in enumerate(b4):
        print(f"Clock {b1+1} is ticking for input size {size}...")
        b6 = time.time()
        fonk2(b5[b1], 0, len(b5[b1]) - 1)
        b7 = time.time()
        b8 = b7 - b6
        print(f"Time taken for InputSize({size}) is {b8:.2f} seconds")
def fonk4(size):
    return [randint(1, size) for _ in range(size)]
if b9 = = "__main__":
    print("Quick Sort Benchmarking")
    fonk3()