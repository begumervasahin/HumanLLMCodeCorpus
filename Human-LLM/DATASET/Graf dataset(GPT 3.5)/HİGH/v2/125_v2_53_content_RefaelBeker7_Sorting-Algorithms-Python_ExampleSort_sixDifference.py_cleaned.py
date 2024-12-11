import random
import time
def fonk1(num1, num2):
    if num1 > num2:
        return (num2 / num1) * 100
    else:
        return (num1 / num2) * 100
def fonk2(arr, name):
    print(f'Sorted array from {name} Sort:')
    for element in arr:
        print(element, b1 = ' ')
    print("")
def fonk3(function_name, b22):
    b2 = time.time() - b22
    print(f'Function [{function_name.__name__}] finished in {b2:.3f} seconds')
    return b2
def fonk4(arr, b6, b10):
    b3 = b10
    b4 = 2 * b10 + 1
    b5 = 2 * b10 + 2
    a1 = 0
    if b4 < b6 and arr[b10] < arr[b4]:
        b3 = b4
        a1 += 1
    if b5 < b6 and arr[b3] < arr[b5]:
        b3 = b5
        a1 += 1
    if b3 != b10:
        arr[b10], arr[b3] = arr[b3], arr[b10]
        a1 += 1
        a1 += fonk4(arr, b6, b3)
    return a1
def fonk5(arr):
    b6 = len(arr)
    a1 = 0
    for b10 in range(b6, -1, -1):
        a1 += 1
        a1 += fonk4(arr, b6, b10)
    for b10 in range(b6 - 1, 0, -1):
        a1 += 1
        arr[b10], arr[0] = arr[0], arr[b10]
        a1 += fonk4(arr, b10, 0)
def fonk6(arr):
    if len(arr) > 1:
        b7 = len(arr)
        b8 = arr[:b7]
        b9 = arr[b7:]
        fonk6(b8)
        fonk6(b9)
        b10 = b15 = k = 0
        while b10 < len(b8) and b15 < len(b9):
            if b8[b10] < b9[b15]:
                arr[k] = b8[b10]
                b10 += 1
            else:
                arr[k] = b9[b15]
                b15 += 1
            k += 1
        while b10 < len(b8):
            arr[k] = b8[b10]
            b10 += 1
            k += 1
        while b15 < len(b9):
            arr[k] = b9[b15]
            b15 += 1
            k += 1
def fonk7(arr, low, high):
    b10 = (low - 1)
    b11 = arr[high]
    for b15 in range(low, high):
        if arr[b15] <= b11:
            b10 = b10 + 1
            arr[b10], arr[b15] = arr[b15], arr[b10]
    arr[b10 + 1], arr[high] = arr[high], arr[b10 + 1]
    return (b10 + 1)
def fonk8(arr, low, high):
    if low < high:
        b12 = fonk7(arr, low, high)
        fonk8(arr, low, b12 - 1)
        fonk8(arr, b12 + 1, high)
def fonk9(arr):
    fonk8(arr, 0, len(arr) - 1)
def fonk10(arr):
    a1 = 0
    for b10 in range(len(arr)):
        a1 += 1
        b13 = b10
        for b15 in range(b10 + 1, len(arr)):
            a1 += 1
            if arr[b13] > arr[b15]:
                b13 = b15
        arr[b10], arr[b13] = arr[b13], arr[b10]
def fonk11(arr):
    a1 = 0
    for b10 in range(1, len(arr)):
        b14 = arr[b10]
        b15 = b10 - 1
        while b15 >= 0 and b14 < arr[b15]:
            a1 += 1
            arr[b15 + 1] = arr[b15]
            b15 -= 1
        arr[b15 + 1] = b14
        a1 += 1
def fonk12(arr):
    b6 = len(arr)
    a1 = 0
    for b10 in range(b6):
        for b15 in range(0, b6 - b10 - 1):
            a1 += 1
            if arr[b15] > arr[b15 + 1]:
                arr[b15], arr[b15 + 1] = arr[b15 + 1], arr[b15]
        a1 += 1
b16 = [random.randint(1, 500) for _ in range(10000)]
b17 = [random.randint(1, 500) for _ in range(10000)]
b18 = [random.randint(1, 500) for _ in range(10000)]
b19 = [random.randint(1, 5000) for _ in range(10000)]
b20 = [random.randint(1, 5000) for _ in range(10000)]
b21 = [random.randint(1, 5000) for _ in range(10000)]
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
print(" ")
fonk2(b16, 'Bubble')
fonk2(b17, 'Insertion')
fonk2(b18, 'Selection')
fonk2(b19, 'Quick')
fonk2(b20, 'Merge')
fonk2(b21, 'Heap')
print(f"\nBubble Sort Time: {b23} seconds")
print(f"Insertion Sort Time: {b24} seconds")
print(f"Selection Sort Time: {b25} seconds")
print(f"Quick Sort Time: {b26} seconds")
print(f"Merge Sort Time: {b27} seconds")
print(f"Heap Sort Time: {b28} seconds")