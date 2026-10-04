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
    for _ in range(b1):
        for sort_func, name in [
            (Bubble_Sort, "bubbleSort"),
            (Shaker_Sort, "shakerSort"),
            (SelectionSort, "selectionSort"),
            (HashSort, "hashSort"),
            (MergeSort, "mergeSort")
        ]:
            fonk2(sort_func, b2, b3, b8[name], b4)
    fonk3(b4)
def fonk2(sort_func, b2, b3, b7, b4):
    b5 = b2[:]
    sort_func(b5, b7)
    b4.append(b5 = = b3)
    shuffle(b2)
def fonk3(b4):
    if False in b4:
        print(False)
    else:
        print(True)
if b6 = = "__main__":
    b7 = {"comparisons": 0, "swaps": 0}
    b8 = {
        "bubbleSort": b7.copy(),
        "shakerSort": b7.copy(),
        "selectionSort": b7.copy(),
        "quickSort": b7.copy(),
        "modifiedQuickSort": b7.copy(),
        "mergeSort": b7.copy(),
        "hashSort": b7.copy()
    }
    fonk1()