import selection_sort
import insertion_sort
import MERGE
import allInOne
import time
import random
def fonk1():
    fonk2()
    b1 = fonk3()
    if b1 is None:
        return
    if b1 = = 4:
        allInOne.drawAllGraph()
    else:
        array_size, b2 = fonk4()
        b3 = fonk6(array_size, b2)
        fonk7(b1, b3)
def fonk2():
    print()
def fonk3():
    try:
        return int(input('>>> '))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 4.")
        return None
def fonk4():
    b4 = fonk5('Enter the b3 size exponent (10**size): ', default=0)
    b5 = fonk5('Enter the b3 range exponent (0 to 10**range): ', default=0)
    print(f'\nArray Size: {10 ** b4}, Range: 0 - {10 ** b5}')
    return 10 ** b4, 10 ** b5
def fonk5(prompt, default):
    try:
        return int(input(prompt))
    except ValueError:
        print(f"Invalid input. Using default value: {default}")
        return default
def fonk6(size, rng):
    return [random.randint(0, rng) for _ in range(size)]
def fonk7(b1, data):
    b6 = {
        1: (insertion_sort.insertionSort, "Insertion Sort"),
        2: (selection_sort.selectionSort, "Selection Sort"),
        3: (MERGE.mergeSort, "Merge Sort")
    }
    if b1 in b6:
        sort_function, b7 = b6[b1]
        fonk8(sort_function, data, b7)
    else:
        print("Invalid b1. Please select a valid sorting algorithm.")
def fonk8(sort_function, data, b7):
    b8 = time.time()
    sort_function(data)
    b9 = time.time() - b8
    print(f"\n{b7} --- {b9:.6f} seconds ---\n")
if b10 = = '__main__':
    fonk1()