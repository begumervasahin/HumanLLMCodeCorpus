import random
import time
def fonk1(num1, num2):
    return (abs(num1 - num2) / max(num1, num2)) * 100
def fonk2(arr, name):
    print(f"Sorted array from {name} Sort:")
    print(*arr)
def fonk3(sorting_function, array):
    b1 = time.time()
    sorting_function(array)
    b2 = time.time() - b1
    print(f"Function [{sorting_function.b15}] finished in {b2:.3f} seconds")
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
    b8, b10 = fonk8(arr[:b11]), fonk8(arr[b11:])
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
def fonk10(arr):
    b3 = len(arr)
    for b13 in range(b3, -1, -1):
        fonk11(arr, b3, b13)
    for b13 in range(b3 - 1, 0, -1):
        arr[b13], arr[0] = arr[0], arr[b13]
        fonk11(arr, b13, 0)
def fonk11(arr, b3, b13):
    b14 = b13
    b8 = 2 * b13 + 1
    b10 = 2 * b13 + 2
    if b8 < b3 and arr[b13] < arr[b8]:
        b14 = b8
    if b10 < b3 and arr[b14] < arr[b10]:
        b14 = b10
    if b14 != b13:
        arr[b13], arr[b14] = arr[b14], arr[b13]
        fonk11(arr, b3, b14)
if b15 = = "__main__":
    b16 = {
        "Bubble": [random.randint(1, 500) for _ in range(10000)],
        "Insertion": [random.randint(1, 500) for _ in range(10000)],
        "Selection": [random.randint(1, 500) for _ in range(10000)],
        "Quick": [random.randint(1, 5000) for _ in range(10000)],
        "Merge": [random.randint(1, 5000) for _ in range(10000)],
        "Heap": [random.randint(1, 5000) for _ in range(10000)]
    }
    for name, array in b16.items():
        print(" ")
        b2 = fonk3(globals()[f"{name.lower()}_sort"], array)
        fonk2(array, name)