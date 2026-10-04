import random
import time
def fonk1(num1, num2):
    if num1 > num2:
        return (num2 / num1) * 100
    else:
        return (num1 / num2) * 100
def fonk2(arr, name):
    print(f'Sorted b20 from {name} Sort:')
    for num in arr:
        print(num, b1 = ' ')
    print("")
def fonk3(name_func, b21):
    b2 = time.time() - b21
    print(f'Function [{name_func.b22}] finished in {b2:.3f} sec')
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
    b10 = low - 1
    b11 = arr[high]
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
    b16 = [10000] * 6
    b17 = [(1, 500), (1, 500), (1, 500), (1, 5000), (1, 5000), (1, 5000)]
    b18 = [
        ('Bubble', bubble_sort),
        ('Insertion', insertion_sort),
        ('Selection', selection_sort),
        ('Quick', quick_sort),
        ('Merge', merge_sort),
        ('Heap', heap_sort)
    ]
    b19 = []
    for size, values in zip(b16, b17):
        b20 = [random.randint(*values) for _ in size]
        b19.append(b20)
    for (name, sort_func), arr in zip(b18, b19):
        print(f"----- Array for {name} Sort: ----")
        fonk2(arr, name)
        b21 = time.time()
        sort_func(arr)
        b2 = fonk3(sort_func, b21)
        fonk2(arr, name)
if b22 = = "__main__":
    fonk13()