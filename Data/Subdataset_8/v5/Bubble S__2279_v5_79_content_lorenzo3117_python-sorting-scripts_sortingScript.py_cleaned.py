import random
import time
from bubbleSort import bubbleSort
from selectionSort import selectionSort
from insertionSort import insertionSort
from heapSort import heapSort
from quickSort import quickSort
def yes_no(question):
    while True:
        reply = input(question + " (y/n): ").lower().strip()
        if reply.startswith('y'):
            return True
        elif reply.startswith('n'):
            return False
        else:
            print("Please enter (y/n)")
print("PYTHON SORTING SCRIPTS")
print("----------------------\n")
while True:
    while True:
        try:
            n = int(input("How many numbers (between 2 and 50,000; could take a couple minutes) do you want in the array? "))
            if n > 50000 or n < 2:
                print("Can't use that number, please try again.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")
    array = random.sample(range(1, n + 1), n)
    if yes_no("Do you want to see the array?"):
        print(array)
    algorithms = [bubbleSort, selectionSort, insertionSort, heapSort, quickSort]
    for sort_algorithm in algorithms:
        start = time.time()
        sorted_array = sort_algorithm(array.copy())
        print(f"{sort_algorithm.__name__}: {sorted_array}")
        print("Time elapsed:", str(time.time() - start) + "\n")
    if not yes_no("Try again with another array?"):
        break
input("Press any key to quit...")