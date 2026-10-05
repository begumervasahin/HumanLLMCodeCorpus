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
    a1 = 0
    a2 = 0
    a3 = 0
    b4 = "Invalid number entered. Please try again.\n"
    while True:
        a1 = input("\nEnter the length of the list of random numbers to be generated:\n")
        if a1.isdigit():
            a1 = int(a1)
            break
        else:
            print(b4)
    while True:
        a2 = input("\nEnter the smallest number in the range of random numbers to be generated:\n")
        if a2.isdigit():
            a2 = int(a2)
            break
        else:
            print(b4)
    while True:
        a3 = input("\nEnter the largest number in the range of random numbers to be generated:\n")
        if a3.isdigit():
            a3 = int(a3)
            break
        else:
            print(b4)
    print("\nGenerating a list of random numbers of length {}, with numbers between {} and {}.\n".format(
        a1, a2, a3))
    b5 = [random.randrange(a2, a3) for _ in range(a1)]
    b6 = copy.deepcopy(b5)
    b7 = copy.deepcopy(b5)
    b8 = copy.deepcopy(b5)
    with open("generatedLists.txt", "w") as my_file:
        b9 = "=================================================================\n"
        my_file.write(b9)
        my_file.write("randList unsorted is:\n")
        my_file.write(b9)
        for item in b5:
            my_file.write("{}\n".format(item))
    print("Beginning quicksort...\n")
    b10 = time.clock()
    b11 = random.randrange(0, len(b5) - 1)
    b6[b11], b6[-1] = b6[-1], b6[b11]
    fonk1(b6, 0, len(b6) - 1)
    b12 = time.clock()
    print("Total elapsed quicksort time is: {:.3f}s\n".format(b12 - b10))
    with open("generatedLists.txt", "a") as my_file:
        my_file.write(b9)
        my_file.write("randList after quicksort sorting is:\n")
        my_file.write(b9)
        for item in b6:
            my_file.write("{}\n".format(item))
    b10 = time.clock()
    b7.sort()
    b12 = time.clock()
    print("Total elapsed built-in Python sorter is: {:.3f}s\n".format(b12 - b10))
    b10 = time.clock()
    b8 = np.sort(b8)
    b12 = time.clock()
    print("Total elapsed time for np sorter is: {:.3f}s\n".format(b12 - b10))