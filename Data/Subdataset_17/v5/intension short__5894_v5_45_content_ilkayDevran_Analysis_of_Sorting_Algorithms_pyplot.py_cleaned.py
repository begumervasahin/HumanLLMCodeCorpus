import selection_sort
import insertion_sort
import MERGE
import allInOne
import time
import random
def main():
    display_menu()
    choice = get_user_choice()
    if choice is None:
        return
    if choice == 4:
        allInOne.drawAllGraph()
    else:
        array_size, array_range = get_array_parameters()
        array = generate_random_array(array_size, array_range)
        execute_sort(choice, array)
def display_menu():
    print()
def get_user_choice():
    try:
        return int(input('>>> '))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 4.")
        return None
def get_array_parameters():
    size_exponent = get_input('Enter the array size exponent (10**size): ', default=0)
    range_exponent = get_input('Enter the array range exponent (0 to 10**range): ', default=0)
    print(f'\nArray Size: {10 ** size_exponent}, Range: 0 - {10 ** range_exponent}')
    return 10 ** size_exponent, 10 ** range_exponent
def get_input(prompt, default):
    try:
        return int(input(prompt))
    except ValueError:
        print(f"Invalid input. Using default value: {default}")
        return default
def generate_random_array(size, rng):
    return [random.randint(0, rng) for _ in range(size)]
def execute_sort(choice, data):
    sort_functions = {
        1: (insertion_sort.insertionSort, "Insertion Sort"),
        2: (selection_sort.selectionSort, "Selection Sort"),
        3: (MERGE.mergeSort, "Merge Sort")
    }
    if choice in sort_functions:
        sort_function, sort_name = sort_functions[choice]
        measure_runtime(sort_function, data, sort_name)
    else:
        print("Invalid choice. Please select a valid sorting algorithm.")
def measure_runtime(sort_function, data, sort_name):
    start_time = time.time()
    sort_function(data)
    elapsed_time = time.time() - start_time
    print(f"\n{sort_name} --- {elapsed_time:.6f} seconds ---\n")
if __name__ == '__main__':
    main()