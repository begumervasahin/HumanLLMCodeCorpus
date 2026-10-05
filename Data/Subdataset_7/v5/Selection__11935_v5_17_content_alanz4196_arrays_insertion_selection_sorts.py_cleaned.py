import time
import random
def fonk1(arr):
    for k in range(len(arr) - 1):
        b1 = k
        for n in range(k + 1, len(arr)):
            if arr[n] < arr[b1]:
                b1 = n
        arr[k], arr[b1] = arr[b1], arr[k]
    return arr
def fonk2(arr):
    for k in range(1, len(arr)):
        b2 = arr[k]
        b3 = k
        while b3 > 0 and arr[b3 - 1] > b2:
            arr[b3] = arr[b3 - 1]
            b3 -= 1
        arr[b3] = b2
    return arr
def fonk3(b9, b4 = 0, max_val=100):
    return [random.randint(b4, max_val) for _ in range(b9)]
def fonk4(sort_function, arr):
    b5 = time.process_time()
    sort_function(arr)
    b6 = time.process_time()
    return b6 - b5
def fonk5(b19, b9):
    b7 = [
        "Increasing Selection",
        "Decreasing Selection",
        "Random Selection",
        "Increasing Insertion",
        "Decreasing Insertion",
        "Random Insertion"
    ]
    for i, scenario in enumerate(b7):
        print(f"{b9}-Val {scenario}: {b19[i]:.20f}")
if b8 = = '__main__':
    b9 = int(input('How many values should be generated? '))
    b10 = list(range(1, b9 + 1))
    b11 = list(range(b9, 0, -1))
    b12 = fonk3(b9)
    b13 = b10.copy()
    b14 = b11.copy()
    b15 = b12.copy()
    b16 = [selection_sort, selection_sort, selection_sort, insertion_sort, insertion_sort, insertion_sort]
    b17 = [b10, b11, b12, b13, b14, b15]
    b18 = [[fonk4(sort_function, arr) for _ in range(5)] for sort_function, arr in zip(b16, b17)]
    b19 = [sum(times) / 5 for times in b18]
    fonk5(b19, b9)