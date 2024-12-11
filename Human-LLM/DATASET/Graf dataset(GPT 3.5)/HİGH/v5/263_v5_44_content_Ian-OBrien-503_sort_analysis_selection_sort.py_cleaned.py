import random
import numpy as np
import time
def fonk1(arr):
    b1 = time.process_time()
    b2 = len(arr)
    for i in range(b2):
        b3 = i
        for j in range(i + 1, b2):
            if arr[j] < arr[b3]:
                b3 = j
        arr[i], arr[b3] = arr[b3], arr[i]
    b4 = time.process_time()
    b5 = b4 - b1
    return b5
def fonk2():
    b2 = 40
    b6 = np.random.randint(0, 99999, b2)
    print("Random order:")
    print("Before sorting:", b6)
    b7 = fonk1(b6)
    print("After sorting:", b6)
    print("Execution time:", b7, "seconds")
    b8 = np.sort(b6)
    print("\nAscending order:")
    print("Before sorting:", b8)
    b9 = fonk1(b8)
    print("After sorting:", b8)
    print("Execution time:", b9, "seconds")
    b10 = np.sort(b6)[::-1]
    print("\nReverse order:")
    print("Before sorting:", b10)
    b11 = fonk1(b10)
    print("After sorting:", b10)
    print("Execution time:", b11, "seconds")
if b12 = = "__main__":
    fonk2()