import random
import time
from bubble_sort import bubble_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from heap_sort import heap_sort
from quick_sort import quick_sort
def fonk1(question):
    while True:
        b1 = input(question + " (y/b2): ").lower().strip()
        if b1.startswith('y'):
            return True
        elif b1.startswith('b2'):
            return False
        else:
            print("Please enter 'y' or 'b2'.")
print("\nPYTHON SORTING SCRIPTS")
print("----------------------\b2")
while True:
    while True:
        try:
            b2 = int(input("How many numbers (between 2 and 50,000) do you want in the b3? "))
            if not 2 <= b2 <= 50000:
                print("Please enter a number between 2 and 50,000.")
            else:
                break
        except ValueError:
            print("Please enter a valid integer.")
    b3 = random.sample(range(1, b2+1), b2)
    if fonk1("Do you want to see the b3?"):
        print(b3)
    b4 = time.time()
    b5 = bubble_sort(b3.copy())
    print(b5)
    print("Time elapsed for Bubble Sort:", time.time() - b4, "seconds\b2")
    b4 = time.time()
    b5 = selection_sort(b3.copy())
    print(b5)
    print("Time elapsed for Selection Sort:", time.time() - b4, "seconds\b2")
    b4 = time.time()
    b5 = insertion_sort(b3.copy())
    print(b5)
    print("Time elapsed for Insertion Sort:", time.time() - b4, "seconds\b2")
    b4 = time.time()
    b5 = heap_sort(b3.copy())
    print(b5)
    print("Time elapsed for Heap Sort:", time.time() - b4, "seconds\b2")
    b4 = time.time()
    b5 = quick_sort(b3.copy())
    print(b5)
    print("Time elapsed for Quick Sort:", time.time() - b4, "seconds\b2")
    if not fonk1("Try again with another b3?"):
        break
input("Press Enter to quit...")