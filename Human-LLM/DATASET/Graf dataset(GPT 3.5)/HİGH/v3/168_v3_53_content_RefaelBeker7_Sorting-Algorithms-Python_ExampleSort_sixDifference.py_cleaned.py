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
def fonk3(sort_function, array):
    b2 = time.time()
    sort_function(array)
    b3 = time.time() - b2
    print(f'Function [{sort_function.__name__}] finished in {b3:.3f} seconds')
    return b3
def fonk4(arr, b7, b11):
    b4 = b11
    b5 = 2 * b11 + 1
    b6 = 2 * b11 + 2
    if b5 < b7 and arr[b11] < arr[b5]:
        b4 = b5
    if b6 < b7 and arr[b4] < arr[b6]:
        b4 = b6
    if b4 != b11:
        arr[b11], arr[b4] = arr[b4], arr[b11]
        fonk4(arr, b7, b4)
def fonk5(arr):
    b7 = len(arr)
    for b11 in range(b7
        fonk4(arr, b7, b11)
    for b11 in range(b7 - 1, 0, -1):
        arr[b11], arr[0] = arr[0], arr[b11]
        fonk4(arr, b11, 0)
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
    b12 = arr[high]
    b11 = low - 1
    for b16 in range(low, high):
        if arr[b16] <= b12:
            b11 += 1
            arr[b11], arr[b16] = arr[b16], arr[b11]
    arr[b11 + 1], arr[high] = arr[high], arr[b11 + 1]
    return b11 + 1
def fonk8(arr, low, high):
    if low < high:
        b13 = fonk7(arr, low, high)
        fonk8(arr, low, b13 - 1)
        fonk8(arr, b13 + 1, high)
def fonk9(arr):
    b7 = len(arr)
    for b11 in range(b7):
        b14 = b11
        for b16 in range(b11 + 1, b7):
            if arr[b14] > arr[b16]:
                b14 = b16
        arr[b11], arr[b14] = arr[b14], arr[b11]
def fonk10(arr):
    for b11 in range(1, len(arr)):
        b15 = arr[b11]
        b16 = b11 - 1
        while b16 >= 0 and b15 < arr[b16]:
            arr[b16 + 1] = arr[b16]
            b16 -= 1
        arr[b16 + 1] = b15
def fonk11(arr):
    b7 = len(arr)
    for b11 in range(b7):
        for b16 in range(0, b7 - b11 - 1):
            if arr[b16] > arr[b16 + 1]:
                arr[b16], arr[b16 + 1] = arr[b16 + 1], arr[b16]
b17 = {
    'Bubble': [random.randint(1, 500) for _ in range(10000)],
    'Insertion': [random.randint(1, 500) for _ in range(10000)],
    'Selection': [random.randint(1, 500) for _ in range(10000)],
    'Quick': [random.randint(1, 5000) for _ in range(10000)],
    'Merge': [random.randint(1, 5000) for _ in range(10000)],
    'Heap': [random.randint(1, 5000) for _ in range(10000)]
}
b18 = {}
for name, array in b17.items():
    b19 = globals()[f'{name.lower()}_sort']
    b18[name] = fonk3(b19, array)
for name, array in b17.items():
    fonk2(array, name)
for name, time_taken in b18.items():
    print(f"{name} Sort Time: {time_taken} seconds")