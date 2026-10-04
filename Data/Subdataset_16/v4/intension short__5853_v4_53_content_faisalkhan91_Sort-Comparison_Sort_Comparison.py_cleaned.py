import random
import timeit
def fonk1(arr):
    print(' '.join(str(b7) for b7 in arr))
def fonk2(arr):
    b1 = len(arr)
    for b7 in range(1, b1):
        b2 = arr[b7]
        b3 = b7 - 1
        while b3 >= 0 and b2 < arr[b3]:
            arr[b3 + 1] = arr[b3]
            b3 -= 1
        arr[b3 + 1] = b2
def fonk3(arr):
    if len(arr) > 1:
        b4 = len(arr)
        b5 = arr[:b4]
        b6 = arr[b4:]
        fonk3(b5)
        fonk3(b6)
        b7 = b3 = k = 0
        while b7 < len(b5) and b3 < len(b6):
            if b5[b7] < b6[b3]:
                arr[k] = b5[b7]
                b7 += 1
            else:
                arr[k] = b6[b3]
                b3 += 1
            k += 1
        while b7 < len(b5):
            arr[k] = b5[b7]
            b7 += 1
            k += 1
        while b3 < len(b6):
            arr[k] = b6[b3]
            b3 += 1
            k += 1
def fonk4(arr):
    b8 = len(arr)
    for b7 in range(b8 - 1, 0, -1):
        for b3 in range(b7):
            if arr[b3] > arr[b3 + 1]:
                arr[b3], arr[b3 + 1] = arr[b3 + 1], arr[b3]
a1 = 10000
b9 = random.sample(range(a1), a1)
b10 = b9.copy()
b11 = b9.copy()
print("Initial Array:")
fonk1(b9)
b12 = timeit.default_timer()
fonk2(b9)
b13 = timeit.default_timer()
b14 = timeit.default_timer()
fonk3(b10)
b15 = timeit.default_timer()
b16 = timeit.default_timer()
fonk4(b11)
b17 = timeit.default_timer()
print("Insertion Sort Time: ", b13 - b12)
print("Merge Sort Time: ", b15 - b14)
print("UNH Sort Time: ", b17 - b16)