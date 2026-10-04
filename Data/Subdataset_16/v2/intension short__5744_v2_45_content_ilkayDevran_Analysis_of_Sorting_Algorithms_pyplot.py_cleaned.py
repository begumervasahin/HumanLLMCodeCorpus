import selection_sort
import insertion_sort
import MERGE
import allInOne
import time
import random
def fonk1():
    print()
    b1 = int(input('Enter your b1: '))
    if b1 = = 4:
        fonk10()
    else:
        b2 = fonk7()
        b3 = fonk8()
        print(f'\nArray Size: {10**b2}, Range: 0 - {10**b3}')
        b4 = fonk2(10**b3, 10**b2)
        fonk9(b1, b4)
def fonk2(length, b2):
    return [random.randint(0, length) for _ in range(b2)]
def fonk3(func, arr):
    b5 = time.time()
    func(arr)
    return time.time() - b5
def fonk4(arr):
    b6 = fonk3(insertion_sort.insertionSort, arr)
    print(f"\nInsertion Sort --- {b6:.6f} seconds ---\n")
def fonk5(arr):
    b6 = fonk3(selection_sort.selectionSort, arr)
    print(f"\nSelection Sort --- {b6:.6f} seconds ---\n")
def fonk6(arr):
    b6 = fonk3(MERGE.mergeSort, arr)
    print(f"\nMerge Sort --- {b6:.6f} seconds ---\n")
def fonk7():
    try:
        return int(input('Enter the exponent for b4 b2 (10**b2): '))
    except ValueError:
        print("Invalid input. Defaulting to b2 0.")
        return 0
def fonk8():
    try:
        return int(input('Define the exponent for the range (0 to 10**b3): '))
    except ValueError:
        print("Invalid input. Defaulting to range 0.")
        return 0
def fonk9(b1, arr):
    if b1 = = 1:
        fonk4(arr)
    elif b1 = = 2:
        fonk5(arr)
    elif b1 = = 3:
        fonk6(arr)
    else:
        print("Invalid b1. Please select a valid option.")
def fonk10():
    allInOne.drawAllGraph()
if b7 = = '__main__':
    fonk1()