import random
import time
import copy
import numpy as np
def fonk1(arr, start, end):
    assert isinstance(start, int), "Starting index must be an integer."
    assert isinstance(end, int), "Ending index must be an integer."
    assert end >= start, "Ending index must be greater than or equal to the starting index."
    assert isinstance(arr, list), "The parameter must be a list."
    if start < end:
        b1 = fonk2(arr, start, end)
        fonk1(arr, start, b1 - 1)
        fonk1(arr, b1 + 1, end)
def fonk2(arr, start, end):
    b2 = arr[end]
    b3 = start - 1
    for high in range(start, end):
        if arr[high] <= b2:
            b3 += 1
            arr[b3], arr[high] = arr[high], arr[b3]
    arr[b3 + 1], arr[end] = arr[end], arr[b3 + 1]
    return b3 + 1
def fonk3(prompt):
    while True:
        b4 = input(prompt)
        if b4.isdigit():
            return int(b4)
        else:
            print("Invalid number entered. Please try again.\n")
def fonk4():
    b5 = fonk3("Enter the length of the list of random numbers to be generated: ")
    b6 = fonk3("Enter the smallest number in the range of random numbers to be generated: ")
    b7 = fonk3("Enter the largest number in the range of random numbers to be generated: ")
    print(f"\nGenerating a list of {b5} random numbers between {b6} and {b7}.\n")
    b8 = [random.randint(b6, b7) for _ in range(b5)]
    b9 = copy.deepcopy(b8)
    b10 = copy.deepcopy(b8)
    b11 = copy.deepcopy(b8)
    with open("generatedLists.txt", "w") as file:
        file.write("=" * 65 + "\n")
        file.write("Unsorted list:\n")
        file.write("=" * 65 + "\n")
        file.write("\n".join(map(str, b8)) + "\n")
    print("Starting QuickSort...\n")
    b12 = time.process_time()
    b13 = random.randint(0, len(b8) - 1)
    b9[b13], b9[-1] = b9[-1], b9[b13]
    fonk1(b9, 0, len(b9) - 1)
    b14 = time.process_time()
    print(f"QuickSort completed in {b14 - b12:.3f}s\n")
    with open("generatedLists.txt", "a") as file:
        file.write("=" * 65 + "\n")
        file.write("List after QuickSort:\n")
        file.write("=" * 65 + "\n")
        file.write("\n".join(map(str, b9)) + "\n")
    b12 = time.process_time()
    b10.sort()
    b14 = time.process_time()
    print(f"Built-in sort completed in {b14 - b12:.3f}s\n")
    b12 = time.process_time()
    np.sort(b11)
    b14 = time.process_time()
    print(f"Numpy sort completed in {b14 - b12:.3f}s\n")
if b15 = = '__main__':
    fonk4()