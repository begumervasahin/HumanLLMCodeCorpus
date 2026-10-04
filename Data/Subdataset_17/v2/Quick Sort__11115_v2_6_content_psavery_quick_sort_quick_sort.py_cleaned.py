import random
import time
import copy
import numpy as np
def quicksort(arr, start, end):
    assert isinstance(start, int), "Starting index must be an integer."
    assert isinstance(end, int), "Ending index must be an integer."
    assert end >= start, "Ending index must be greater than or equal to the starting index."
    assert isinstance(arr, list), "The parameter must be a list."
    if start < end:
        pivot_index = partition(arr, start, end)
        quicksort(arr, start, pivot_index - 1)
        quicksort(arr, pivot_index + 1, end)
def partition(arr, start, end):
    pivot = arr[end]
    low = start - 1
    for high in range(start, end):
        if arr[high] <= pivot:
            low += 1
            arr[low], arr[high] = arr[high], arr[low]
    arr[low + 1], arr[end] = arr[end], arr[low + 1]
    return low + 1
def get_input(prompt):
    while True:
        value = input(prompt)
        if value.isdigit():
            return int(value)
        else:
            print("Invalid number entered. Please try again.\n")
def main():
    list_length = get_input("Enter the length of the list of random numbers to be generated: ")
    first_number = get_input("Enter the smallest number in the range of random numbers to be generated: ")
    last_number = get_input("Enter the largest number in the range of random numbers to be generated: ")
    print(f"\nGenerating a list of {list_length} random numbers between {first_number} and {last_number}.\n")
    random_list1 = [random.randint(first_number, last_number) for _ in range(list_length)]
    random_list2 = copy.deepcopy(random_list1)
    random_list3 = copy.deepcopy(random_list1)
    random_list4 = copy.deepcopy(random_list1)
    with open("generatedLists.txt", "w") as file:
        file.write("=" * 65 + "\n")
        file.write("Unsorted list:\n")
        file.write("=" * 65 + "\n")
        file.write("\n".join(map(str, random_list1)) + "\n")
    print("Starting QuickSort...\n")
    start_time = time.process_time()
    random_index = random.randint(0, len(random_list1) - 1)
    random_list2[random_index], random_list2[-1] = random_list2[-1], random_list2[random_index]
    quicksort(random_list2, 0, len(random_list2) - 1)
    end_time = time.process_time()
    print(f"QuickSort completed in {end_time - start_time:.3f}s\n")
    with open("generatedLists.txt", "a") as file:
        file.write("=" * 65 + "\n")
        file.write("List after QuickSort:\n")
        file.write("=" * 65 + "\n")
        file.write("\n".join(map(str, random_list2)) + "\n")
    start_time = time.process_time()
    random_list3.sort()
    end_time = time.process_time()
    print(f"Built-in sort completed in {end_time - start_time:.3f}s\n")
    start_time = time.process_time()
    np.sort(random_list4)
    end_time = time.process_time()
    print(f"Numpy sort completed in {end_time - start_time:.3f}s\n")
if __name__ == '__main__':
    main()