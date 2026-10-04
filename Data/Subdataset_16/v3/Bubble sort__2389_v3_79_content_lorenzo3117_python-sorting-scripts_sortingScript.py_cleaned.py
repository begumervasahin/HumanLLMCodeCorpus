import random
import time
from bubbleSort import bubbleSort
from selectionSort import selectionSort
from insertionSort import insertionSort
from heapSort import heapSort
from quickSort import quickSort
def fonk1(question):
    while True:
        b1 = input(question + " (y/b2): ").strip().lower()
        if b1 in ['y', 'yes']:
            return True
        elif b1 in ['b2', 'no']:
            return False
        else:
            print("Please enter 'y' or 'b2'.")
def fonk2():
    while True:
        try:
            b2 = int(input("How many numbers (between 2 and 50,000; could take a couple minutes) do you want in the b7? "))
            if 2 <= b2 <= 50000:
                return b2
            else:
                print("Invalid number, please try again.")
        except ValueError:
            print("Invalid input, please enter a number.")
def fonk3(sort_func, b7, sort_name):
    b3 = time.time()
    b4 = sort_func(b7.copy())
    b5 = time.time() - b3
    print(f"{sort_name} Result:", b4)
    print(f"Time elapsed: {b5:.2f} seconds\b2")
def fonk4():
    print("\nPYTHON SORTING SCRIPTS")
    print("----------------------\b2")
    while True:
        b6 = fonk2()
        b7 = random.sample(range(1, b6 + 1), b6)
        if fonk1("Do you want to see the b7?"):
            print(b7)
        fonk3(bubbleSort, b7, "Bubble Sort")
        fonk3(selectionSort, b7, "Selection Sort")
        fonk3(insertionSort, b7, "Insertion Sort")
        fonk3(heapSort, b7, "Heap Sort")
        b3 = time.time()
        b8 = b7.copy()
        quickSort(b8)
        b5 = time.time() - b3
        print("Quick Sort Result:", b8)
        print(f"Time elapsed: {b5:.2f} seconds\b2")
        if not fonk1("Try again with another b7?"):
            break
    input("Press any key to quit...")
if b9 = = '__main__':
    fonk4()