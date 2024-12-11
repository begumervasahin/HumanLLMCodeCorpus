import random
import time
def fonk1(num1, num2):
    if num1 > num2:
        return ((num2 / num1) * 100)
    else:
        return ((num1 / num2) * 100)
def fonk2(arr, b1):
    if b1 = = 'Bubble':
        print('Sorted array from Bubble Sort:')
    elif b1 = = 'Insertion':
        print('Sorted array from Insertion Sort:')
    elif b1 = = 'Selection':
        print('Sorted array from Selection Sort:')
    elif b1 = = 'Quick':
        print('Sorted array from Quick Sort:')
    elif b1 = = 'Merge':
        print('Sorted array from Merge Sort:')
    elif b1 = = 'Heap':
        print('Sorted array from Heap Sort:')
    for b11 in range(len(arr)):
        print(arr[b11], b2 = ' ')
    print("")
def fonk3(name_func, b23):
    b3 = time.time() - b23
    print('Function [{}] finished in {:.3f} sec'.format(
        name_func.__name__, float(b3)))
    return b3
def fonk4(arr, b7, b11):
    b4 = b11
    b5 = 2 * b11 + 1
    b6 = 2 * b11 + 2
    a1 = 0
    if b5 < b7 and arr[b11] < arr[b5]:
        b4 = b5
        a1 += 1
    if b6 < b7 and arr[b4] < arr[b6]:
        b4 = b6
        a1 += 1
    if b4 != b11:
        arr[b11], arr[b4] = arr[b4], arr[b11]
        a1 += 1
        a1 += fonk4(arr, b7, b4)
    return a1
def fonk5(arr):
    b7 = len(arr)
    a1 = 0
    for b11 in range(b7, -1, -1):
        a1 += 1
        a1 += fonk4(arr, b7, b11)
    for b11 in range(b7 - 1, 0, -1):
        a1 += 1
        arr[b11], arr[0] = arr[0], arr[b11]
        a1 += fonk4(arr, b11, 0)
def fonk6(arr):
    if len(arr) > 1:
        b8 = len(arr)
        b9 = arr[:b8]
        b10 = arr[b8:]
        fonk6(b9)
        fonk6(b10)
        b11 = b16 = k = 0
        while b11 < len(b9) and b16 < len(b10):
            if b9[b11] < b10[b16]:
                arr[k] = b9[b11]
                b11 += 1
            else:
                arr[k] = b10[b16]
                b16 += 1
            k += 1
        while b11 < len(b9):
            arr[k] = b9[b11]
            b11 += 1
            k += 1
        while b16 < len(b10):
            arr[k] = b10[b16]
            b16 += 1
            k += 1
def fonk7(arr, low, high):
    b11 = (low - 1)
    b12 = arr[high]
    for b16 in range(low, high):
        if arr[b16] <= b12:
            b11 = b11 + 1
            arr[b11], arr[b16] = arr[b16], arr[b11]
    arr[b11 + 1], arr[high] = arr[high], arr[b11 + 1]
    return (b11 + 1)
def fonk8(arr, low, high):
    if low < high:
        b13 = fonk7(arr, low, high)
        fonk8(arr, low, b13 - 1)
        fonk8(arr, b13 + 1, high)
def fonk9(arr):
    fonk8(arr, 0, len(arr) - 1)
def fonk10(arr):
    a1 = 0
    for b11 in range(len(arr)):
        a1 += 1
        b14 = b11
        for b16 in range(b11 + 1, len(arr)):
            a1 += 1
            if arr[b14] > arr[b16]:
                b14 = b16
        arr[b11], arr[b14] = arr[b14], arr[b11]
def fonk11(arr):
    a1 = 0
    for b11 in range(1, len(arr)):
        b15 = arr[b11]
        b16 = b11 - 1
        while b16 >= 0 and b15 < arr[b16]:
            a1 += 1
            arr[b16 + 1] = arr[b16]
            b16 -= 1
        arr[b16 + 1] = b15
        a1 += 1
def fonk12(arr):
    b7 = len(arr)
    a1 = 0
    for b11 in range(b7):
        for b16 in range(0, b7 - b11 - 1):
            a1 += 1
            if arr[b16] > arr[b16 + 1]:
                arr[b16], arr[b16 + 1] = arr[b16 + 1], arr[b16]
        a1 += 1
b17 = [random.randint(1, 500) for _ in range(10000)]
b18 = [random.randint(1, 500) for _ in range(10000)]
b19 = [random.randint(1, 500) for _ in range(10000)]
b20 = [random.randint(1, 5000) for _ in range(10000)]
b21 = [random.randint(1, 5000) for _ in range(10000)]
b22 = [random.randint(1, 5000) for _ in range(10000)]
print("----- Array Random 1 --- Bubble sort: ---- ")
fonk2(b17, 'Bubble')
print("---- Array Random 2 ---- Insertion sort: ----")
fonk2(b18, 'Insertion')
print(" ---- Array Random 3 --- Selection Sort: ---- ")
fonk2(b19, 'Selection')
print("----- Array Random 4 --- Quick sort: ---- ")
fonk2(b20, 'Quick')
print("----- Array Random 5 --- Merge sort: ---- ")
fonk2(b21, 'Merge')
print("----- Array Random 6 --- Heap sort: ---- ")
fonk2(b22, 'Heap')
print(" ")
b23 = time.time()
fonk12(b17)
b24 = fonk3(bubble_sort, b23)
print(" ")
b23 = time.time()
fonk11(b18)
b25 = fonk3(insertion_sort, b23)
print(" ")
b23 = time.time()
fonk10(b19)
b26 = fonk3(selection_sort, b23)
print(" ")
b23 = time.time()
fonk9(b20)
b27 = fonk3(quick_sort, b23)
print(" ")
b23 = time.time()
fonk6(b21)
b28 = fonk3(merge_sort, b23)
print(" ")
b23 = time.time()
fonk5(b22)
b29 = fonk3(heap_sort, b23)
print(" ")
print(" ")
fonk2(b17, 'Bubble')
fonk2(b18, 'Insertion')
fonk2(b19, 'Selection')
fonk2(b20, 'Quick')
fonk2(b21, 'Merge')
fonk2(b22, 'Heap')