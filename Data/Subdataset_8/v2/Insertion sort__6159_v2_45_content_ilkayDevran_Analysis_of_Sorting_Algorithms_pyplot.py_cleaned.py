import selection_sort
import insertion_sort
import MERGE
import allInOne
import time
import random
def Main():
    print("\nChoose the type of sort to get runtime with specific variables:")
    print("1. Insertion sort")
    print("2. Selection sort")
    print("3. Merge sort")
    print("4. Draw all of their runtime graphs with 10**k where k = 1, 2, 3, 4, 5")
    sort_type = int(input('>>> '))
    if sort_type == 4:
        chooseSortType(sort_type, generateRandomArrays(1, 1))
    else:
        array_size = setSize()
        value_range = setRange()
        print('\nArray Size:', 10**array_size, "Range 0 -", 10**value_range)
        createArray = generateRandomArrays(10**value_range, 10**array_size)
        chooseSortType(sort_type, createArray)
def generateRandomArrays(length, rng):
    return [random.randint(0, length) for _ in range(rng)]
def callInsertionSort(lst):
    start_time = time.time()
    insertion_sort.insertionSort(lst)
    execution_time = (time.time() - start_time)
    print("\nInsertion Sort --- %s  ---\n" % execution_time)
    print("\n")
def callSelectionSort(lst):
    start_time = time.time()
    selection_sort.selectionSort(lst)
    execution_time = (time.time() - start_time)
    print("\nSelection Sort --- %s  ---\n" % execution_time)
    print("\n")
def callMergeSort(lst):
    start_time = time.time()
    MERGE.mergeSort(lst)
    execution_time = (time.time() - start_time)
    print("\nMerge Sort --- %s  ---\n" % execution_time)
    print("\n")
def setSize():
    while True:
        try:
            return int(input('Enter the array size (10**size): '))
        except ValueError:
            print("Please enter a valid number.")
def setRange():
    while True:
        try:
            return int(input('Define the range (0 to ...): '))
        except ValueError:
            print("Please enter a valid number.")
def chooseSortType(sort_type, lst):
    if sort_type == 1:
        return callInsertionSort(lst)
    elif sort_type == 2:
        return callSelectionSort(lst)
    elif sort_type == 3:
        return callMergeSort(lst)
    elif sort_type == 4:
        return allOFthem()
    else:
        print("Wrong sort code.")
def allOFthem():
    allInOne.drawAllGraph()
if __name__ == '__main__':
    Main()