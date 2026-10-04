import sys
from random import shuffle, randrange, seed
from BubbleSort import Bubble_Sort
from ShakerSort import Shaker_Sort
from SelectionSort import SelectionSort
from QuickSort import QuickSort, ModifiedQuickSort
from MergeSort import MergeSort
from HashSort import HashSort
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
        fonk2(b2[:], b6)
        b4.append(b2 = = b3)
        shuffle(b2)
        fonk3(b2[:], b6)
        b4.append(b2 = = b3)
        shuffle(b2)
        fonk4(b2[:], b6)
        b4.append(b2 = = b3)
        shuffle(b2)
        fonk5(b2[:], b6)
        b4.append(b2 = = b3)
        shuffle(b2)
        ModifiedQuickSort(b2[:], b6)
        b4.append(b2 = = b3)
        shuffle(b2)
        fonk7(b2[:], b6)
        b4.append(b2 = = b3)
        shuffle(b2)
        fonk8(b2[:], b6)
        b4.append(b2 = = b3)
    if False in b4:
        print("Some tests failed.")
    else:
        print("All tests passed successfully.")
if b7 = = "__main__":
    fonk1()
def fonk2(array, b5):
    b8 = len(array)
    for b16 in range(b8):
        for j in range(0, b8-b16-1):
            b5['bubbleSort']['comparisons'] += 1
            if array[j] > array[j+1]:
                b5['bubbleSort']['swaps'] += 1
                array[j], array[j+1] = array[j+1], array[j]
def fonk3(array, b5):
    b8 = len(array)
    b9 = True
    a1 = 0
    b10 = b8 - 1
    while b9:
        b9 = False
        for b16 in range(a1, b10):
            b5['shakerSort']['comparisons'] += 1
            if array[b16] > array[b16 + 1]:
                b5['shakerSort']['swaps'] += 1
                array[b16], array[b16 + 1] = array[b16 + 1], array[b16]
                b9 = True
        if not b9:
            break
        b9 = False
        b10 = b10 - 1
        for b16 in range(b10 - 1, a1 - 1, -1):
            b5['shakerSort']['comparisons'] += 1
            if array[b16] > array[b16 + 1]:
                b5['shakerSort']['swaps'] += 1
                array[b16], array[b16 + 1] = array[b16 + 1], array[b16]
                b9 = True
        a1 = a1 + 1
def fonk4(array, b5):
    b8 = len(array)
    for b16 in range(b8):
        b11 = b16
        for j in range(b16+1, b8):
            b5['selectionSort']['comparisons'] += 1
            if array[j] < array[b11]:
                b11 = j
        b5['selectionSort']['swaps'] += 1
        array[b16], array[b11] = array[b11], array[b16]
def fonk5(array, b5, b12 = 0, b13=None):
    if b13 is None:
        b13 = len(array) - 1
    if b12 < b13:
        b14 = fonk6(array, b12, b13, b5)
        fonk5(array, b5, b12, b14 - 1)
        fonk5(array, b5, b14 + 1, b13)
def fonk6(array, b12, b13, b5):
    b15 = array[b13]
    b16 = b12 - 1
    for j in range(b12, b13):
        b5['quickSort']['comparisons'] += 1
        if array[j] < b15:
            b16 += 1
            b5['quickSort']['swaps'] += 1
            array[b16], array[j] = array[j], array[b16]
    b5['quickSort']['swaps'] += 1
    array[b16 + 1], array[b13] = array[b13], array[b16 + 1]
    return b16 + 1
def fonk7(array, b5):
    if len(array) > 1:
        b17 = len(array)
        b18 = array[:b17]
        b19 = array[b17:]
        fonk7(b18, b5)
        fonk7(b19, b5)
        b16 = j = k = 0
        while b16 < len(b18) and j < len(b19):
            b5['mergeSort']['comparisons'] += 1
            if b18[b16] < b19[j]:
                array[k] = b18[b16]
                b16 += 1
            else:
                array[k] = b19[j]
                j += 1
            k += 1
        while b16 < len(b18):
            array[k] = b18[b16]
            b16 += 1
            k += 1
        while j < len(b19):
            array[k] = b19[j]
            j += 1
            k += 1
def fonk8(array, b5):
    array.sort()