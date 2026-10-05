import numpy as np
import matplotlib.pyplot as plt
import selection_sort
import insertion_sort
import merge_sort
import time
def fonk1(b1):
    return np.random.randint(1, 10000000, b1 = b1)
def fonk2(sort_func, b11):
    b2 = time.time()
    b3 = sort_func(b11.copy())
    return time.time() - b2
def fonk3(b7, b8, b9, b10):
    plt.figure(b4 = (12, 5))
    plt.plot(b7, b8, b5 = 'x', c='b', label='Selection Sort')
    plt.plot(b7, b9, b5 = 'x', c='r', label='Merge Sort')
    plt.plot(b7, b10, b5 = 'x', c='g', label='Insertion Sort')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel("Size of Unsorted List (log scale)")
    plt.ylabel("Seconds of Computation (log scale)")
    plt.legend(b6 = 'upper left')
    plt.grid()
    plt.title("Comparison of Selection Sort, Merge Sort, and Insertion Sort")
    plt.show()
def fonk4():
    b7 = [10**i for i in range(1, 5)]
    b8 = []
    b9 = []
    b10 = []
    for b1 in b7:
        b11 = fonk1(b1)
        b12 = fonk2(selection_sort.selectionSort, b11)
        b13 = fonk2(merge_sort.mergeSort, b11)
        b14 = fonk2(insertion_sort.insertionSort, b11)
        b8.append(b12)
        b9.append(b13)
        b10.append(b14)
    fonk3(b7, b8, b9, b10)
if b15 = = "__main__":
    fonk4()