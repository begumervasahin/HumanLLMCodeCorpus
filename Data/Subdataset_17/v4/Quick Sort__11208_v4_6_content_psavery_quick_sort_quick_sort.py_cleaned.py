import random
import time
import copy
import numpy as np
def quicksort(arr, start, finish):
    assert isinstance(start, int), "Starting index must be an integer."
    assert isinstance(finish, int), "Ending index must be an integer."
    assert finish > start, "Ending index must be greater than starting index."
    assert isinstance(arr, list), "List parameter must be a list."
    comparison_index = start
    swap_index = start
    while comparison_index != finish:
        if arr[comparison_index] <= arr[finish]:
            arr[comparison_index], arr[swap_index] = arr[swap_index], arr[comparison_index]
            swap_index += 1
        comparison_index += 1
    arr[swap_index], arr[finish] = arr[finish], arr[swap_index]
    if start < swap_index - 1:
        quicksort(arr, start, swap_index - 1)
    if swap_index + 1 < finish:
        quicksort(arr, swap_index + 1, finish)
def get_input(prompt, error_message):
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            return int(user_input)
        else:
            print(error_message)
def main():
    error_message = "Invalid number entered. Please try again.\n"
    list_length = get_input("\nEnter the length of the list of random numbers to be generated.\n", error_message)
    first_number = get_input("\nEnter the smallest number in the range of random numbers to be generated.\n", error_message)
    last_number = get_input("\nEnter the largest number in the range of random numbers to be generated.\n", error_message)
    print(f"\nGenerating a list of random numbers of length {list_length}, with numbers between {first_number} and {last_number}.\n")
    rand_list1 = [random.randrange(first_number, last_number) for _ in range(list_length)]
    rand_list2 = copy.deepcopy(rand_list1)
    rand_list3 = copy.deepcopy(rand_list1)
    rand_list4 = copy.deepcopy(rand_list1)
    with open("generatedLists.txt", "w") as my_file:
        banner = "=" * 65 + "\n"
        my_file.write(banner)
        my_file.write("randList unsorted is:\n")
        my_file.write(banner)
        for item in rand_list1:
            my_file.write(f"{item}\n")
    print("Beginning quicksort...\n")
    start_time = time.process_time()
    random_index = random.randrange(0, len(rand_list1) - 1)
    rand_list2[random_index], rand_list2[-1] = rand_list2[-1], rand_list2[random_index]
    quicksort(rand_list2, 0, len(rand_list2) - 1)
    end_time = time.process_time()
    print(f"Total elapsed quicksort time is: {end_time - start_time:.3f}s\n")
    with open("generatedLists.txt", "a") as my_file:
        my_file.write(banner)
        my_file.write("randList after quicksort sorting is:\n")
        my_file.write(banner)
        for item in rand_list2:
            my_file.write(f"{item}\n")
    start_time = time.process_time()
    rand_list3.sort()
    end_time = time.process_time()
    print(f"Total elapsed built-in Python sorter time is: {end_time - start_time:.3f}s\n")
    start_time = time.process_time()
    rand_list4 = np.sort(rand_list4)
    end_time = time.process_time()
    print(f"Total elapsed time for NumPy sorter is: {end_time - start_time:.3f}s\n")
if __name__ == "__main__":
    main()