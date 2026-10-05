import selection_sort
import insertion_sort
import merge_sort
import all_in_one
import time
import random
def main():
    print("\nChoose the type of sort to measure runtime with specific variables:")
    print("1. Insertion sort")
    print("2. Selection sort")
    print("3. Merge sort")
    print("4. Draw all their runtime graphs with 10**k where k = 1, 2, 3, 4, 5")
    sort_type = int(input('>>> '))
    if sort_type == 4:
        choose_sort_type(sort_type, generate_random_arrays(1, 1))
    else:
        size = set_size()
        rng = set_range()
        print('\nArray Size:', 10**size, "Range 0 -", 10**rng)
        create_array = generate_random_arrays(10**rng, 10**size)
        choose_sort_type(sort_type, create_array)
def generate_random_arrays(length, rng):
    return [random.randint(0, length) for _ in range(rng)]
def call_insertion_sort(lst):
    start_time = time.time()
    insertion_sort.insertionSort(lst)
    execution_time = (time.time() - start_time)
    print("\nInsertion Sort --- %s  ---\n" % execution_time)
    print("\n")
def call_selection_sort(lst):
    start_time = time.time()
    selection_sort.selectionSort(lst)
    execution_time = (time.time() - start_time)
    print("\nSelection Sort --- %s  ---\n" % execution_time)
    print("\n")
def call_merge_sort(lst):
    start_time = time.time()
    merge_sort.mergeSort(lst)
    execution_time = (time.time() - start_time)
    print("\nMerge Sort --- %s  ---\n" % execution_time)
    print("\n")
def set_size():
    while True:
        try:
            return int(input('Enter the array size (10**size): '))
        except ValueError:
            print("Please enter a valid number.")
def set_range():
    while True:
        try:
            return int(input('Define the range (0 to ...): '))
        except ValueError:
            print("Please enter a valid number.")
def choose_sort_type(sort_type, lst):
    if sort_type == 1:
        return call_insertion_sort(lst)
    elif sort_type == 2:
        return call_selection_sort(lst)
    elif sort_type == 3:
        return call_merge_sort(lst)
    elif sort_type == 4:
        return draw_all_of_them()
    else:
        print("Wrong sort code.")
def draw_all_of_them():
    all_in_one.drawAllGraph()
if __name__ == '__main__':
    main()