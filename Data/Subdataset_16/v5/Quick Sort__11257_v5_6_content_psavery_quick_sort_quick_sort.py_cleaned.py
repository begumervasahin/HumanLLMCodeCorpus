import random
import time
import copy
import numpy as np
def fonk1(arr, start, finish):
    assert isinstance(start, int), "Starting index must be an integer."
    assert isinstance(finish, int), "Ending index must be an integer."
    assert finish > start, "Ending index must be greater than starting index."
    assert isinstance(arr, list), "List parameter must be a list."
    b1 = start
    b2 = start
    while b1 != finish:
        if arr[b1] <= arr[finish]:
            arr[b1], arr[b2] = arr[b2], arr[b1]
            b2 += 1
        b1 += 1
    arr[b2], arr[finish] = arr[finish], arr[b2]
    if start < b2 - 1:
        fonk1(arr, start, b2 - 1)
    if b2 + 1 < finish:
        fonk1(arr, b2 + 1, finish)
def fonk2(prompt, b4):
    while True:
        b3 = input(prompt)
        if b3.isdigit():
            return int(b3)
        else:
            print(b4)
def fonk3():
    b4 = "Invalid number entered. Please try again.\n"
    b5 = fonk2("Enter the length of the list of random numbers to be generated: ", b4)
    b6 = fonk2("Enter the smallest number in the range of random numbers to be generated: ", b4)
    b7 = fonk2("Enter the largest number in the range of random numbers to be generated: ", b4)
    print(f"\nGenerating a list of random numbers of length {b5}, with numbers between {b6} and {b7}.\n")
    b8 = [random.randint(b6, b7) for _ in range(b5)]
    b9 = copy.deepcopy(b8)
    b10 = copy.deepcopy(b8)
    b11 = copy.deepcopy(b8)
    with open("generatedLists.txt", "w") as file:
        b12 = "=" * 65 + "\n"
        file.write(b12)
        file.write("Unsorted list:\n")
        file.write(b12)
        for item in b8:
            file.write(f"{item}\n")
    print("Beginning quicksort...\n")
    b13 = time.process_time()
    b14 = random.randrange(0, len(b8) - 1)
    b9[b14], b9[-1] = b9[-1], b9[b14]
    fonk1(b9, 0, len(b9) - 1)
    b15 = time.process_time()
    print(f"Total elapsed quicksort time: {b15 - b13:.3f} seconds\n")
    with open("generatedLists.txt", "a") as file:
        file.write(b12)
        file.write("List after quicksort:\n")
        file.write(b12)
        for item in b9:
            file.write(f"{item}\n")
    print("Beginning Python built-in sort...\n")
    b13 = time.process_time()
    b10.sort()
    b15 = time.process_time()
    print(f"Total elapsed built-in Python sort time: {b15 - b13:.3f} seconds\n")
    print("Beginning NumPy sort...\n")
    b13 = time.process_time()
    b11 = np.sort(b11)
    b15 = time.process_time()
    print(f"Total elapsed NumPy sort time: {b15 - b13:.3f} seconds\n")
if b16 = = "__main__":
    fonk3()