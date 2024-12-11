import numpy as np
import matplotlib.pyplot as plt
import selection_sort
import insertion_sort
import MERGE
import time
def fonk1():
    b1 = []
    b2 = []
    b3 = []
    b4 = [10**i for i in range(1, 5)]
    for size in b4:
        b5 = np.random.random_integers(1, 10000000, size=size)
        b6 = time.time()
        b7 = selection_sort.selectionSort(b5.copy())
        b8 = time.time() - b6
        b2.append(b8)
        b6 = time.time()
        b9 = MERGE.mergeSort(b5.copy())
        b8 = time.time() - b6
        b3.append(b8)
        b6 = time.time()
        b10 = insertion_sort.insertionSort(b5.copy())
        b8 = time.time() - b6
        b1.append(b8)
    plt.figure(b11 = (12, 5))
    plt.plot(b4, b2, b12 = 'x', c='b', label='Selectionsort')
    plt.plot(b4, b3, b12 = 'x', c='r', label='Mergesort')
    plt.plot(b4, b1, b12 = 'x', c='g', label='Insertionsort')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel("Size of unsorted list - log scale")
    plt.ylabel("Seconds of computation - log scale")
    plt.legend(b13 = 2)
    plt.grid()
    plt.title("Selectionsort vs Mergesort vs Insertionsort")
    plt.show()
fonk1()