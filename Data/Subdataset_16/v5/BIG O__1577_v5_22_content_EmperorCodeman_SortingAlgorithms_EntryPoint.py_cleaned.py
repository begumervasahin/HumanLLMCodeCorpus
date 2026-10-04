from BubbleSort import Bubble_Sort
from ShakerSort import Shaker_Sort
from SelectionSort import SelectionSort
from QuickSort import QuickSort, ModifiedQuickSort
from MergeSort import MergeSort
from HashSort import HashSort
from random import shuffle, randrange, seed
import sys
def fonk1(b1 = 1000, debug=False):
    if debug:
        seed(10)
    b2 = [randrange(0, 7) for _ in range(7)]
    b3 = sorted(b2[:])
    b4 = []
    sys.setrecursionlimit(12000)
    b5 = [
        (Bubble_Sort, "Bubble Sort"),
        (Shaker_Sort, "Shaker Sort"),
        (SelectionSort, "Selection Sort"),
        (HashSort, "Hash Sort"),
        (MergeSort, "Merge Sort")
    ]
    b6 = {name: {"comparisons": 0, "swaps": 0} for _, name in b5}
    for _ in range(b1):
        for sort_func, name in b5:
            fonk2(sort_func, b2, b3, b6[name], b4)
    fonk3(b4)
def fonk2(sort_func, b2, b3, metrics, b4):
    b7 = b2[:]
    sort_func(b7, metrics)
    b8 = b7 == b3
    b4.append(b8)
    shuffle(b2)
def fonk3(b4):
    if any(not result for result in b4):
        print("Some sorting algorithms failed.")
    else:
        print("All sorting algorithms passed.")
if b9 = = "__main__":
    fonk1()