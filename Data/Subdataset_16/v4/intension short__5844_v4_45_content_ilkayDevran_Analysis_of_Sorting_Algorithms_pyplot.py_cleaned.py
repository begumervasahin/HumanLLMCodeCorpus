import selection_sort
import insertion_sort
import MERGE
import allInOne
import time
import random
def fonk1():
    print()
    try:
        b1 = int(input('>>> '))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 4.")
        return
    if b1 = = 4:
        allInOne.drawAllGraph()
    else:
        b2 = fonk7()
        b3 = fonk8()
        print(f'\nArray Size: {10 ** b2}, Range: 0 - {10 ** b3}')
        b4 = fonk2(10 ** b3, 10 ** b2)
        fonk9(b1, b4)
def fonk2(length, size):
    return [random.randint(0, length) for _ in range(size)]
def fonk3(sort_function, data, sort_name):
    b5 = time.time()
    sort_function(data)
    b6 = time.time() - b5
    print(f"\n{sort_name} --- {b6:.6f} seconds ---\n")
def fonk4(data):
    fonk3(insertion_sort.insertionSort, data, "Insertion Sort")
def fonk5(data):
    fonk3(selection_sort.selectionSort, data, "Selection Sort")
def fonk6(data):
    fonk3(MERGE.mergeSort, data, "Merge Sort")
def fonk7():
    try:
        return int(input('Enter the b4 size exponent (10**size): '))
    except ValueError:
        print("Invalid input. Using default size exponent: 0")
        return 0
def fonk8():
    try:
        return int(input('Enter the b4 range exponent (0 to 10**range): '))
    except ValueError:
        print("Invalid input. Using default range exponent: 0")
        return 0
def fonk9(b1, data):
    if b1 = = 1:
        fonk4(data)
    elif b1 = = 2:
        fonk5(data)
    elif b1 = = 3:
        fonk6(data)
    else:
        print("Invalid b1. Please select a valid sorting algorithm.")
if b7 = = '__main__':
    fonk1()