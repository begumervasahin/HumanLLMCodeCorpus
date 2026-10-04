import random
import time
def fonk1(num1, num2):
    return (min(num1, num2) / max(num1, num2)) * 100
def fonk2(arr, b19):
    print(f'Sorted array from {b19} Sort is:')
    print(' '.join(map(str, arr)))
    print()
def fonk3(func, arr):
    b1 = time.time()
    func(arr)
    b2 = time.time() - b1
    print(f'Function [{func.b20}] finished in {b2:.3f} sec')
    return b2
def fonk4(arr, b6, b10):
    b3 = b10
    b4 = 2 * b10 + 1
    b5 = 2 * b10 + 2
    if b4 < b6 and arr[b10] < arr[b4]:
        b3 = b4
    if b5 < b6 and arr[b3] < arr[b5]:
        b3 = b5
    if b3 != b10:
        arr[b10], arr[b3] = arr[b3], arr[b10]
        fonk4(arr, b6, b3)
def fonk5(arr):
    b6 = len(arr)
    for b10 in range(b6
        fonk4(arr, b6, b10)
    for b10 in range(b6 - 1, 0, -1):
        arr[b10], arr[0] = arr[0], arr[b10]
        fonk4(arr, b10, 0)
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
    b11 = arr[high]
    b10 = low - 1
    for b15 in range(low, high):
        if arr[b15] <= b11:
            b10 += 1
            arr[b10], arr[b15] = arr[b15], arr[b10]
    arr[b10 + 1], arr[high] = arr[high], arr[b10 + 1]
    return b10 + 1
def fonk8(arr, low, high):
    if low < high:
        b12 = fonk7(arr, low, high)
        fonk8(arr, low, b12 - 1)
        fonk8(arr, b12 + 1, high)
def fonk9(arr):
    fonk8(arr, 0, len(arr) - 1)
def fonk10(arr):
    for b10 in range(len(arr)):
        b13 = b10
        for b15 in range(b10 + 1, len(arr)):
            if arr[b13] > arr[b15]:
                b13 = b15
        arr[b10], arr[b13] = arr[b13], arr[b10]
def fonk11(arr):
    for b10 in range(1, len(arr)):
        b14 = arr[b10]
        b15 = b10 - 1
        while b15 >= 0 and b14 < arr[b15]:
            arr[b15 + 1] = arr[b15]
            b15 -= 1
        arr[b15 + 1] = b14
def fonk12(arr):
    b6 = len(arr)
    for b10 in range(b6):
        for b15 in range(0, b6 - b10 - 1):
            if arr[b15] > arr[b15 + 1]:
                arr[b15], arr[b15 + 1] = arr[b15 + 1], arr[b15]
def fonk13():
    a1 = 10000
    b16 = {
        'Bubble': [random.randint(1, 500) for _ in range(a1)],
        'Insertion': [random.randint(1, 500) for _ in range(a1)],
        'Selection': [random.randint(1, 500) for _ in range(a1)],
        'Quick': [random.randint(1, 5000) for _ in range(a1)],
        'Merge': [random.randint(1, 5000) for _ in range(a1)],
        'Heap': [random.randint(1, 5000) for _ in range(a1)]
    }
    for b19, arr in b16.items():
        print(f"----- Array Random --- {b19} Sort: ---- ")
        print(' '.join(map(str, arr)))
    print()
    b17 = {}
    for b19, arr in b16.items():
        b18 = arr.copy()
        b1 = time.time()
        if b19 = = 'Bubble':
            fonk12(b18)
        elif b19 = = 'Insertion':
            fonk11(b18)
        elif b19 = = 'Selection':
            fonk10(b18)
        elif b19 = = 'Quick':
            fonk9(b18)
        elif b19 = = 'Merge':
            fonk6(b18)
        elif b19 = = 'Heap':
            fonk5(b18)
        b2 = time.time() - b1
        b17[b19] = b2
        print(f'Function [{b19} Sort] finished in {b2:.3f} sec')
    for b19, arr in b16.items():
        fonk2(arr, b19)
if b20 = = "__main__":
    fonk13()