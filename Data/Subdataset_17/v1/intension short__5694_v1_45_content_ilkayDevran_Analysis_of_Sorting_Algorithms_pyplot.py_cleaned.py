import selection_sort
import insertion_sort
import MERGE
import allInOne
import time
import random
def main():
    print()
    choice = int(input('>>> '))
    if choice == 4:
        choose_sort_type(choice, generate_random_array(1, 1))
    else:
        size = get_array_size()
        rng = get_array_range()
        print(f'\nArray Size: {10**size}, Range 0 - {10**rng}')
        array = generate_random_array(10**rng, 10**size)
        choose_sort_type(choice, array)
def generate_random_array(length, size):
    return [random.randint(0, length) for _ in range(size)]
def time_function(func, arr):
    start_time = time.time()
    func(arr)
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
        return int(input('Enter the array size (10**size): '))
    except ValueError:
        print("Invalid input. Defaulting to size 0.")
        return 0
def get_array_range():
    try:
        return int(input('Define the range (0 to ...): '))
    except ValueError:
        print("Invalid input. Defaulting to range 0.")
        return 0
def choose_sort_type(choice, arr):
    if choice == 1:
        call_insertion_sort(arr)
    elif choice == 2:
        call_selection_sort(arr)
    elif choice == 3:
        call_merge_sort(arr)
    elif choice == 4:
        all_in_one()
    else:
        print("Invalid choice.")
def all_in_one():
    allInOne.drawAllGraph()
if __name__ == '__main__':
    main()