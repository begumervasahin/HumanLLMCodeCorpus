import sys
from random import shuffle, randrange, seed
from BubbleSort import Bubble_Sort
from ShakerSort import Shaker_Sort
from SelectionSort import SelectionSort
from QuickSort import QuickSort, ModifiedQuickSort
from MergeSort import MergeSort
from HashSort import HashSort
def fonk1():
    b1 = {"comparisons": 0, "swaps": 0}
    return {
        "bubbleSort": b1.copy(),
        "shakerSort": b1.copy(),
        "selectionSort": b1.copy(),
        "quickSort": b1.copy(),
        "modifiedQuickSort": b1.copy(),
        "mergeSort": b1.copy(),
        "hashSort": b1.copy()
    }
def fonk2(b3, b5, b4, b6):
    b2 = []
    for _ in range(b4):
        shuffle(b3)
        fonk4(b3[:], b6)
        b2.append(b3 = = b5)
        shuffle(b3)
        fonk5(b3[:], b6)
        b2.append(b3 = = b5)
        shuffle(b3)
        fonk6(b3[:], b6)
        b2.append(b3 = = b5)
        shuffle(b3)
        fonk7(b3[:], b6)
        b2.append(b3 = = b5)
        shuffle(b3)
        ModifiedQuickSort(b3[:], b6)
        b2.append(b3 = = b5)
        shuffle(b3)
        fonk9(b3[:], b6)
        b2.append(b3 = = b5)
        shuffle(b3)
        fonk10(b3[:], b6)
        b2.append(b3 = = b5)
    return b2
def fonk3(b4 = 1000, debug=False):
    if debug:
        seed(10)
    b3 = [randrange(0, 7) for _ in range(7)]
    b5 = sorted(b3[:])
    sys.setrecursionlimit(12000)
    b6 = fonk1()
    b2 = fonk2(b3, b5, b4, b6)
    if False in b2:
        print("Some tests failed.")
    else:
        print("All tests passed successfully.")
def fonk4(array, b1):
    b7 = len(array)
    for b15 in range(b7):
        for j in range(0, b7-b15-1):
            b1['bubbleSort']['comparisons'] += 1
            if array[j] > array[j+1]:
                b1['bubbleSort']['swaps'] += 1
                array[j], array[j+1] = array[j+1], array[j]
def fonk5(array, b1):
    b7 = len(array)
    b8 = True
    a1 = 0
    b9 = b7 - 1
    while b8:
        b8 = False
        for b15 in range(a1, b9):
            b1['shakerSort']['comparisons'] += 1
            if array[b15] > array[b15 + 1]:
                b1['shakerSort']['swaps'] += 1
                array[b15], array[b15 + 1] = array[b15 + 1], array[b15]
                b8 = True
        if not b8:
            break
        b8 = False
        b9 = b9 - 1
        for b15 in range(b9 - 1, a1 - 1, -1):
            b1['shakerSort']['comparisons'] += 1
            if array[b15] > array[b15 + 1]:
                b1['shakerSort']['swaps'] += 1
                array[b15], array[b15 + 1] = array[b15 + 1], array[b15]
                b8 = True
        a1 = a1 + 1
def fonk6(array, b1):
    b7 = len(array)
    for b15 in range(b7):
        b10 = b15
        for j in range(b15+1, b7):
            b1['selectionSort']['comparisons'] += 1
            if array[j] < array[b10]:
                b10 = j
        b1['selectionSort']['swaps'] += 1
        array[b15], array[b10] = array[b10], array[b15]
def fonk7(array, b1, b11 = 0, b12=None):
    if b12 is None:
        b12 = len(array) - 1
    if b11 < b12:
        b13 = fonk8(array, b11, b12, b1)
        fonk7(array, b1, b11, b13 - 1)
        fonk7(array, b1, b13 + 1, b12)
def fonk8(array, b11, b12, b1):
    b14 = array[b12]
    b15 = b11 - 1
    for j in range(b11, b12):
        b1['quickSort']['comparisons'] += 1
        if array[j] < b14:
            b15 += 1
            b1['quickSort']['swaps'] += 1
            array[b15], array[j] = array[j], array[b15]
    b1['quickSort']['swaps'] += 1
    array[b15 + 1], array[b12] = array[b12], array[b15 + 1]
    return b15 + 1
def fonk9(array, b1):
    if len(array) > 1:
        b16 = len(array)
        b17 = array[:b16]
        b18 = array[b16:]
        fonk9(b17, b1)
        fonk9(b18, b1)
        b15 = j = k = 0
        while b15 < len(b17) and j < len(b18):
            b1['mergeSort']['comparisons'] += 1
            if b17[b15] < b18[j]:
                array[k] = b17[b15]
                b15 += 1
            else:
                array[k] = b18[j]
                j += 1
            k += 1
        while b15 < len(b17):
            array[k] = b17[b15]
            b15 += 1
            k += 1
        while j < len(b18):
            array[k] = b18[j]
            j += 1
            k += 1
def fonk10(array, b1):
    array.sort()
if b19 = = "__main__":
    fonk3()