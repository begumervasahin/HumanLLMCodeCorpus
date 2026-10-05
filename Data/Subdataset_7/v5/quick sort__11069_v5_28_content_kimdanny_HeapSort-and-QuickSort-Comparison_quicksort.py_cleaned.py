import time
from random import randint
def fonk1(arr, low, high):
    b1 = (low - 1)
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
    print("Quick sort performance test:")
    b4 = [100000, 1200000, 2300000, 3400000, 4500000, 5600000, 6700000, 7800000, 8900000, 10000000]
    for b1, input_size in enumerate(b4, b5 = 1):
        b6 = [randint(1, input_size) for _ in range(input_size)]
        print(f"Running test {b1} for input size: {input_size}")
        b7 = time.time()
        fonk2(b6, 0, len(b6) - 1)
        b8 = time.time()
        print(f"Time taken: {b8 - b7:.5f} seconds\n")
if b9 = = "__main__":
    fonk3()