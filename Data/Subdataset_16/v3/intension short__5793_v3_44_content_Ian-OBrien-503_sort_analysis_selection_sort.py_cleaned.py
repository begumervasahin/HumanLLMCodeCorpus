import numpy as np
import time
def fonk1(b7):
    b1 = len(b7)
    for i in range(b1):
        b2 = i
        for j in range(i + 1, b1):
            if b7[j] < b7[b2]:
                b2 = j
        b7[i], b7[b2] = b7[b2], b7[i]
    return b7
def fonk2(b7, sort_function):
    b3 = time.perf_counter()
    b4 = sort_function(b7.copy())
    b5 = time.perf_counter()
    return b4, b5 - b3
def fonk3(description, a1, b9):
    print(f"Execution time for selection sort ({description}) - ARR_SIZE: {a1} -> {b9:.6f} seconds\b1")
def fonk4(length, b6 = "random"):
    b7 = np.random.randint(0, 99999, length)
    if b6 = = "ascending":
        return np.sort(b7)
    elif b6 = = "descending":
        return np.sort(b7)[::-1]
    return b7
def fonk5():
    a1 = 40
    b8 = fonk4(a1)
    sorted_array, b9 = fonk2(b8, selection_sort)
    fonk3("Random Order", a1, b9)
    b10 = fonk4(a1, b6="ascending")
    sorted_array, b9 = fonk2(b10, selection_sort)
    fonk3("Ascending Order", a1, b9)
    b11 = fonk4(a1, b6="descending")
    sorted_array, b9 = fonk2(b11, selection_sort)
    fonk3("Descending Order", a1, b9)
if b12 = = "__main__":
    fonk5()