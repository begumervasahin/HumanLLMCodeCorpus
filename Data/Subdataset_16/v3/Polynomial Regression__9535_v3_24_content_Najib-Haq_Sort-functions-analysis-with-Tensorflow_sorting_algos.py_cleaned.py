import time
import random
import sys
def fonk1(arr):
    b1 = len(arr)
    for b7 in range(b1):
        for b4 in range(b1 - b7 - 1):
            if arr[b4] > arr[b4 + 1]:
                arr[b4], arr[b4 + 1] = arr[b4 + 1], arr[b4]
def fonk2(arr):
    b1 = len(arr)
    for b7 in range(b1 - 1):
        b2 = b7
        for b4 in range(b7 + 1, b1):
            if arr[b4] < arr[b2]:
                b2 = b4
        arr[b7], arr[b2] = arr[b2], arr[b7]
def fonk3(arr):
    b1 = len(arr)
    for b7 in range(1, b1):
        b3 = arr[b7]
        b4 = b7 - 1
        while b4 >= 0 and arr[b4] > b3:
            arr[b4 + 1] = arr[b4]
            b4 -= 1
        arr[b4 + 1] = b3
def fonk4(arr, b13, b9, b14):
    b5 = arr[b13:b9 + 1]
    b6 = arr[b9 + 1:b14 + 1]
    b7 = b4 = 0
    b8 = b13
    while b7 < len(b5) and b4 < len(b6):
        if b5[b7] <= b6[b4]:
            arr[b8] = b5[b7]
            b7 += 1
        else:
            arr[b8] = b6[b4]
            b4 += 1
        b8 += 1
    while b7 < len(b5):
        arr[b8] = b5[b7]
        b7 += 1
        b8 += 1
    while b4 < len(b6):
        arr[b8] = b6[b4]
        b4 += 1
        b8 += 1
def fonk5(arr, b13, b14):
    if b13 < b14:
        b9 = b13 + (b14 - b13)
        fonk5(arr, b13, b9)
        fonk5(arr, b9 + 1, b14)
        fonk4(arr, b13, b9, b14)
def fonk6(arr):
    fonk5(arr, 0, len(arr) - 1)
def fonk7(arr, low, high):
    b10 = arr[high]
    b7 = low - 1
    for b4 in range(low, high):
        if arr[b4] <= b10:
            b7 += 1
            arr[b7], arr[b4] = arr[b4], arr[b7]
    arr[b7 + 1], arr[high] = arr[high], arr[b7 + 1]
    return b7 + 1
def fonk8(arr, low, high):
    if low < high:
        b11 = fonk7(arr, low, high)
        fonk8(arr, low, b11 - 1)
        fonk8(arr, b11 + 1, high)
def fonk9(arr):
    fonk8(arr, 0, len(arr) - 1)
def fonk10(arr, b1, b7):
    b12 = b7
    b13 = 2 * b7 + 1
    b14 = 2 * b7 + 2
    if b13 < b1 and arr[b13] > arr[b12]:
        b12 = b13
    if b14 < b1 and arr[b14] > arr[b12]:
        b12 = b14
    if b12 != b7:
        arr[b7], arr[b12] = arr[b12], arr[b7]
        fonk10(arr, b1, b12)
def fonk11(arr):
    b1 = len(arr)
    for b7 in range(b1
        fonk10(arr, b1, b7)
    for b7 in range(b1 - 1, -1, -1):
        arr[0], arr[b7] = arr[b7], arr[0]
        fonk10(arr, b7, 0)
if b15 = = "__main__":
    sys.setrecursionlimit(10000000)
    a1 = 4000
    b16 = [random.randrange(0, 1000000000) for _ in range(a1)]
    b16.sort()
    a2 = 0
    a3 = 100000
    for _ in range(a3):
        b17 = b16.copy()
        b18 = time.time()
        fonk9(b17)
        a2 += time.time() - b18
    b19 = a2 / a3
    print(f"Time taken is {b19:.6f} seconds")
    print(b17)
    sys.setrecursionlimit(1000)