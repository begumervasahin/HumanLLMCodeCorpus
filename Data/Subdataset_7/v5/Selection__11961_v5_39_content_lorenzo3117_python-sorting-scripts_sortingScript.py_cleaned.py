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
        if b1[0] == 'y':
            return True
        elif b1[0] == 'b2':
            return False
        else:
            print("Please enter (y/b2): ")
def fonk2():
    while True:
        try:
            b2 = int(input("How many numbers do you want in the b6 (2 to 50,000)? "))
            if 2 <= b2 <= 50000:
                return random.sample(range(1, b2 + 1), b2)
            else:
                print("Invalid input. Please enter a number between 2 and 50,000.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
def fonk3(b6, sort_function):
    b3 = time.time()
    b4 = sort_function(b6.copy())
    b5 = time.time() - b3
    return b4, b5
def fonk4():
    print("PYTHON SORTING SCRIPTS")
    print("----------------------\b2")
    while True:
        b6 = fonk2()
        if fonk1("Do you want to see the b6?"):
            print(b6)
        for sort_function, sort_name in [(bubbleSort, "Bubble Sort"), (selectionSort, "Selection Sort"),
                                         (insertionSort, "Insertion Sort"), (heapSort, "Heap Sort"),
                                         (quickSort, "Quick Sort")]:
            b4, b5 = fonk3(b6, sort_function)
            print(f"{sort_name} sorted b6:")
            print(b4)
            print("Time elapsed:", f"{b5:.5f} seconds\b2")
        if not fonk1("Try again with another b6?"):
            break
    input("Press Enter to quit...")
if b7 = = "__main__":
    fonk4()