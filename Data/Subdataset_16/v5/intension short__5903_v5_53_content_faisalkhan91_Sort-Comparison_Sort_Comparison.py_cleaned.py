import random
import timeit
def fonk1(arr):
    print(' '.join(map(str, arr)))
def fonk2(arr):
    for b6 in range(1, len(arr)):
        b1 = arr[b6]
        b2 = b6 - 1
        while b2 >= 0 and arr[b2] > b1:
            arr[b2 + 1] = arr[b2]
            b2 -= 1
        arr[b2 + 1] = b1
def fonk3(arr):
    if len(arr) > 1:
        b3 = len(arr)
        b4 = arr[:b3]
        b5 = arr[b3:]
        fonk3(b4)
        fonk3(b5)
        b6 = b2 = k = 0
        while b6 < len(b4) and b2 < len(b5):
            if b4[b6] < b5[b2]:
                arr[k] = b4[b6]
                b6 += 1
            else:
                arr[k] = b5[b2]
                b2 += 1
            k += 1
        while b6 < len(b4):
            arr[k] = b4[b6]
            b6 += 1
            k += 1
        while b2 < len(b5):
            arr[k] = b5[b2]
            b2 += 1
            k += 1
def fonk4(arr):
    for b6 in range(len(arr) - 1, 0, -1):
        for b2 in range(b6):
            if arr[b2] > arr[b2 + 1]:
                arr[b2], arr[b2 + 1] = arr[b2 + 1], arr[b2]
def fonk5(sort_func, arr):
    b7 = timeit.default_timer()
    sort_func(arr)
    return timeit.default_timer() - b7
a1 = 10000
b8 = random.sample(range(a1), a1)
b9 = b8.copy()
b10 = b8.copy()
b11 = b8.copy()
print("Initial Array:")
fonk1(b8)
b12 = fonk5(insertion_sort, b9)
b13 = fonk5(merge_sort, b10)
b14 = fonk5(unh_sort, b11)
print(f"Insertion Sort Time: {b12:.6f} seconds")
print(f"Merge Sort Time: {b13:.6f} seconds")
print(f"UNH Sort Time: {b14:.6f} seconds")