import random
import timeit
def fonk1(arr):
    print(' '.join(str(b6) for b6 in arr))
def fonk2(arr):
    for b6 in range(1, len(arr)):
        b1 = arr[b6]
        b2 = b6
        while b2 > 0 and arr[b2 - 1] > b1:
            arr[b2] = arr[b2 - 1]
            b2 -= 1
        arr[b2] = b1
def fonk3(arr):
    if len(arr) > 1:
        b3 = len(arr)
        b4 = arr[:b3]
        b5 = arr[b3:]
        fonk3(b4)
        fonk3(b5)
        b6 = j = k = 0
        while b6 < len(b4) and j < len(b5):
            if b4[b6] < b5[j]:
                arr[k] = b4[b6]
                b6 += 1
            else:
                arr[k] = b5[j]
                j += 1
            k += 1
        while b6 < len(b4):
            arr[k] = b4[b6]
            b6 += 1
            k += 1
        while j < len(b5):
            arr[k] = b5[j]
            j += 1
            k += 1
def fonk4(arr):
    for b6 in range(len(arr) - 1, 0, -1):
        for j in range(1, b6):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
a1 = 10000
b7 = random.sample(range(a1), a1)
b8 = b7.copy()
b9 = b7.copy()
b10 = b7.copy()
print("Initial Array:")
fonk1(b7)
b11 = timeit.default_timer()
fonk2(b8)
b12 = timeit.default_timer()
print("Insertion Sort Time: {:.5f} seconds".format(b12 - b11))
b13 = timeit.default_timer()
fonk3(b9)
b14 = timeit.default_timer()
print("Merge Sort Time: {:.5f} seconds".format(b14 - b13))
b15 = timeit.default_timer()
fonk4(b10)
b16 = timeit.default_timer()
print("UNH Sort Time: {:.5f} seconds".format(b16 - b15))