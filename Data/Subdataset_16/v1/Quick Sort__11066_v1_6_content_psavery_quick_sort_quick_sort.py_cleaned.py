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
def fonk2(prompt):
    while True:
        b3 = input(prompt)
        if b3.isdigit():
            return int(b3)
        else:
            print("Invalid number entered. Please try again.\n")
def fonk3():
    b4 = fonk2("\nEnter the length of the list of random numbers to be generated.\n")
    b5 = fonk2("\nEnter the smallest number in the range of random numbers to be generated.\n")
    b6 = fonk2("\nEnter the largest number in the range of random numbers to be generated.\n")
    print(f"\nGenerating a list of random numbers of length {b4}, with numbers between {b5} and {b6}.\n")
    b7 = [random.randrange(b5, b6) for _ in range(b4)]
    b8 = copy.deepcopy(b7)
    b9 = copy.deepcopy(b7)
    b10 = copy.deepcopy(b7)
    with open("generatedLists.txt", "w") as my_file:
        b11 = "=" * 65 + "\n"
        my_file.write(b11)
        my_file.write("randList unsorted is:\n")
        my_file.write(b11)
        for item in b7:
            my_file.write(f"{item}\n")
    print("Beginning quicksort...\n")
    b12 = time.process_time()
    b13 = random.randrange(0, len(b7) - 1)
    b8[b13], b8[len(b8) - 1] = b8[len(b7) - 1], b8[b13]
    fonk1(b8, 0, len(b8) - 1)
    b14 = time.process_time()
    print(f"Total elapsed quicksort time is: {b14 - b12:.3f}s\n")
    with open("generatedLists.txt", "a") as my_file:
        my_file.write(b11)
        my_file.write("randList after quicksort sorting is:\n")
        my_file.write(b11)
        for item in b8:
            my_file.write(f"{item}\n")
    b12 = time.process_time()
    b9.sort()
    b14 = time.process_time()
    print(f"Total elapsed built-in Python sorter time is: {b14 - b12:.3f}s\n")
    b12 = time.process_time()
    b10 = np.sort(b10)
    b14 = time.process_time()
    print(f"Total elapsed time for numpy sorter is: {b14 - b12:.3f}s\n")
if b15 = = '__main__':
    fonk3()