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
    b2 = [randrange(0, 7) for x in range(7)]
    b3 = b2[:]
    b3.sort()
    b4 = []
    import sys
    sys.setrecursionlimit(12000)
    for test in range(b1):
        b5 = b2[:]
        Bubble_Sort(b5, b7)
        b4.append(b5 = = b3)
        b5 = b2[:]
        Shaker_Sort(b5, b7)
        b4.append(b5 = = b3)
        b5 = b2[:]
        SelectionSort(b5, b7)
        b4.append(b5 = = b3)
        b5 = b2[:]
        QuickSort(b5, b7)
        b4.append(b5 = = b3)
        b5 = b2[:]
        ModifiedQuickSort(b5, b7)
        b4.append(b5 = = b3)
        b5 = b2[:]
        MergeSort(b5, b7)
        b4.append(b5 = = b3)
        b5 = b2[:]
        HashSort(b5, b7)
        b4.append(b5 = = b3)
        shuffle(b2)
    if False in b4:
        print(False)
    else:
        print(True)
b6 = {"comparisons": 0, "swaps": 0}
b7 = {
    "bubbleSort": b6,
    "shakerSort": b6,
    "selectionSort": b6,
    "quickSort": b6,
    "modifiedQuickSort": b6,
    "mergeSort": b6,
    "hashSort": b6
}
fonk1()