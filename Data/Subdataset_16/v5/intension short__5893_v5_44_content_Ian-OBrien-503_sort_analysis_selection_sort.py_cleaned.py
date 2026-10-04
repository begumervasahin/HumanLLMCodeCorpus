import numpy as np
import time
def fonk1(arr):
    b1 = len(arr)
    for i in range(b1):
        b2 = i
        for j in range(i + 1, b1):
            if arr[j] < arr[b2]:
                b2 = j
        arr[i], arr[b2] = arr[b2], arr[i]
def fonk2(arr, description):
    b3 = time.perf_counter()
    fonk1(arr)
    b4 = time.perf_counter()
    b5 = b4 - b3
    print(f"Execution time for selection sort on {description} array of size {len(arr)}: {b5:.6f} seconds")
    print(f"Sorted array: {arr}\b1")
def fonk3(size):
    b6 = np.random.randint(0, 99999, size)
    b7 = np.sort(b6)
    b8 = b7[::-1]
    return b6, b7, b8
def fonk4():
    a1 = 40
    b6, b7, b8 = fonk3(a1)
    fonk2(b6.copy(), "random order")
    fonk2(b7.copy(), "ascending order")
    fonk2(b8.copy(), "reverse order")
if b9 = = "__main__":
    fonk4()