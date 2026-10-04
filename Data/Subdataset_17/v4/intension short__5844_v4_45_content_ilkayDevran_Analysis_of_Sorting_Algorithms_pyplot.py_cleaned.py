import selection_sort
import insertion_sort
import MERGE
import allInOne
import time
import random
def main():
    print()
    try:
        choice = int(input('>>> '))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 4.")
        return
    if choice == 4:
        allInOne.drawAllGraph()
    else:
        array_size = get_array_size()
        array_range = get_array_range()
        print(f'\nArray Size: {10 ** array_size}, Range: 0 - {10 ** array_range}')
        array = generate_random_array(10 ** array_range, 10 ** array_size)
        execute_sort(choice, array)
def generate_random_array(length, size):
    return [random.randint(0, length) for _ in range(size)]
def measure_runtime(sort_function, data, sort_name):
    start_time = time.time()
    sort_function(data)
    elapsed_time = time.time() - start_time
    print(f"\n{sort_name} --- {elapsed_time:.6f} seconds ---\n")
def call_insertion_sort(data):
    measure_runtime(insertion_sort.insertionSort, data, "Insertion Sort")
def call_selection_sort(data):
    measure_runtime(selection_sort.selectionSort, data, "Selection Sort")
def call_merge_sort(data):
    measure_runtime(MERGE.mergeSort, data, "Merge Sort")
def get_array_size():
    try:
        return int(input('Enter the array size exponent (10**size): '))
    except ValueError:
        print("Invalid input. Using default size exponent: 0")
        return 0
def get_array_range():
    try:
        return int(input('Enter the array range exponent (0 to 10**range): '))
    except ValueError:
        print("Invalid input. Using default range exponent: 0")
        return 0
def execute_sort(choice, data):
    if choice == 1:
        call_insertion_sort(data)
    elif choice == 2:
        call_selection_sort(data)
    elif choice == 3:
        call_merge_sort(data)
    else:
        print("Invalid choice. Please select a valid sorting algorithm.")
if __name__ == '__main__':
    main()