import random
import time
import copy
import numpy as np
def quicksort(my_list, start, finish):
    assert isinstance(start, int), "Starting index must be an integer."
    assert isinstance(finish, int), "Ending index must be an integer."
    assert finish > start, "Ending index must be greater than starting index."
    assert isinstance(my_list, list), "List parameter must be a list."
    comparison_index = start
    swap_index = start
    while comparison_index != finish:
        if my_list[comparison_index] <= my_list[finish]:
            my_list[comparison_index], my_list[swap_index] = my_list[swap_index], my_list[comparison_index]
            swap_index += 1
        comparison_index += 1
    my_list[swap_index], my_list[finish] = my_list[finish], my_list[swap_index]
    if start < swap_index - 1:
        quicksort(my_list, start, swap_index - 1)
    if swap_index + 1 < finish:
        quicksort(my_list, swap_index + 1, finish)
if __name__ == "__main__":
    list_length = 0
    first_number = 0
    last_number = 0
    error_message = "Invalid number entered. Please try again.\n"
    while True:
        list_length = input("\nEnter the length of the list of random numbers to be generated:\n")
        if list_length.isdigit():
            list_length = int(list_length)
            break
        else:
            print(error_message)
    while True:
        first_number = input("\nEnter the smallest number in the range of random numbers to be generated:\n")
        if first_number.isdigit():
            first_number = int(first_number)
            break
        else:
            print(error_message)
    while True:
        last_number = input("\nEnter the largest number in the range of random numbers to be generated:\n")
        if last_number.isdigit():
            last_number = int(last_number)
            break
        else:
            print(error_message)
    print("\nGenerating a list of random numbers of length {}, with numbers between {} and {}.\n".format(
        list_length, first_number, last_number))
    rand_list1 = [random.randrange(first_number, last_number) for _ in range(list_length)]
    rand_list2 = copy.deepcopy(rand_list1)
    rand_list3 = copy.deepcopy(rand_list1)
    rand_list4 = copy.deepcopy(rand_list1)
    with open("generatedLists.txt", "w") as my_file:
        banner = "=================================================================\n"
        my_file.write(banner)
        my_file.write("randList unsorted is:\n")
        my_file.write(banner)
        for item in rand_list1:
            my_file.write("{}\n".format(item))
    print("Beginning quicksort...\n")
    start_time = time.clock()
    random_index = random.randrange(0, len(rand_list1) - 1)
    rand_list2[random_index], rand_list2[-1] = rand_list2[-1], rand_list2[random_index]
    quicksort(rand_list2, 0, len(rand_list2) - 1)
    end_time = time.clock()
    print("Total elapsed quicksort time is: {:.3f}s\n".format(end_time - start_time))
    with open("generatedLists.txt", "a") as my_file:
        my_file.write(banner)
        my_file.write("randList after quicksort sorting is:\n")
        my_file.write(banner)
        for item in rand_list2:
            my_file.write("{}\n".format(item))
    start_time = time.clock()
    rand_list3.sort()
    end_time = time.clock()
    print("Total elapsed built-in Python sorter is: {:.3f}s\n".format(end_time - start_time))
    start_time = time.clock()
    rand_list4 = np.sort(rand_list4)
    end_time = time.clock()
    print("Total elapsed time for np sorter is: {:.3f}s\n".format(end_time - start_time))