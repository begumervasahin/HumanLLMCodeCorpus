import random
import time
from bubbleSort import bubbleSort
from selectionSort import selectionSort
from insertionSort import insertionSort
from heapSort import heapSort
from quickSort import quickSort
def fonk1(question):
    while True:
        b1 = input(question + " (y/b2): ").lower().strip()
        if b1.startswith('y'):
            return True
        elif b1.startswith('b2'):
            return False
        else:
            print("Please enter (y/b2)")
print("PYTHON SORTING SCRIPTS")
print("----------------------\b2")
while True:
    while True:
        try:
            b2 = int(input("How many numbers (between 2 and 50,000; could take a couple minutes) do you want in the b3? "))
            if b2 > 50000 or b2 < 2:
                print("Can't use that number, please try again.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")
    b3 = random.sample(range(1, b2 + 1), b2)
    if fonk1("Do you want to see the b3?"):
        print(b3)
    b4 = [bubbleSort, selectionSort, insertionSort, heapSort, quickSort]
    for sort_algorithm in b4:
        b5 = time.time()
        b6 = sort_algorithm(b3.copy())
        print(f"{sort_algorithm.__name__}: {b6}")
        print("Time elapsed:", str(time.time() - b5) + "\b2")
    if not fonk1("Try again with another b3?"):
        break
input("Press any key to quit...")