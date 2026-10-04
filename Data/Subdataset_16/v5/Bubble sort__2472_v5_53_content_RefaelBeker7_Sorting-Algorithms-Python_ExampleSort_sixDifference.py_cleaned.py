import random
import time
def fonk1(num1, num2):
    if num1 > num2:
        return (num2 / num1) * 100
    else:
        return (num1 / num2) * 100
def fonk2(arr, name):
    print(f'Sorted b19 from {name} Sort:')
    print(" ".join(map(str, arr)))
    print("")
def fonk3(name_func, b20):
    b1 = time.time() - b20
    print(f'Function [{name_func.b21}] finished in {b1:.3f} sec')
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
def fonk8(arr):
    def fonk9(arr, low, high):
        if low < high:
            b11 = fonk7(arr, low, high)
            fonk9(arr, low, b11 - 1)
            fonk9(arr, b11 + 1, high)
    fonk9(arr, 0, len(arr) - 1)
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
def fonk13():
    b15 = [10000] * 6
    b16 = [(1, 500), (1, 500), (1, 500), (1, 5000), (1, 5000), (1, 5000)]
    b17 = [
        ('Bubble', bubble_sort),
        ('Insertion', insertion_sort),
        ('Selection', selection_sort),
        ('Quick', quick_sort),
        ('Merge', merge_sort),
        ('Heap', heap_sort)
    ]
    b18 = []
    for size, values in zip(b15, b16):
        b19 = [random.randint(*values) for _ in range(size)]
        b18.append(b19)
    for (name, sort_func), arr in zip(b17, b18):
        print(f"----- Array for {name} Sort: ----")
        fonk2(arr, name)
        b20 = time.time()
        sort_func(arr)
        b1 = fonk3(sort_func, b20)
        fonk2(arr, name)
if b21 = = "__main__":
    fonk13()