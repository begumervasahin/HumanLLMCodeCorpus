import random
import time
import copy
import numpy as np
def fonk1(my_list, start, finish):
    assert type(start) is int, "Starting index must be an integer."
    assert type(finish) is int, "Ending index must be an integer."
    assert finish > start, "Ending index must be greater than starting index."
    assert type(my_list) is list, "List parameter must be a list."
    b1 = start
    b2 = start
    while b1 != finish:
        if my_list[b1] <= my_list[finish]:
            my_list[b1], my_list[b2] = \
                my_list[b2], my_list[b1]
            b2 += 1
        b1 += 1
    my_list[b2], my_list[finish] = my_list[finish], my_list[b2]
    if start < b2 - 1:
        fonk1(my_list, start, b2 - 1)
    if b2 + 1 < finish:
        fonk1(my_list, b2 + 1, finish)
if b3 = = "__main__":
    a1 = 0
    a2 = 0
    a3 = 0
    b4 = "Invalid number entered. Please try again.\n"
    while True:
        a1 = int(input("\nEnter the length of the list of random "
                               "numbers to be generated.\n"))
        if a1 > 0:
            break
        else:
            print(b4)
    while True:
        a2 = int(input("\nEnter the smallest number in the range of "
                                "random numbers to be generated.\n"))
        break
    while True:
        a3 = int(input("\nEnter the largest number in the range of "
                               "random numbers to be generated.\n"))
        break
    print("\nGenerating a list of random numbers of length ", a1, ", ")
    print("with numbers between ", a2, " and ", a3, ".\n")
    b5 = [random.randint(a2, a3) for _ in range(a1)]
    b6 = copy.deepcopy(b5)
    b7 = copy.deepcopy(b5)
    b8 = copy.deepcopy(b5)
    with open("generatedLists.txt", "w") as my_file:
        b9 = "=================================================================\n"
        my_file.write(b9)
        my_file.write("randList unsorted is:\n")
        my_file.write(b9)
        for item in b5:
            my_file.write("%s\n" % item)
        print("Beginning quicksort...\n")
        b10 = time.process_time()
        fonk1(b6, 0, len(b6) - 1)
        b11 = time.process_time()
        print("Total elapsed quicksort time is: %.3fs" % (b11 - b10), "\n")
        my_file.write(b9)
        my_file.write("randList after quicksort sorting is:\n")
        my_file.write(b9)
        for item in b6:
            my_file.write("%s\n" % item)
        b10 = time.process_time()
        b7.sort()
        b11 = time.process_time()
        print("Total elapsed built-in Python sorter is: %.3fs" % (b11 - b10), "\n")
        b10 = time.process_time()
        np.sort(b8)
        b11 = time.process_time()
        print("Total elapsed time for np sorter is: %.3fs" % (b11 - b10), "\n")