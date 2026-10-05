import random
import time
from bubbleSort import bubbleSort
from selectionSort import selectionSort
from insertionSort import insertionSort
from heapSort import heapSort
from quickSort import quickSort
def yes_no(question):
    reply = input(question + " (y/n): ").strip().lower()
    if reply[0] == 'y':
        return True
    elif reply[0] == 'n':
        return False
    else:
        return yes_no("Please enter (y/n): ")
print()
print("PYTHON SORTING SCRIPTS")
print("----------------------\n")
while True:
    valid_input = True
    while valid_input:
        n = int(input("How many numbers (between 2 and 50,000; could take a couple of minutes) do you want in the array? "))
        if n > 50000 or n < 2:
            print("Can't use that number, please try again.")
        else:
            valid_input = False
    array = random.sample(range(1, n + 1), n)
    if yes_no("Do you want to see the array?"):
        print(array)
    start = time.time()
    sorted_array = bubbleSort(array.copy())
    print(sorted_array)
    print("Time elapsed:", str(time.time() - start) + " seconds\n")
    start = time.time()
    sorted_array = selectionSort(array.copy())
    print(sorted_array)
    print("Time elapsed:", str(time.time() - start) + " seconds\n")
    start = time.time()
    sorted_array = insertionSort(array.copy())
    print(sorted_array)
    print("Time elapsed:", str(time.time() - start) + " seconds\n")
    start = time.time()
    sorted_array = heapSort(array.copy())
    print(sorted_array)
    print("Time elapsed:", str(time.time() - start) + " seconds\n")
    start = time.time()
    quickSort(array.copy())
    if not yes_no("Try again with another array?"):
        break
input("Press any key to quit...")