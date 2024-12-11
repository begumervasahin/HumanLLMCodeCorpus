import random
import timeit
def fonk1(arr):
    print(' '.join(map(str, arr)))
def fonk2(arr):
    b1 = len(arr)
    for b7 in range(1, b1):
        b2 = arr[b7]
        b3 = b7
        while b3 > 0 and arr[b3 - 1] > b2:
            arr[b3] = arr[b3 - 1]
            b3 -= 1
        arr[b3] = b2
def fonk3(arr):
    if len(arr) <= 1:
        return
    b4 = len(arr)
    b5 = arr[:b4]
    b6 = arr[b4:]
    fonk3(b5)
    fonk3(b6)
    fonk4(b5, b6, arr)
def fonk4(left, right, arr):
    b7 = j = k = 0
    while b7 < len(left) and j < len(right):
        if left[b7] < right[j]:
            arr[k] = left[b7]
            b7 += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while b7 < len(left):
        arr[k] = left[b7]
        b7 += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
def fonk5(arr):
    b1 = len(arr)
    for b7 in range(b1):
        for j in range(0, b1-b7-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
b8 = random.sample(range(10000), 10000)
b9 = b8[:]
b10 = b8[:]
b11 = b8[:]
print("Initial Array:")
fonk1(b8)
b12 = timeit.timeit(lambda: fonk2(b9), number=1)
b13 = timeit.timeit(lambda: fonk3(b10), number=1)
b14 = timeit.timeit(lambda: fonk5(b11), number=1)
print("Insertion Sort Time:", b12)
print("Merge Sort Time:", b13)
print("Bubble Sort Time:", b14)