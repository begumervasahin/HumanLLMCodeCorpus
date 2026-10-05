from BubbleSort import Bubble_Sort
from ShakerSort import Shaker_Sort
from SelectionSort import SelectionSort
from QuickSort import QuickSort, ModifiedQuickSort
from MergeSort import MergeSort
from HashSort import HashSort
from random import shuffle, randrange, seed
def fonk1(b1 = 1000, debug=False):
    if debug:
        seed(10)
    b2 = [randrange(0, 7) for _ in range(7)]
    b3 = sorted(b2)
    b4 = []
    import sys
    sys.setrecursionlimit(12000)
    for _ in range(b1):
        for sorting_algorithm in b6:
            b5 = b2[:]
            sorting_algorithm(b5, b8)
            b4.append(b5 = = b3)
            shuffle(b2)
    print(all(b4))
b6 = [
    Bubble_Sort,
    Shaker_Sort,
    SelectionSort,
    QuickSort,
    ModifiedQuickSort,
    MergeSort,
    HashSort
]
b7 = {"comparisons": 0, "swaps": 0}
b8 = {algorithm.__name__: b7.copy() for algorithm in b6}
fonk1()