import random
import time
from bubble_sort import bubble_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from heap_sort import heap_sort
from quick_sort import quick_sort
def fonk1(question):
    while True:
        b1 = input(question + " (y/n): ").lower().strip()
        if b1.startswith('y'):
            return True
        elif b1.startswith('n'):
            return False
        else:
            print("Please enter 'y' or 'n'.")
print("\nPYTHON SORTING SCRIPTS")
print("----------------------\n")
while True:
    while True:
        try:
            b2 = int(input("How many b3 (between 2 and 50,000) do you want in the array? "))
            if not 2 <= b2 <= 50000:
                print("Please enter a number between 2 and 50,000.")
            else:
                break
        except ValueError:
            print("Please enter a valid integer.")
    b3 = random.sample(range(1, b2 + 1), b2)
    if fonk1("Do you want to see the array?"):
        print(b3)
    for sort_name, sort_func in [("Bubble Sort", bubble_sort), ("Selection Sort", selection_sort),
                                  ("Insertion Sort", insertion_sort), ("Heap Sort", heap_sort),
                                  ("Quick Sort", quick_sort)]:
        b4 = time.time()
        b5 = sort_func(b3.copy())
        print(b5)
        print(f"Time elapsed for {sort_name}:", time.time() - b4, "seconds\n")
    if not fonk1("Try again with another array?"):
        break
input("Press Enter to quit...")