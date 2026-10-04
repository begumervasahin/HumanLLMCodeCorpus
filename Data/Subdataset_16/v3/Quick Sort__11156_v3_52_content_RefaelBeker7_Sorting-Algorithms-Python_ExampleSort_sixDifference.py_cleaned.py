import random
import time
def fonk1(num1, num2):
    return (min(num1, num2) / max(num1, num2)) * 100
def fonk2(arr, name):
    print(f'Sorted array from {name} Sort is:')
    print(' '.join(map(str, arr)))
def fonk3(func, b22):
    b1 = time.time() - b22
    print(f'Function [{func.b29}] finished in {b1:.3f} seconds')
    return b1
def fonk4(arr, b5, b9):
    b2 = b9
    b3 = 2 * b9 + 1
    b4 = 2 * b9 + 2
    if b3 < b5 and arr[b2] < arr[b3]:
        b2 = b3
    if b4 < b5 and arr[b2] < arr[b4]:
        b2 = b4
    if b2 != b9:
        arr[b9], arr[b2] = arr[b2], arr[b9]
        fonk4(arr, b5, b2)
def fonk5(arr):
    b5 = len(arr)
    for b9 in range(b5
        fonk4(arr, b5, b9)
    for b9 in range(b5 - 1, 0, -1):
        arr[b9], arr[0] = arr[0], arr[b9]
        fonk4(arr, b9, 0)
def fonk6(arr):
    if len(arr) > 1:
        b6 = len(arr)
        b7 = arr[:b6]
        b8 = arr[b6:]
        fonk6(b7)
        fonk6(b8)
        b9 = b14 = k = 0
        while b9 < len(b7) and b14 < len(b8):
            if b7[b9] < b8[b14]:
                arr[k] = b7[b9]
                b9 += 1
            else:
                arr[k] = b8[b14]
                b14 += 1
            k += 1
        while b9 < len(b7):
            arr[k] = b7[b9]
            b9 += 1
            k += 1
        while b14 < len(b8):
            arr[k] = b8[b14]
            b14 += 1
            k += 1
def fonk7(arr, low, high):
    b10 = arr[high]
    b9 = low - 1
    for b14 in range(low, high):
        if arr[b14] <= b10:
            b9 += 1
            arr[b9], arr[b14] = arr[b14], arr[b9]
    arr[b9 + 1], arr[high] = arr[high], arr[b9 + 1]
    return b9 + 1
def fonk8(arr, low, high):
    if low < high:
        b11 = fonk7(arr, low, high)
        fonk8(arr, low, b11 - 1)
        fonk8(arr, b11 + 1, high)
def fonk9(arr):
    fonk8(arr, 0, len(arr) - 1)
def fonk10(arr):
    for b9 in range(len(arr)):
        b12 = b9
        for b14 in range(b9 + 1, len(arr)):
            if arr[b12] > arr[b14]:
                b12 = b14
        arr[b9], arr[b12] = arr[b12], arr[b9]
def fonk11(arr):
    for b9 in range(1, len(arr)):
        b13 = arr[b9]
        b14 = b9 - 1
        while b14 >= 0 and b13 < arr[b14]:
            arr[b14 + 1] = arr[b14]
            b14 -= 1
        arr[b14 + 1] = b13
def fonk12(arr):
    b5 = len(arr)
    for b9 in range(b5):
        for b14 in range(0, b5 - b9 - 1):
            if arr[b14] > arr[b14 + 1]:
                arr[b14], arr[b14 + 1] = arr[b14 + 1], arr[b14]
def fonk13(size, b15 = 1, upper_bound=5000):
    return [random.randint(b15, upper_bound) for _ in range(size)]
def fonk14():
    a1 = 10000
    b16 = fonk13(a1, 1, 500)
    b17 = fonk13(a1, 1, 500)
    b18 = fonk13(a1, 1, 500)
    b19 = fonk13(a1)
    b20 = fonk13(a1)
    b21 = fonk13(a1)
    b22 = time.time()
    fonk12(b16)
    b23 = fonk3(bubble_sort, b22)
    b22 = time.time()
    fonk11(b17)
    b24 = fonk3(insertion_sort, b22)
    b22 = time.time()
    fonk10(b18)
    b25 = fonk3(selection_sort, b22)
    b22 = time.time()
    fonk9(b19)
    b26 = fonk3(quick_sort, b22)
    b22 = time.time()
    fonk6(b20)
    b27 = fonk3(merge_sort, b22)
    b22 = time.time()
    fonk5(b21)
    b28 = fonk3(heap_sort, b22)
    fonk2(b16, 'Bubble')
    fonk2(b17, 'Insertion')
    fonk2(b18, 'Selection')
    fonk2(b19, 'Quick')
    fonk2(b20, 'Merge')
    fonk2(b21, 'Heap')
if b29 = = "__main__":
    fonk14()