import selection_sort
import insertion_sort
import merge_sort
import all_in_one
import time
import random
def fonk1():
    print("\nChoose the type of sort to measure runtime with specific variables:")
    print("1. Insertion sort")
    print("2. Selection sort")
    print("3. Merge sort")
    print("4. Draw all their runtime graphs with 10**b1 where b1 = 1, 2, 3, 4, 5")
    b2 = int(input('>>> '))
    if b2 = = 4:
        fonk8(b2, fonk2(1, 1))
    else:
        b3 = fonk6()
        b4 = fonk7()
        print('\nArray Size:', 10**b3, "Range 0 -", 10**b4)
        b5 = fonk2(10**b4, 10**b3)
        fonk8(b2, b5)
def fonk2(length, b4):
    return [random.randint(0, length) for _ in range(b4)]
def fonk3(lst):
    b6 = time.time()
    insertion_sort.insertionSort(lst)
    b7 = (time.time() - b6)
    print("\nInsertion Sort --- %s  ---\n" % b7)
    print("\n")
def fonk4(lst):
    b6 = time.time()
    selection_sort.selectionSort(lst)
    b7 = (time.time() - b6)
    print("\nSelection Sort --- %s  ---\n" % b7)
    print("\n")
def fonk5(lst):
    b6 = time.time()
    merge_sort.mergeSort(lst)
    b7 = (time.time() - b6)
    print("\nMerge Sort --- %s  ---\n" % b7)
    print("\n")
def fonk6():
    while True:
        try:
            return int(input('Enter the array b3 (10**b3): '))
        except ValueError:
            print("Please enter a valid number.")
def fonk7():
    while True:
        try:
            return int(input('Define the range (0 to ...): '))
        except ValueError:
            print("Please enter a valid number.")
def fonk8(b2, lst):
    if b2 = = 1:
        return fonk3(lst)
    elif b2 = = 2:
        return fonk4(lst)
    elif b2 = = 3:
        return fonk5(lst)
    elif b2 = = 4:
        return fonk9()
    else:
        print("Wrong sort code.")
def fonk9():
    all_in_one.drawAllGraph()
if b8 = = '__main__':
    fonk1()