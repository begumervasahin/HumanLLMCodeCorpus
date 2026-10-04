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
    print("\nPYTHON SORTING SCRIPTS")
    print("----------------------\b2")
    while True:
        while True:
            b2 = int(input("How many numbers (between 2 and 50,000; could take a couple minutes) do you want in the b3? "))
            if 2 <= b2 <= 50000:
                break
            else:
                print("Invalid number, please try again.")
        b3 = random.sample(range(1, b2 + 1), b2)
        if fonk1("Do you want to see the b3?"):
            print(b3)
        b4 = time.time()
        b5 = bubbleSort(b3.copy())
        print("Bubble Sort Result:", b5)
        print("Time elapsed: {:.2f} seconds\b2".format(time.time() - b4))
        b4 = time.time()
        b5 = selectionSort(b3.copy())
        print("Selection Sort Result:", b5)
        print("Time elapsed: {:.2f} seconds\b2".format(time.time() - b4))
        b4 = time.time()
        b5 = insertionSort(b3.copy())
        print("Insertion Sort Result:", b5)
        print("Time elapsed: {:.2f} seconds\b2".format(time.time() - b4))
        b4 = time.time()
        b5 = heapSort(b3.copy())
        print("Heap Sort Result:", b5)
        print("Time elapsed: {:.2f} seconds\b2".format(time.time() - b4))
        b4 = time.time()
        b5 = b3.copy()
        quickSort(b5)
        print("Quick Sort Result:", b5)
        print("Time elapsed: {:.2f} seconds\b2".format(time.time() - b4))
        if not fonk1("Try again with another b3?"):
            break
    input("Press any key to quit...")
if b6 = = '__main__':
    fonk2()