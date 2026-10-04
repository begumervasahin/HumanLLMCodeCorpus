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
    b5 = {"comparisons": 0, "swaps": 0}
    b6 = {
        "bubbleSort": b5.copy(),
        "shakerSort": b5.copy(),
        "selectionSort": b5.copy(),
        "quickSort": b5.copy(),
        "modifiedQuickSort": b5.copy(),
        "mergeSort": b5.copy(),
        "hashSort": b5.copy()
    }
    for _ in range(b1):
        shuffle(b2)
        fonk2(b2, b6)
        b4.append(b2 = = b3)
        shuffle(b2)
        Shaker_Sort(b2, b6)
        b4.append(b2 = = b3)
        shuffle(b2)
        SelectionSort(b2, b6)
        b4.append(b2 = = b3)
        shuffle(b2)
        QuickSort(b2, b6)
        b4.append(b2 = = b3)
        shuffle(b2)
        ModifiedQuickSort(b2, b6)
        b4.append(b2 = = b3)
        shuffle(b2)
        MergeSort(b2, b6)
        b4.append(b2 = = b3)
        shuffle(b2)
        HashSort(b2, b6)
        b4.append(b2 = = b3)
    if False in b4:
        print(False)
    else:
        print(True)
fonk1()
def fonk2(array, b5):
    b7 = len(array)
    for i in range(b7):
        for j in range(0, b7-i-1):
            b5['bubbleSort']['comparisons'] += 1
            if array[j] > array[j+1]:
                b5['bubbleSort']['swaps'] += 1
                array[j], array[j+1] = array[j+1], array[j]
