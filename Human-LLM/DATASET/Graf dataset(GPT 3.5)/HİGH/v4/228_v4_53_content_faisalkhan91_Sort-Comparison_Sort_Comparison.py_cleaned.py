import random
import timeit
def fonk1(arr):
    print(' '.join(str(b7) for b7 in arr))
def fonk2(arr):
    b1 = len(arr)
    for b7 in range(1, b1):
        b2 = b7 - 1
        b3 = arr[b7]
        while b2 >= 0 and b3 < arr[b2]:
            arr[b2 + 1] = arr[b2]
            b2 -= 1
        arr[b2 + 1] = b3
def fonk3(arr):
    if len(arr) <= 1:
        return
    b4 = len(arr)
    b5 = arr[:b4]
    b6 = arr[b4:]
    fonk3(b5)
    fonk3(b6)
    b7 = b2 = k = 0
    while b7 < len(b5) and b2 < len(b6):
        if b5[b7] < b6[b2]:
            arr[k] = b5[b7]
            b7 += 1
        else:
            arr[k] = b6[b2]
            b2 += 1
        k += 1
    while b7 < len(b5):
        arr[k] = b5[b7]
        b7 += 1
        k += 1
    while b2 < len(b6):
        arr[k] = b6[b2]
        b2 += 1
        k += 1
def fonk4(arr):
    b1 = len(arr)
    for b7 in range(b1):
        for b2 in range(0, b1-b7-1):
            if arr[b2] > arr[b2+1]:
                arr[b2], arr[b2+1] = arr[b2+1], arr[b2]
b8 = random.sample(range(10000), 10000)
b9 = b8[:]
b10 = b8[:]
b11 = b8[:]
print("Initial Array:")
fonk1(b8)
b12 = timeit.default_timer()
fonk2(b9)
b13 = timeit.default_timer()
b14 = timeit.default_timer()
fonk3(b10)
b15 = timeit.default_timer()
b16 = timeit.default_timer()
fonk4(b11)
b17 = timeit.default_timer()
print("Insertion Sort Time:", b13 - b12)
print("Merge Sort Time:", b15 - b14)
print("Bubble Sort Time:", b17 - b16)