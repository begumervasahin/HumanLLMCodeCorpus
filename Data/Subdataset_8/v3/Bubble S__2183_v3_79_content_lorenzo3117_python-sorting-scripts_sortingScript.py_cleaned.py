import random
import time
from bubble_sort import bubble_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from heap_sort import heap_sort
from quick_sort import quick_sort
def ask_yes_no_question(question):
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
            num_numbers = int(input("How many numbers (between 2 and 50,000) do you want in the array? "))
            if not 2 <= num_numbers <= 50000:
                print("Please enter a number between 2 and 50,000.")
            else:
                break
        except ValueError:
            print("Please enter a valid integer.")
    numbers = random.sample(range(1, num_numbers + 1), num_numbers)
    if ask_yes_no_question("Do you want to see the array?"):
        print(numbers)
    for sort_name, sort_func in [("Bubble Sort", bubble_sort), ("Selection Sort", selection_sort),
                                  ("Insertion Sort", insertion_sort), ("Heap Sort", heap_sort),
                                  ("Quick Sort", quick_sort)]:
        start_time = time.time()
        sorted_array = sort_func(numbers.copy())
        print(sorted_array)
        print(f"Time elapsed for {sort_name}:", time.time() - start_time, "seconds\n")
    if not ask_yes_no_question("Try again with another array?"):
        break
input("Press Enter to quit...")