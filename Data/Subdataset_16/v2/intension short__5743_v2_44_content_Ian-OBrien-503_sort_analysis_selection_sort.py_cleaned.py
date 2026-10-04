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
    return arr
def fonk2(arr):
    b3 = time.perf_counter()
    b4 = fonk1(arr.copy())
    b5 = time.perf_counter()
    return b4, b5 - b3
def fonk3(order_description, a1, exec_time):
    print(f"Execution time for selection sort ({order_description}) && ARR_SIZE: {a1} -> {exec_time:.6f} seconds\b1")
def fonk4():
    a1 = 40
    b6 = np.random.randint(0, 99999, a1)
    sorted_array, b7 = fonk2(b6)
    fonk3("Random Order", a1, b7)
    b8 = np.sort(b6)
    sorted_array, b7 = fonk2(b8)
    fonk3("Ascending Order", a1, b7)
    b9 = np.sort(b6)[::-1]
    sorted_array, b7 = fonk2(b9)
    fonk3("Reverse Order", a1, b7)
if b10 = = "__main__":
    fonk4()