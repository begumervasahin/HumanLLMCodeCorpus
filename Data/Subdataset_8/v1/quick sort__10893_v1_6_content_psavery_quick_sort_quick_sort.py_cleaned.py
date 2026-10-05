import random
import time
import copy
import numpy as np
def quicksort(my_list, start, finish):
    assert type(start) is int, "Starting index must be an integer."
    assert type(finish) is int, "Ending index must be an integer."
    assert finish > start, "Ending index must be greater than starting index."
    assert type(my_list) is list, "List parameter must be a list."
    comparisonIndex = start
    swapIndex = start
    while comparisonIndex != finish:
        if my_list[comparisonIndex] <= my_list[finish]:
            my_list[comparisonIndex], my_list[swapIndex] = \
                my_list[swapIndex], my_list[comparisonIndex]
            swapIndex += 1
        comparisonIndex += 1
    my_list[swapIndex], my_list[finish] = my_list[finish], my_list[swapIndex]
    if start < swapIndex - 1:
        quicksort(my_list, start, swapIndex - 1)
    if swapIndex + 1 < finish:
        quicksort(my_list, swapIndex + 1, finish)
if __name__ == "__main__":
    listLength = 0
    firstNumber = 0
    lastNumber = 0
    errorMessage = "Invalid number entered. Please try again.\n"
    while True:
        listLength = int(input("\nEnter the length of the list of random "
                               "numbers to be generated.\n"))
        if listLength > 0:
            break
        else:
            print(errorMessage)
    while True:
        firstNumber = int(input("\nEnter the smallest number in the range of "
                                "random numbers to be generated.\n"))
        break
    while True:
        lastNumber = int(input("\nEnter the largest number in the range of "
                               "random numbers to be generated.\n"))
        break
    print("\nGenerating a list of random numbers of length ", listLength, ", ")
    print("with numbers between ", firstNumber, " and ", lastNumber, ".\n")
    randList1 = [random.randint(firstNumber, lastNumber) for _ in range(listLength)]
    randList2 = copy.deepcopy(randList1)
    randList3 = copy.deepcopy(randList1)
    randList4 = copy.deepcopy(randList1)
    with open("generatedLists.txt", "w") as my_file:
        banner = "=================================================================\n"
        my_file.write(banner)
        my_file.write("randList unsorted is:\n")
        my_file.write(banner)
        for item in randList1:
            my_file.write("%s\n" % item)
        print("Beginning quicksort...\n")
        startTime = time.process_time()
        quicksort(randList2, 0, len(randList2) - 1)
        endTime = time.process_time()
        print("Total elapsed quicksort time is: %.3fs" % (endTime - startTime), "\n")
        my_file.write(banner)
        my_file.write("randList after quicksort sorting is:\n")
        my_file.write(banner)
        for item in randList2:
            my_file.write("%s\n" % item)
        startTime = time.process_time()
        randList3.sort()
        endTime = time.process_time()
        print("Total elapsed built-in Python sorter is: %.3fs" % (endTime - startTime), "\n")
        startTime = time.process_time()
        np.sort(randList4)
        endTime = time.process_time()
        print("Total elapsed time for np sorter is: %.3fs" % (endTime - startTime), "\n")