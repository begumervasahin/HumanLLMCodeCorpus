import random
import time
import sys
def fonk1(arr):
    for b6 in range(len(arr)):
        b1 = arr[b6]
        b2 = b6
        while b2 > 0 and arr[b2 - 1] > b1:
            arr[b2] = arr[b2 - 1]
            b2 -= 1
        arr[b2] = b1
    return arr
def fonk2(arr):
    for b6 in range(len(arr)):
        b1 = arr[b6]
        b2 = b6
        while b2 > 0 and arr[b2 - 1] < b1:
            arr[b2] = arr[b2 - 1]
            b2 -= 1
        arr[b2] = b1
    return arr
def fonk3(arr, low, high, b3 = "standard"):
    if low < high:
        if b3 = = "random":
            b4 = fonk5(arr, low, high)
        else:
            b4 = fonk4(arr, low, high)
        fonk3(arr, low, b4 - 1, b3)
        fonk3(arr, b4 + 1, high, b3)
def fonk4(arr, low, high):
    b5 = arr[high]
    b6 = low - 1
    for j in range(low, high):
        if arr[j] <= b5:
            b6 += 1
            arr[b6], arr[j] = arr[j], arr[b6]
    arr[b6 + 1], arr[high] = arr[high], arr[b6 + 1]
    return b6 + 1
def fonk5(arr, low, high):
    b7 = random.randint(low, high)
    arr[b7], arr[high] = arr[high], arr[b7]
    return fonk4(arr, low, high)
def fonk6():
    print("Hi, Question 1 - Assignment 2 Algorithm has started.")
    print("Plotting of graph to compare sorting algorithms will be done.")
    while True:
        print("There are 4 modules listed as [A, B, C, D] for Question 1.")
        print("Only one module can be run at a time. Press 'E' to exit.")
        b8 = input("Please enter which part of Question 1 you want to run (Example: A): ").lower().strip()
        if b8 = = 'e':
            break
        try:
            b9 = int(input("Enter size of array N: ").strip())
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue
        b10 = random.sample(range(b9), b9)
        if b8 = = 'a':
            fonk7(b9, b10, insertion_sort, quicksort, "standard")
        elif b8 = = 'b':
            fonk7(b9, b10, quicksort, quicksort, "random")
        elif b8 = = 'c':
            b10 = list(range(b9))
            fonk7(b9, b10, insertion_sort, quicksort, "standard")
        elif b8 = = 'd':
            b10 = fonk2(list(range(b9)))
            fonk7(b9, b10, insertion_sort, quicksort, "standard")
        else:
            print("Wrong Input. Please try again or press 'E' to exit.")
        print("\n" * 3)
def fonk7(b9, b10, algo1, algo2, b3 = "standard"):
    sample1, b11 = b10[:], b10[:]
    b12 = fonk8(algo1, sample1)
    b13 = fonk8(algo2, b11, 0, len(b11) - 1, b3=b3)
    print("\nTest Sample Size:", [b9])
    print(f"{algo1.b15.replace('_', ' ').title()}: {b12}")
    print(f"{algo2.b15.replace('_', ' ').title()} ({b3.title()} Pivot): {b13}")
def fonk8(algo, *args, **kwargs):
    b14 = time.time()
    algo(*args, **kwargs)
    return abs(time.time() - b14)
if b15 = = "__main__":
    fonk6()