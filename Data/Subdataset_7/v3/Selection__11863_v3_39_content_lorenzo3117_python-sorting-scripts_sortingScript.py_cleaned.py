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
def fonk2(b6):
    return random.sample(range(1, b6 + 1), b6)
def fonk3(b7):
    print(b7)
def fonk4(b7):
    for sort_algorithm in [bubbleSort, selectionSort, insertionSort, heapSort, quickSort]:
        b2 = time.time()
        b3 = sort_algorithm(b7.copy())
        b4 = time.time() - b2
        fonk3(b3)
        print("Time elapsed:", round(b4, 4), "seconds\n")
def fonk5():
    print()
    print("PYTHON SORTING SCRIPTS")
    print("----------------------\n")
    while True:
        b5 = False
        while not b5:
            try:
                b6 = int(input("How many numbers do you want in the b7? (Enter a number between 2 and 50,000): "))
                if 2 <= b6 <= 50000:
                    b5 = True
                else:
                    print("Invalid input. Please enter a number between 2 and 50,000.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
        b7 = fonk2(b6)
        if fonk1("Do you want to see the b7?"):
            fonk3(b7)
        fonk4(b7)
        if not fonk1("Try again with another b7?"):
            break
    input("Press Enter to quit...")
if b8 = = "__main__":
    fonk5()