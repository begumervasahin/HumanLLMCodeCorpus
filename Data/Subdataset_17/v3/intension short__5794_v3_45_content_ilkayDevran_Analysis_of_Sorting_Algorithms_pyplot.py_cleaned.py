import selection_sort
import insertion_sort
import MERGE
import allInOne
import time
import random
def main():
    print()
    choice = get_user_choice()
    if choice == 4:
        draw_all_sort_graphs()
    else:
        array_size = get_array_size()
        value_range = get_array_range()
        print(f'\nArray Size: {10**array_size}, Range: 0 - {10**value_range}')
        array = generate_random_array(10**value_range, 10**array_size)
        execute_sort_choice(choice, array)
def get_user_choice():
    try:
        return int(input('Enter your choice: '))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return get_user_choice()
def generate_random_array(max_value, size):
    return [random.randint(0, max_value) for _ in range(size)]
def time_function(sort_function, arr):
    start_time = time.time()
    sort_function(arr)
    return time.time() - start_time
def call_insertion_sort(arr):
    duration = time_function(insertion_sort.insertionSort, arr)
    print(f"\nInsertion Sort --- {duration:.6f} seconds ---\n")
def call_selection_sort(arr):
    duration = time_function(selection_sort.selectionSort, arr)
    print(f"\nSelection Sort --- {duration:.6f} seconds ---\n")
def call_merge_sort(arr):
    duration = time_function(MERGE.mergeSort, arr)
    print(f"\nMerge Sort --- {duration:.6f} seconds ---\n")
def get_array_size():
    try:
        return int(input('Enter the exponent for array size (10**size): '))
    except ValueError:
        print("Invalid input. Defaulting to size 0.")
        return 0
def get_array_range():
    try:
        return int(input('Define the exponent for the range (0 to 10**rng): '))
    except ValueError:
        print("Invalid input. Defaulting to range 0.")
        return 0
def execute_sort_choice(choice, arr):
    sort_functions = {
        1: call_insertion_sort,
        2: call_selection_sort,
        3: call_merge_sort
    }
    sort_function = sort_functions.get(choice)
    if sort_function:
        sort_function(arr)
    else:
        print("Invalid choice. Please select a valid option.")
def draw_all_sort_graphs():
    allInOne.drawAllGraph()
if __name__ == '__main__':
    main()