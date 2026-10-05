import numpy as np
import matplotlib.pyplot as plt
import selection_sort
import insertion_sort
import merge_sort
import time
def fonk1():
    b1 = []
    b2 = []
    b3 = []
    b4 = [10**i for i in range(1, 5)]
    for size in b4:
        b5 = np.random.random_integers(1, 10000000, size=size)
        b6 = time.time()
        selection_sort.selectionSort(b5)
        b7 = time.time() - b6
        b2.append(b7)
        b6 = time.time()
        merge_sort.mergeSort(b5)
        b7 = time.time() - b6
        b3.append(b7)
        b6 = time.time()
        insertion_sort.insertionSort(b5)
        b7 = time.time() - b6
        b1.append(b7)
    plt.figure(b8 = (12, 5))
    plt.plot(b4, b2, b9 = 'x', c='b', label='Selection Sort')
    plt.plot(b4, b3, b9 = 'x', c='r', label='Merge Sort')
    plt.plot(b4, b1, b9 = 'x', c='g', label='Insertion Sort')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel("Size of Unsorted List (log scale)")
    plt.ylabel("Seconds of Computation (log scale)")
    plt.legend(b10 = 'upper left')
    plt.grid()
    plt.title("Comparison of Selection Sort, Merge Sort, and Insertion Sort")
    plt.show()
fonk1()