import random
import time
def fonk1(num1, num2):
    if num1 > num2:
        return (num2 / num1) * 100
    else:
        return (num1 / num2) * 100
def fonk2(arr, b20):
    print(f'Sorted array from {b20} Sort is:')
    for num in arr:
        print(num, b1 = ' ')
    print()
def fonk3(func, arr):
    b2 = time.time()
    func(arr)
    b3 = time.time() - b2
    print(f'Function [{func.b21}] finished in {b3:.3f} sec')
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
    fonk8(arr, 0, len(arr) - 1)
def fonk10(arr):
    for b11 in range(len(arr)):
        b14 = b11
        for b16 in range(b11 + 1, len(arr)):
            if arr[b14] > arr[b16]:
                b14 = b16
        arr[b11], arr[b14] = arr[b14], arr[b11]
def fonk11(arr):
    for b11 in range(1, len(arr)):
        b15 = arr[b11]
        b16 = b11 - 1
        while b16 >= 0 and b15 < arr[b16]:
            arr[b16 + 1] = arr[b16]
            b16 -= 1
        arr[b16 + 1] = b15
def fonk12(arr):
    b7 = len(arr)
    for b11 in range(b7):
        for b16 in range(0, b7 - b11 - 1):
            if arr[b16] > arr[b16 + 1]:
                arr[b16], arr[b16 + 1] = arr[b16 + 1], arr[b16]
def fonk13():
    a1 = 10000
    b17 = {
        'Bubble': [random.randint(1, 500) for _ in range(a1)],
        'Insertion': [random.randint(1, 500) for _ in range(a1)],
        'Selection': [random.randint(1, 500) for _ in range(a1)],
        'Quick': [random.randint(1, 5000) for _ in range(a1)],
        'Merge': [random.randint(1, 5000) for _ in range(a1)],
        'Heap': [random.randint(1, 5000) for _ in range(a1)]
    }
    for b20, arr in b17.items():
        print(f"----- Array Random --- {b20} sort: ---- ")
        print(*arr)
    print("")
    b18 = {}
    for b20, arr in b17.items():
        b19 = arr.copy()
        b2 = time.time()
        if b20 = = 'Bubble':
            fonk12(b19)
        elif b20 = = 'Insertion':
            fonk11(b19)
        elif b20 = = 'Selection':
            fonk10(b19)
        elif b20 = = 'Quick':
            fonk9(b19)
        elif b20 = = 'Merge':
            fonk6(b19)
        elif b20 = = 'Heap':
            fonk5(b19)
        b3 = time.time() - b2
        b18[b20] = b3
        print(f'Function [{b20} Sort] finished in {b3:.3f} sec')
    for b20, arr in b17.items():
        fonk2(arr, b20)
if b21 = = "__main__":
    fonk13()