import random
import time
def fonk1(num1, num2):
    return ((num2 / num1) * 100) if num1 > num2 else ((num1 / num2) * 100)
def fonk2(arr, sort_name):
    print(f'Sorted array from {sort_name} Sort:')
    print(' '.join(map(str, arr)))
def fonk3(sort_func, arr):
    b1 = time.time()
    sort_func(arr)
    b2 = time.time() - b1
    print(f'Function [{sort_func.__name__}] finished in {b2:.3f} sec')
    return b2
def fonk4(arr):
    b3 = len(arr)
    for b13 in range(b3):
        for b5 in range(0, b3 - b13 - 1):
            if arr[b5] > arr[b5 + 1]:
                arr[b5], arr[b5 + 1] = arr[b5 + 1], arr[b5]
def fonk5(arr):
    for b13 in range(1, len(arr)):
        b4 = arr[b13]
        b5 = b13 - 1
        while b5 >= 0 and b4 < arr[b5]:
            arr[b5 + 1] = arr[b5]
            b5 -= 1
        arr[b5 + 1] = b4
def fonk6(arr):
    for b13 in range(len(arr)):
        b6 = b13
        for b5 in range(b13 + 1, len(arr)):
            if arr[b6] > arr[b5]:
                b6 = b5
        arr[b13], arr[b6] = arr[b6], arr[b13]
def fonk7(arr):
    if len(arr) <= 1:
        return arr
    b7 = arr[len(arr)
    b8 = [x for x in arr if x < b7]
    b9 = [x for x in arr if x == b7]
    b10 = [x for x in arr if x > b7]
    return fonk7(b8) + b9 + fonk7(b10)
def fonk8(arr):
    if len(arr) <= 1:
        return arr
    b11 = len(arr)
    b8 = fonk8(arr[:b11])
    b10 = fonk8(arr[b11:])
    return fonk9(b8, b10)
def fonk9(b8, b10):
    b12 = []
    b13 = b5 = 0
    while b13 < len(b8) and b5 < len(b10):
        if b8[b13] < b10[b5]:
            b12.append(b8[b13])
            b13 += 1
        else:
            b12.append(b10[b5])
            b5 += 1
    b12.extend(b8[b13:])
    b12.extend(b10[b5:])
    return b12
def fonk10(arr, b3, b13):
    b14 = b13
    b15 = 2 * b13 + 1
    b16 = 2 * b13 + 2
    if b15 < b3 and arr[b13] < arr[b15]:
        b14 = b15
    if b16 < b3 and arr[b14] < arr[b16]:
        b14 = b16
    if b14 != b13:
        arr[b13], arr[b14] = arr[b14], arr[b13]
        fonk10(arr, b3, b14)
def fonk11(arr):
    b3 = len(arr)
    for b13 in range(b3, -1, -1):
        fonk10(arr, b3, b13)
    for b13 in range(b3 - 1, 0, -1):
        arr[b13], arr[0] = arr[0], arr[b13]
        fonk10(arr, b13, 0)
b17 = {
    'Bubble': [random.randint(1, 500) for _ in range(10000)],
    'Insertion': [random.randint(1, 500) for _ in range(10000)],
    'Selection': [random.randint(1, 500) for _ in range(10000)],
    'Quick': [random.randint(1, 5000) for _ in range(10000)],
    'Merge': [random.randint(1, 5000) for _ in range(10000)],
    'Heap': [random.randint(1, 5000) for _ in range(10000)]
}
for b18, array in b17.items():
    fonk2(array, b18)
    if b18 = = 'Bubble':
        b2 = fonk3(bubble_sort, array)
    elif b18 = = 'Insertion':
        b2 = fonk3(insertion_sort, array)
    elif b18 = = 'Selection':
        b2 = fonk3(selection_sort, array)
    elif b18 = = 'Quick':
        b2 = fonk3(quick_sort, array)
    elif b18 = = 'Merge':
        b2 = fonk3(merge_sort, array)
    elif b18 = = 'Heap':
        b2 = fonk3(heap_sort, array)
    print(f'Execution time of {b18} sort: {b2:.3f} seconds')
    print('')
fonk2(b17['Bubble'], 'Bubble')
fonk2(b17['Insertion'], 'Insertion')
fonk2(b17['Selection'], 'Selection')
fonk2(b17['Quick'], 'Quick')
fonk2(b17['Merge'], 'Merge')
fonk2(b17['Heap'], 'Heap')