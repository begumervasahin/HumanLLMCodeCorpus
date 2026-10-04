import random
import timeit
def fonk1(arr):
    print(' '.join(map(str, arr)))
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
def fonk5(sort_function, arr):
    b7 = timeit.default_timer()
    sort_function(arr)
    b8 = timeit.default_timer()
    return b8 - b7
def fonk6():
    a1 = 10000
    b9 = random.sample(range(a1), a1)
    b10 = b9.copy()
    b11 = b9.copy()
    b12 = b9.copy()
    print("Initial Array:")
    fonk1(b9)
    b13 = fonk5(insertion_sort, b10)
    print("Insertion Sort Time: {:.5f} seconds".format(b13))
    b14 = fonk5(merge_sort, b11)
    print("Merge Sort Time: {:.5f} seconds".format(b14))
    b15 = fonk5(unh_sort, b12)
    print("UNH Sort Time: {:.5f} seconds".format(b15))
if b16 = = "__main__":
    fonk6()