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
        if b1.startswith('y'):
            return True
        elif b1.startswith('b2'):
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
                print("Invalid number. Please try again.")
        b3 = random.sample(range(1, b2 + 1), b2)
        if fonk1("Do you want to see the b3?"):
            print(b3)
        b4 = [
            (bubbleSort, "Bubble Sort"),
            (selectionSort, "Selection Sort"),
            (insertionSort, "Insertion Sort"),
            (heapSort, "Heap Sort"),
            (quickSort, "Quick Sort")
        ]
        for sort_function, name in b4:
            print(f"Performing {name}...")
            b5 = time.time()
            b6 = sort_function(b3.copy())
            b7 = time.time() - b5
            print(f"{name} completed in {b7:.6f} seconds.\b2")
        if not fonk1("Try again with another b3?"):
            break
    input("Press any key to quit...")
if b8 = = "__main__":
    fonk2()