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
    print(f"\b1{arr}\b1\b1{b5:.6f} seconds for selection sort on {description} array of size: {len(arr)}\b1")
a1 = 40
b6 = np.random.randint(0, 99999, a1)
fonk2(b6.copy(), "random order")
b7 = np.sort(b6)
fonk2(b7.copy(), "ascending order")
b8 = np.sort(b6)[::-1]
fonk2(b8.copy(), "reverse order")