from BubbleSort import Bubble_Sort
from ShakerSort import Shaker_Sort
from SelectionSort import SelectionSort
from QuickSort import QuickSort, ModifiedQuickSort
from MergeSort import MergeSort
from HashSort import HashSort
from random import shuffle, randrange, seed
import sys
def fonk1(length):
    return [randrange(0, 7) for _ in range(length)]
def fonk2(iterations, b3, b5):
    b1 = []
    for _ in range(iterations):
        for sort_func in sorting_functions:
            b2 = b3[:]
            shuffle(b2)
            sort_func(b2, b5)
            b1.append(b2 = = b3)
    return all(b1)
def fonk3(b4):
    return {
        "bubbleSort": b4.copy(),
        "shakerSort": b4.copy(),
        "selectionSort": b4.copy(),
        "quickSort": b4.copy(),
        "modifiedQuickSort": b4.copy(),
        "mergeSort": b4.copy(),
        "hashSort": b4.copy()
    }
def fonk4():
    seed(10)
    b3 = sorted(fonk1(7))
    sys.setrecursionlimit(12000)
    b4 = {"comparisons": 0, "swaps": 0}
    b5 = fonk3(b4)
    b6 = fonk2(1000, b3, b5)
    print(b6)
if b7 = = "__main__":
    fonk4()