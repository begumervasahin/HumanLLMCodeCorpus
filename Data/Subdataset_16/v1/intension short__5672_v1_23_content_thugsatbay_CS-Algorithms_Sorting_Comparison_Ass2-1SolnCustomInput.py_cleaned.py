import random
import time
import sys
def fonk1(b8):
    for b5 in range(1, len(b8)):
        b1 = b8[b5]
        b2 = b5
        while b2 > 0 and b8[b2 - 1] > b1:
            b8[b2] = b8[b2 - 1]
            b2 -= 1
        b8[b2] = b1
    return b8
def fonk2(b8):
    for b5 in range(1, len(b8)):
        b1 = b8[b5]
        b2 = b5
        while b2 > 0 and b8[b2 - 1] < b1:
            b8[b2] = b8[b2 - 1]
            b2 -= 1
        b8[b2] = b1
    return b8
def fonk3(b8, start, end):
    if start < end:
        b3 = fonk5(b8, start, end)
        fonk3(b8, start, b3 - 1)
        fonk3(b8, b3 + 1, end)
def fonk4(b8, start, end):
    if start < end:
        b3 = fonk6(b8, start, end)
        fonk4(b8, start, b3 - 1)
        fonk4(b8, b3 + 1, end)
def fonk5(b8, start, end):
    b4 = b8[end]
    b5 = start - 1
    for j in range(start, end):
        if b8[j] <= b4:
            b5 += 1
            b8[b5], b8[j] = b8[j], b8[b5]
    b8[b5 + 1], b8[end] = b8[end], b8[b5 + 1]
    return b5 + 1
def fonk6(b8, start, end):
    b6 = random.randint(start, end)
    b8[end], b8[b6] = b8[b6], b8[end]
    return fonk5(b8, start, end)
def fonk7(b7, b12):
    if b7 = = 'a':
        b8 = random.sample(range(b12), b12)
        fonk8(b8)
        fonk9(b8)
    elif b7 = = 'b':
        b8 = random.sample(range(b12), b12)
        fonk9(b8)
        fonk10(b8)
    elif b7 = = 'c':
        b8 = list(range(b12))
        fonk8(b8)
        fonk9(b8)
    elif b7 = = 'd':
        b8 = list(range(b12))
        b8 = fonk2(b8)
        fonk8(b8)
        fonk9(b8)
def fonk8(b8):
    b9 = time.time()
    fonk1(b8.copy())
    b10 = time.time() - b9
    print(f"Insertion Sort Time: {b10:.6f} seconds")
def fonk9(b8):
    b9 = time.time()
    fonk3(b8.copy(), 0, len(b8) - 1)
    b10 = time.time() - b9
    print(f"Quicksort with Fixed Pivot Time: {b10:.6f} seconds")
def fonk10(b8):
    b9 = time.time()
    fonk4(b8.copy(), 0, len(b8) - 1)
    b10 = time.time() - b9
    print(f"Quicksort with Random Pivot Time: {b10:.6f} seconds")
def fonk11():
    print("Hi, Question 1 - Assignment 2 Algorithm has started.")
    while True:
        print("Choose one of the following options (A, B, C, D) to run the corresponding module or press E to exit:")
        print("A: Insertion Sort vs Quicksort with Fixed Pivot")
        print("B: Quicksort with Fixed Pivot vs Quicksort with Random Pivot")
        print("C: Insertion Sort vs Quicksort with Fixed Pivot (Ordered Array)")
        print("D: Insertion Sort vs Quicksort with Fixed Pivot (Reversed Array)")
        print("E: Exit")
        b11 = input("Enter your choice (A, B, C, D, or E): ").lower()
        if b11 in ['a', 'b', 'c', 'd']:
            b12 = int(input("Enter size of array N: ").strip())
            fonk7(b11, b12)
        elif b11 = = 'e':
            print("Exiting...")
            break
        else:
            print("Invalid input. Please try again.")
if b13 = = "__main__":
    fonk11()