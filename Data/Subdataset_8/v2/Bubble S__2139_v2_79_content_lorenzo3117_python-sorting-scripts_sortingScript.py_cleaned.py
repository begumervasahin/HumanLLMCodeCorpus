import random
import time
from bubble_sort import bubble_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from heap_sort import heap_sort
from quick_sort import quick_sort
def get_user_confirmation(question):
    while True:
        reply = input(question + " (y/n): ").lower().strip()
        if reply.startswith('y'):
            return True
        elif reply.startswith('n'):
            return False
        else:
            print("Please enter 'y' or 'n'.")
print("\nPYTHON SORTING SCRIPTS")
print("----------------------\n")
while True:
    while True:
        try:
            n = int(input("How many numbers (between 2 and 50,000) do you want in the array? "))
            if not 2 <= n <= 50000:
                print("Please enter a number between 2 and 50,000.")
            else:
                break
        except ValueError:
            print("Please enter a valid integer.")
    array = random.sample(range(1, n+1), n)
    if get_user_confirmation("Do you want to see the array?"):
        print(array)
    start_time = time.time()
    sorted_array = bubble_sort(array.copy())
    print(sorted_array)
    print("Time elapsed for Bubble Sort:", time.time() - start_time, "seconds\n")
    start_time = time.time()
    sorted_array = selection_sort(array.copy())
    print(sorted_array)
    print("Time elapsed for Selection Sort:", time.time() - start_time, "seconds\n")
    start_time = time.time()
    sorted_array = insertion_sort(array.copy())
    print(sorted_array)
    print("Time elapsed for Insertion Sort:", time.time() - start_time, "seconds\n")
    start_time = time.time()
    sorted_array = heap_sort(array.copy())
    print(sorted_array)
    print("Time elapsed for Heap Sort:", time.time() - start_time, "seconds\n")
    start_time = time.time()
    sorted_array = quick_sort(array.copy())
    print(sorted_array)
    print("Time elapsed for Quick Sort:", time.time() - start_time, "seconds\n")
    if not get_user_confirmation("Try again with another array?"):
        break
input("Press Enter to quit...")