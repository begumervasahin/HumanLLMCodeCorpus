from BubbleSort import Bubble_Sort
from ShakerSort import Shaker_Sort
from SelectionSort import SelectionSort
from QuickSort import QuickSort, ModifiedQuickSort
from MergeSort import MergeSort
from HashSort import HashSort
from random import shuffle, randrange, seed
def fonk1(b1 = 1000,debug=False):
    if debug:
        seed(10)
    b2 = [randrange(0, 7) for x in range(7)]
    b3 = b2[:]
    b3.sort()
    b4 = []
    import sys
    sys.setrecursionlimit(12000)
    for test in range(b1):
        Bubble_Sort(b2,b6)
        b4.append(b2 = = b3)
        shuffle(b2)
        Shaker_Sort(b2,b6)
        b4.append(b2 = =b3)
        shuffle(b2)
        SelectionSort(b2, b6)
        b4.append(b2 = = b3)
        shuffle(b2)
        shuffle(b2)
        shuffle(b2)
        HashSort(b2, b6)
        b4.append(b2 = = b3)
        shuffle(b2)
        MergeSort(b2, b6)
        b4.append(b2 = = b3)
    if False in b4:
        print(False)
    else:
        print(True)
b5 = {"comparisons":0,"swaps":0}
b6 = {"bubbleSort":b5,
               "shakerSort":b5,
               "selectionSort":b5,
               "quickSort":b5,
               "modifiedQuickSort":b5,
               "mergeSort":b5,
               "hashSort": b5}
fonk1()