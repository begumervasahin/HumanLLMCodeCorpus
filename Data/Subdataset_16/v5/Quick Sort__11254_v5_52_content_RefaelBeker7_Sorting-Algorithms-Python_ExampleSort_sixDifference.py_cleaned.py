import random
import time
'''Utility Functions'''
def fonk1(num1, num2):
    return (num2 / num1 * 100) if num1 > num2 else (num1 / num2 * 100)
def fonk2(arr, name):
    print(f"Sorted array from {name} Sort is:")
    print(' '.join(map(str, arr)))
def fonk3(name_func, b22):
    b1 = time.time() - b22
    print(f'Function [{name_func.b16}] finished in {b1:.3f} sec')
    return b1
def fonk4(size, b2 = 1, upper=5000):
    return [random.randint(b2, upper) for _ in range(size)]
'''Sorting Algorithms'''
def fonk5(arr, b6, b10):
    b3 = b10
    b4 = 2 * b10 + 1
    b5 = 2 * b10 + 2
    if b4 < b6 and arr[b10] < arr[b4]:
        b3 = b4
    if b5 < b6 and arr[b3] < arr[b5]:
        b3 = b5
    if b3 != b10:
        arr[b10], arr[b3] = arr[b3], arr[b10]
        fonk5(arr, b6, b3)
def fonk6(arr):
    b6 = len(arr)
    for b10 in range(b6
        fonk5(arr, b6, b10)
    for b10 in range(b6 - 1, 0, -1):
        arr[b10], arr[0] = arr[0], arr[b10]
        fonk5(arr, b10, 0)
def fonk7(arr):
    if len(arr) > 1:
        b7 = len(arr)
        b8 = arr[:b7]
        b9 = arr[b7:]
        fonk7(b8)
        fonk7(b9)
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
def fonk8(arr, low, high):
    b11 = arr[high]
    b10 = low - 1
    for b15 in range(low, high):
        if arr[b15] <= b11:
            b10 += 1
            arr[b10], arr[b15] = arr[b15], arr[b10]
    arr[b10 + 1], arr[high] = arr[high], arr[b10 + 1]
    return b10 + 1
def fonk9(arr, low, high):
    if low < high:
        b12 = fonk8(arr, low, high)
        fonk9(arr, low, b12 - 1)
        fonk9(arr, b12 + 1, high)
def fonk10(arr):
    fonk9(arr, 0, len(arr) - 1)
def fonk11(arr):
    b6 = len(arr)
    for b10 in range(b6):
        b13 = b10
        for b15 in range(b10 + 1, b6):
            if arr[b13] > arr[b15]:
                b13 = b15
        arr[b10], arr[b13] = arr[b13], arr[b10]
def fonk12(arr):
    for b10 in range(1, len(arr)):
        b14 = arr[b10]
        b15 = b10 - 1
        while b15 >= 0 and b14 < arr[b15]:
            arr[b15 + 1] = arr[b15]
            b15 -= 1
        arr[b15 + 1] = b14
def fonk13(arr):
    b6 = len(arr)
    for b10 in range(b6):
        for b15 in range(0, b6 - b10 - 1):
            if arr[b15] > arr[b15 + 1]:
                arr[b15], arr[b15 + 1] = arr[b15 + 1], arr[b15]
if b16 = = "__main__":
    b17 = [10000] * 6
    b18 = [fonk4(size) for size in b17]
    b19 = ['Bubble', 'Insertion', 'Selection', 'Quick', 'Merge', 'Heap']
    print("Generated Arrays:")
    for name, arr in zip(b19, b18):
        print(f"Array for {name} Sort:")
        print(' '.join(map(str, arr)))
        print("")
    b20 = {
        'Bubble': bubble_sort,
        'Insertion': insertion_sort,
        'Selection': selection_sort,
        'Quick': quick_sort,
        'Merge': merge_sort,
        'Heap': heap_sort
    }
    b21 = {}
    for name, arr in zip(b19, b18):
        b22 = time.time()
        b20[name](arr)
        b1 = fonk3(b20[name], b22)
        b21[name] = b1
        print("")
    for name, arr in zip(b19, b18):
        fonk2(arr, name)
    print("Elapsed Times:")
    for name, b1 in b21.items():
        print(f"{name} Sort took {b1:.3f} seconds")