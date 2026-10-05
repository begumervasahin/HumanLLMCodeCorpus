import random
import time
import copy
import numpy as np
def fonk1(my_list, start, finish):
    assert isinstance(start, int), "Starting index must be an integer."
    assert isinstance(finish, int), "Ending index must be an integer."
    assert finish > start, "Ending index must be greater than starting index."
    assert isinstance(my_list, list), "List parameter must be a list."
    b1 = start
    b2 = start
    while b1 != finish:
        if my_list[b1] <= my_list[finish]:
            my_list[b1], my_list[b2] = my_list[b2], my_list[b1]
            b2 += 1
        b1 += 1
    my_list[b2], my_list[finish] = my_list[finish], my_list[b2]
    if start < b2 - 1:
        fonk1(my_list, start, b2 - 1)
    if b2 + 1 < finish:
        fonk1(my_list, b2 + 1, finish)
if b3 = = "__main__":
    while True:
        try:
            b4 = int(input("\nEnter the length of the list of random numbers to be generated:\n"))
            b5 = int(input("\nEnter the smallest number in the range of random numbers to be generated:\n"))
            b6 = int(input("\nEnter the largest number in the range of random numbers to be generated:\n"))
            break
        except ValueError:
            print("Invalid number entered. Please try again.\n")
    b7 = [random.randrange(b5, b6) for _ in range(b4)]
    b8 = copy.deepcopy(b7)
    b9 = copy.deepcopy(b7)
    b10 = copy.deepcopy(b7)
    with open("generatedLists.txt", "w") as my_file:
        my_file.write("=================================================================\n")
        my_file.write("randList unsorted is:\n")
        my_file.write("=================================================================\n")
        for item in b7:
            my_file.write(f"{item}\n")
    print("Beginning quicksort...\n")
    b11 = time.process_time()
    b12 = random.randrange(0, len(b7) - 1)
    b8[b12], b8[-1] = b8[-1], b8[b12]
    fonk1(b8, 0, len(b8) - 1)
    b13 = time.process_time()
    print(f"Total elapsed quicksort time is: {b13 - b11:.3f}s\n")
    with open("generatedLists.txt", "a") as my_file:
        my_file.write("=================================================================\n")
        my_file.write("randList after quicksort sorting is:\n")
        my_file.write("=================================================================\n")
        for item in b8:
            my_file.write(f"{item}\n")
    b11 = time.process_time()
    b9.sort()
    b13 = time.process_time()
    print(f"Total elapsed built-in Python sorter is: {b13 - b11:.3f}s\n")
    b11 = time.process_time()
    b10 = np.sort(b10)
    b13 = time.process_time()
    print(f"Total elapsed time for np sorter is: {b13 - b11:.3f}s\n")