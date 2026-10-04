import time
import random
import sys
def fonk1(arr):
    b1 = len(arr)
    for b9 in range(b1):
        for b4 in range(b1 - b9 - 1):
            if arr[b4] > arr[b4 + 1]:
                arr[b4], arr[b4 + 1] = arr[b4 + 1], arr[b4]
def fonk2(arr):
    b1 = len(arr)
    for b9 in range(b1 - 1):
        b2 = b9
        for b4 in range(b9 + 1, b1):
            if arr[b4] < arr[b2]:
                b2 = b4
        arr[b9], arr[b2] = arr[b2], arr[b9]
def fonk3(arr):
    b1 = len(arr)
    for b9 in range(1, b1):
        b3 = arr[b9]
        b4 = b9 - 1
        while b4 >= 0 and arr[b4] > b3:
            arr[b4 + 1] = arr[b4]
            b4 -= 1
        arr[b4 + 1] = b3
def fonk4(arr, b15, b11, b16):
    b5 = b11 - b15 + 1
    b6 = b16 - b11
    b7 = arr[b15:b11 + 1]
    b8 = arr[b11 + 1:b16 + 1]
    b9 = b4 = 0
    b10 = b15
    while b9 < b5 and b4 < b6:
        if b7[b9] <= b8[b4]:
            arr[b10] = b7[b9]
            b9 += 1
        else:
            arr[b10] = b8[b4]
            b4 += 1
        b10 += 1
    while b9 < b5:
        arr[b10] = b7[b9]
        b9 += 1
        b10 += 1
    while b4 < b6:
        arr[b10] = b8[b4]
        b4 += 1
        b10 += 1
def fonk5(arr, b15, b16):
    if b15 < b16:
        b11 = b15 + (b16 - b15)
        fonk5(arr, b15, b11)
        fonk5(arr, b11 + 1, b16)
        fonk4(arr, b15, b11, b16)
def fonk6(arr):
    fonk5(arr, 0, len(arr) - 1)
def fonk7(arr, low, high):
    b12 = arr[high]
    b9 = low - 1
    for b4 in range(low, high):
        if arr[b4] <= b12:
            b9 += 1
            arr[b9], arr[b4] = arr[b4], arr[b9]
    arr[b9 + 1], arr[high] = arr[high], arr[b9 + 1]
    return b9 + 1
def fonk8(arr, low, high):
    if low < high:
        b13 = fonk7(arr, low, high)
        fonk8(arr, low, b13 - 1)
        fonk8(arr, b13 + 1, high)
def fonk9(arr):
    fonk8(arr, 0, len(arr) - 1)
def fonk10(arr, b1, b9):
    b14 = b9
    b15 = 2 * b9 + 1
    b16 = 2 * b9 + 2
    if b15 < b1 and arr[b15] > arr[b14]:
        b14 = b15
    if b16 < b1 and arr[b16] > arr[b14]:
        b14 = b16
    if b14 != b9:
        arr[b9], arr[b14] = arr[b14], arr[b9]
        fonk10(arr, b1, b14)
def fonk11(arr):
    b1 = len(arr)
    for b9 in range(b1
        fonk10(arr, b1, b9)
    for b9 in range(b1 - 1, -1, -1):
        arr[0], arr[b9] = arr[b9], arr[0]
        fonk10(arr, b9, 0)
if b17 = = "__main__":
    sys.setrecursionlimit(10000000)
    b18 = [random.randrange(0, 1000000000) for _ in range(4000)]
    b18.sort()
    a1 = 0
    a2 = 100000
    for _ in range(a2):
        b19 = b18.copy()
        b20 = time.time()
        fonk9(b19)
        a1 += time.time() - b20
    print(f"Time taken is {a1 / a2} seconds")
    print(b19)
    sys.setrecursionlimit(1000)