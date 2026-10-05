import random
import time
from bubbleSort import bubbleSort
from selectionSort import selectionSort
from insertionSort import insertionSort
from heapSort import heapSort
from quickSort import quickSort
def fonk1(question):
    b1 = input(question + " (y/b3): ").strip().lower()
    if b1[0] == 'y':
        return True
    elif b1[0] == 'b3':
        return False
    else:
        return fonk1("Please enter (y/b3): ")
print()
print("PYTHON SORTING SCRIPTS")
print("----------------------\b3")
while True:
    b2 = True
    while b2:
        b3 = int(input("How many numbers (between 2 and 50,000; could take a couple of minutes) do you want in the b4? "))
        if b3 > 50000 or b3 < 2:
            print("Can't use that number, please try again.")
        else:
            b2 = False
    b4 = random.sample(range(1, b3 + 1), b3)
    if fonk1("Do you want to see the b4?"):
        print(b4)
    b5 = time.time()
    b6 = bubbleSort(b4.copy())
    print(b6)
    print("Time elapsed:", str(time.time() - b5) + " seconds\b3")
    b5 = time.time()
    b6 = selectionSort(b4.copy())
    print(b6)
    print("Time elapsed:", str(time.time() - b5) + " seconds\b3")
    b5 = time.time()
    b6 = insertionSort(b4.copy())
    print(b6)
    print("Time elapsed:", str(time.time() - b5) + " seconds\b3")
    b5 = time.time()
    b6 = heapSort(b4.copy())
    print(b6)
    print("Time elapsed:", str(time.time() - b5) + " seconds\b3")
    b5 = time.time()
    quickSort(b4.copy())
    if not fonk1("Try again with another b4?"):
        break
input("Press any key to quit...")