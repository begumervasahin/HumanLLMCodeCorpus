import random
import time
from bubbleSort import bubbleSort
from selectionSort import selectionSort
from insertionSort import insertionSort
from heapSort import heapSort
from quickSort import quickSort
def ask_yes_no(question):
    while True:
        reply = input(question + " (y/n): ").strip().lower()
        if reply[0] == 'y':
            return True
        elif reply[0] == 'n':
            return False
        else:
            print("Please enter (y/n): ")
def generate_random_array():
    while True:
        try:
            n = int(input("How many numbers do you want in the array (2 to 50,000)? "))
            if 2 <= n <= 50000:
                return random.sample(range(1, n + 1), n)
            else:
                print("Invalid input. Please enter a number between 2 and 50,000.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
def sort_and_measure_time(array, sort_function):
    start_time = time.time()
    sorted_array = sort_function(array.copy())
    elapsed_time = time.time() - start_time
    return sorted_array, elapsed_time
def main():
    print("PYTHON SORTING SCRIPTS")
    print("----------------------\n")
    while True:
        array = generate_random_array()
        if ask_yes_no("Do you want to see the array?"):
            print(array)
        for sort_function, sort_name in [(bubbleSort, "Bubble Sort"), (selectionSort, "Selection Sort"),
                                         (insertionSort, "Insertion Sort"), (heapSort, "Heap Sort"),
                                         (quickSort, "Quick Sort")]:
            sorted_array, elapsed_time = sort_and_measure_time(array, sort_function)
            print(f"{sort_name} sorted array:")
            print(sorted_array)
            print("Time elapsed:", f"{elapsed_time:.5f} seconds\n")
        if not ask_yes_no("Try again with another array?"):
            break
    input("Press Enter to quit...")
if __name__ == "__main__":
    main()