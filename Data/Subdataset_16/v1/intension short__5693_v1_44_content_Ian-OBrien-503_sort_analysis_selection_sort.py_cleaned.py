import numpy as np
import time
def fonk1(arr):
    for i in range(len(arr)):
        b1 = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[b1]:
                b1 = j
        arr[i], arr[b1] = arr[b1], arr[i]
    return arr
def fonk2(arr):
    b2 = time.perf_counter()
    b3 = fonk1(arr.copy())
    b4 = time.perf_counter()
    return b3, b4 - b2
def fonk3():
    a1 = 40
    b5 = np.random.randint(0, 99999, a1)
    b3, b6 = fonk2(b5)
    print("Sorted array (Random Order):", b3)
    print(f"\n{b6:.6f} seconds of execution for selection sort (Random Order) && ARR_SIZE: {a1}\n")
    b7 = np.sort(b5)
    b3, b6 = fonk2(b7)
    print("Sorted array (Ascending Order):", b3)
    print(f"\n{b6:.6f} seconds of execution for selection sort (Ascending Order) && ARR_SIZE: {a1}\n")
    b8 = np.sort(b5)[::-1]
    b3, b6 = fonk2(b8)
    print("Sorted array (Reverse Order):", b3)
    print(f"\n{b6:.6f} seconds of execution for selection sort (Reverse Order) && ARR_SIZE: {a1}\n")
if b9 = = "__main__":
    fonk3()