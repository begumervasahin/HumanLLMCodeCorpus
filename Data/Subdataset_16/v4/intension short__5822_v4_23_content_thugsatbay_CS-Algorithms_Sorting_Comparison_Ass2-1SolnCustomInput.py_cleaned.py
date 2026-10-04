import random
import time
import sys
def fonk1(arr):
    for b5 in range(len(arr)):
        b1 = arr[b5]
        b2 = b5
        while b2 > 0 and arr[b2 - 1] > b1:
            arr[b2] = arr[b2 - 1]
            b2 -= 1
        arr[b2] = b1
    return arr
def fonk2(arr):
    for b5 in range(len(arr)):
        b1 = arr[b5]
        b2 = b5
        while b2 > 0 and arr[b2 - 1] < b1:
            arr[b2] = arr[b2 - 1]
            b2 -= 1
        arr[b2] = b1
    return arr
def fonk3(arr, low, high):
    if low < high:
        b3 = fonk5(arr, low, high)
        fonk3(arr, low, b3 - 1)
        fonk3(arr, b3 + 1, high)
def fonk4(arr, low, high):
    if low < high:
        b3 = fonk6(arr, low, high)
        fonk4(arr, low, b3 - 1)
        fonk4(arr, b3 + 1, high)
def fonk5(arr, low, high):
    b4 = arr[high]
    b5 = low - 1
    for j in range(low, high):
        if arr[j] <= b4:
            b5 += 1
            arr[b5], arr[j] = arr[j], arr[b5]
    arr[b5 + 1], arr[high] = arr[high], arr[b5 + 1]
    return b5 + 1
def fonk6(arr, low, high):
    b6 = random.randint(low, high)
    arr[b6], arr[high] = arr[high], arr[b6]
    return fonk5(arr, low, high)
def fonk7():
    print("Hi, Question 1 - Assignment 2 Algorithm has started.")
    print("Plotting of graph to compare sorting algorithms will be done.")
    while True:
        print("There are 4 modules listed as [A, B, C, D] for Question 1.")
        print("Only one module can be run at a time. Press 'E' to exit.")
        if sys.version_info[0] < 3:
            b7 = raw_input("Please enter which part of Question 1 you want to run (Example: A): ").lower().strip()
            b8 = int(raw_input("Enter size of array N: ").strip())
        else:
            b7 = input("Please enter which part of Question 1 you want to run (Example: A): ").lower().strip()
            b8 = int(input("Enter size of array N: ").strip())
        if b7 = = 'e':
            break
        b9 = random.sample(range(b8), b8)
        if b7 = = 'a':
            fonk8(b8, b9, insertion_sort, quicksort_standard_pivot)
        elif b7 = = 'b':
            fonk8(b8, b9, quicksort_standard_pivot, quicksort_random_pivot)
        elif b7 = = 'c':
            b9 = list(range(b8))
            fonk8(b8, b9, insertion_sort, quicksort_standard_pivot)
        elif b7 = = 'd':
            b9 = list(range(b8))
            b9 = fonk2(b9)
            fonk8(b8, b9, insertion_sort, quicksort_standard_pivot)
        else:
            print("Wrong Input. Please try again or press 'E' to exit.")
        print("\n" * 3)
def fonk8(b8, b9, algo1, algo2):
    algo1_time, b10 = [], []
    for _ in [b8]:
        sample1, b11 = b9[:], b9[:]
        b12 = time.time()
        algo1(sample1)
        algo1_time.append(abs(time.time() - b12))
        b12 = time.time()
        algo2(b11, 0, len(b11) - 1)
        b10.append(abs(time.time() - b12))
    print("\nTest Sample Size:", [b8])
    print(f"{algo1.b13.replace('_', ' ').title()}: {algo1_time}")
    print(f"{algo2.b13.replace('_', ' ').title()}: {b10}")
if b13 = = "__main__":
    fonk7()