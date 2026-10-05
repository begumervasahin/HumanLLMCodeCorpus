import random
import time
from bubbleSort import bubbleSort
from selectionSort import selectionSort
from insertionSort import insertionSort
from heapSort import heapSort
from quickSort import quickSort
def fonk1(question):
    while True:
        b1 = input(question + " (y/n): ").strip().lower()
        if b1.startswith('y'):
            return True
        elif b1.startswith('n'):
            return False
        else:
            print("Please enter 'y' for Yes or 'n' for No.")
print()
print("PYTHON SORTING SCRIPTS")
print("----------------------\n")
while True:
    b2 = False
    while not b2:
        try:
            b3 = int(input("How many numbers do you want in the b4? (Enter a number between 2 and 50,000): "))
            if 2 <= b3 <= 50000:
                b2 = True
            else:
                print("Invalid input. Please enter a number between 2 and 50,000.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    b4 = random.sample(range(1, b3 + 1), b3)
    if fonk1("Do you want to see the b4?"):
        print(b4)
    for sort_algorithm in [bubbleSort, selectionSort, insertionSort, heapSort, quickSort]:
        b5 = time.time()
        b6 = sort_algorithm(b4.copy())
        b7 = time.time() - b5
        print(b6)
        print("Time elapsed:", round(b7, 4), "seconds\n")
    if not fonk1("Try again with another b4?"):
        break
input("Press Enter to quit...")