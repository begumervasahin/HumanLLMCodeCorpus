import random
import time
def fonk1(b7):
    for b5 in range(1, len(b7)):
        b1 = b7[b5]
        b2 = b5
        while b2 > 0 and b7[b2 - 1] > b1:
            b7[b2] = b7[b2 - 1]
            b2 -= 1
        b7[b2] = b1
    return b7
def fonk2(b7):
    for b5 in range(1, len(b7)):
        b1 = b7[b5]
        b2 = b5
        while b2 > 0 and b7[b2 - 1] < b1:
            b7[b2] = b7[b2 - 1]
            b2 -= 1
        b7[b2] = b1
    return b7
def fonk3(b7, start, end):
    if start < end:
        b3 = fonk5(b7, start, end)
        fonk3(b7, start, b3 - 1)
        fonk3(b7, b3 + 1, end)
def fonk4(b7, start, end):
    if start < end:
        b3 = fonk6(b7, start, end)
        fonk4(b7, start, b3 - 1)
        fonk4(b7, b3 + 1, end)
def fonk5(b7, start, end):
    b4 = b7[end]
    b5 = start - 1
    for j in range(start, end):
        if b7[j] <= b4:
            b5 += 1
            b7[b5], b7[j] = b7[j], b7[b5]
    b7[b5 + 1], b7[end] = b7[end], b7[b5 + 1]
    return b5 + 1
def fonk6(b7, start, end):
    b6 = random.randint(start, end)
    b7[end], b7[b6] = b7[b6], b7[end]
    return fonk5(b7, start, end)
def fonk7(b8, b13):
    b7 = fonk8(b8, b13)
    if b8 = = 'a':
        fonk9(b7, [insertion_sort, quicksort_fixed_pivot])
    elif b8 = = 'b':
        fonk9(b7, [quicksort_fixed_pivot, quicksort_random_pivot])
    elif b8 = = 'c':
        fonk9(b7, [insertion_sort, quicksort_fixed_pivot])
    elif b8 = = 'd':
        fonk9(b7, [insertion_sort, quicksort_fixed_pivot])
def fonk8(b8, b13):
    if b8 = = 'a' or b8 == 'b':
        return random.sample(range(b13), b13)
    elif b8 = = 'c':
        return list(range(b13))
    elif b8 = = 'd':
        b7 = list(range(b13))
        return fonk2(b7)
def fonk9(b7, algorithms):
    for sort_func in algorithms:
        b9 = b7.copy()
        b10 = time.time()
        sort_func(b9)
        b11 = time.time() - b10
        print(f"{sort_func.b14.replace('_', ' ').title()} Time: {b11:.6f} seconds")
def fonk10():
    print("Hi, Question 1 - Assignment 2 Algorithm has started.")
    while True:
        print("\nChoose one of the following options to run the corresponding module:")
        print("A: Insertion Sort vs Quicksort with Fixed Pivot")
        print("B: Quicksort with Fixed Pivot vs Quicksort with Random Pivot")
        print("C: Insertion Sort vs Quicksort with Fixed Pivot (Ordered Array)")
        print("D: Insertion Sort vs Quicksort with Fixed Pivot (Reversed Array)")
        print("E: Exit")
        b12 = input("Enter your choice (A, B, C, D, or E): ").lower()
        if b12 in ['a', 'b', 'c', 'd']:
            try:
                b13 = int(input("Enter the size of the array (N): ").strip())
                fonk7(b12, b13)
            except ValueError:
                print("Invalid input. Please enter a valid integer for the array size.")
        elif b12 = = 'e':
            print("Exiting...")
            break
        else:
            print("Invalid input. Please try again.")
if b14 = = "__main__":
    fonk10()