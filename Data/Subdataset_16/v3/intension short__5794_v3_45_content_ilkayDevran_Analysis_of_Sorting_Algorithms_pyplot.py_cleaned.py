import selection_sort
import insertion_sort
import MERGE
import allInOne
import time
import random
def fonk1():
    print()
    b1 = fonk2()
    if b1 = = 4:
        fonk11()
    else:
        b2 = fonk8()
        b3 = fonk9()
        print(f'\nArray Size: {10**b2}, Range: 0 - {10**b3}')
        b4 = fonk3(10**b3, 10**b2)
        fonk10(b1, b4)
def fonk2():
    try:
        return int(input('Enter your b1: '))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return fonk2()
def fonk3(max_value, size):
    return [random.randint(0, max_value) for _ in range(size)]
def fonk4(b8, arr):
    b5 = time.time()
    b8(arr)
    return time.time() - b5
def fonk5(arr):
    b6 = fonk4(insertion_sort.insertionSort, arr)
    print(f"\nInsertion Sort --- {b6:.6f} seconds ---\n")
def fonk6(arr):
    b6 = fonk4(selection_sort.selectionSort, arr)
    print(f"\nSelection Sort --- {b6:.6f} seconds ---\n")
def fonk7(arr):
    b6 = fonk4(MERGE.mergeSort, arr)
    print(f"\nMerge Sort --- {b6:.6f} seconds ---\n")
def fonk8():
    try:
        return int(input('Enter the exponent for b4 size (10**size): '))
    except ValueError:
        print("Invalid input. Defaulting to size 0.")
        return 0
def fonk9():
    try:
        return int(input('Define the exponent for the range (0 to 10**rng): '))
    except ValueError:
        print("Invalid input. Defaulting to range 0.")
        return 0
def fonk10(b1, arr):
    b7 = {
        1: call_insertion_sort,
        2: call_selection_sort,
        3: call_merge_sort
    }
    b8 = b7.get(b1)
    if b8:
        b8(arr)
    else:
        print("Invalid b1. Please select a valid option.")
def fonk11():
    allInOne.drawAllGraph()
if b9 = = '__main__':
    fonk1()