import selection_sort
import insertion_sort
import MERGE
import allInOne
import time
import random
def Main():
    print("\nChoose type of sort to get runtime with specific variables")
    print("1. Insertion sort")
    print("2. Selection Sort")
    print("3. Merge Sort")
    print("4. Draw all of their run time graph with 10**k where k = 1,2,3,4,5")
    x = int(input('>>> '))
    if x == 4:
        chooseSortType(x, generateRandomArrays(1, 1))
    else:
        size = setSize()
        rng = setRange()
        print('\nArray Size:', 10**size, "Range 0 -", 10**rng)
        createArray = generateRandomArrays(10**rng, 10**size)
        chooseSortType(x, createArray)
def generateRandomArrays(length, rng):
    return [random.randint(0, length) for i in range(rng)]
def callInsertionSort(lst):
    start_time = time.time()
    insertion_sort.insertionSort(lst)
    insertionSort_time = (time.time() - start_time)
    print("\nInsertion Sort --- %s  ---\n" % insertionSort_time)
    print("\n")
def callSelectionSort(lst):
    start_time = time.time()
    selection_sort.selectionSort(lst)
    selectionSort_time = (time.time() - start_time)
    print("\nSelection Sort --- %s  ---\n" % selectionSort_time)
    print("\n")
def callMergeSort(lst):
    start_time = time.time()
    MERGE.mergeSort(lst)
    mergeSort_time = (time.time() - start_time)
    print("\nMerge Sort --- %s  ---\n" % mergeSort_time)
    print("\n")
def setSize():
    while True:
        try:
            return int(input('Enter the array size (10**size): '))
        except ValueError:
            print("Not a number")
def setRange():
    while True:
        try:
            return int(input('Define the range (0 to ...): '))
        except ValueError:
            print("Not a number")
def chooseSortType(x, lst):
    if x == 1:
        return callInsertionSort(lst)
    elif x == 2:
        return callSelectionSort(lst)
    elif x == 3:
        return callMergeSort(lst)
    elif x == 4:
        return allOFthem()
    else:
        print("Wrong sort code")
def allOFthem():
    allInOne.drawAllGraph()
if __name__ == '__main__':
    Main()