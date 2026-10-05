import random
import time
from bubbleSort import bubbleSort
from selectionSort import selectionSort
from insertionSort import insertionSort
from heapSort import heapSort
from quickSort import quickSort
def get_user_confirmation(question):
    while True:
        reply = input(question + " (y/n): ").strip().lower()
        if reply.startswith('y'):
            return True
        elif reply.startswith('n'):
            return False
        else:
            print("Please enter 'y' for Yes or 'n' for No.")
print()
print("PYTHON SORTING SCRIPTS")
print("----------------------\n")
while True:
    valid_input = False
    while not valid_input:
        try:
            num_elements = int(input("How many numbers do you want in the array? (Enter a number between 2 and 50,000): "))
            if 2 <= num_elements <= 50000:
                valid_input = True
            else:
                print("Invalid input. Please enter a number between 2 and 50,000.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    array = random.sample(range(1, num_elements + 1), num_elements)
    if get_user_confirmation("Do you want to see the array?"):
        print(array)
    for sort_algorithm in [bubbleSort, selectionSort, insertionSort, heapSort, quickSort]:
        start_time = time.time()
        sorted_array = sort_algorithm(array.copy())
        elapsed_time = time.time() - start_time
        print(sorted_array)
        print("Time elapsed:", round(elapsed_time, 4), "seconds\n")
    if not get_user_confirmation("Try again with another array?"):
        break
input("Press Enter to quit...")