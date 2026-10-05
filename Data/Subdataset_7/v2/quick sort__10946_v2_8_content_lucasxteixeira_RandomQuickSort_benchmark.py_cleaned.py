import timeit
import random
def fonk1(arr, low, high):
    if low < high:
        b1 = fonk2(arr, low, high)
        fonk1(arr, low, b1 - 1)
        fonk1(arr, b1 + 1, high)
def fonk2(arr, low, high):
    b2 = arr[high]
    b3 = low - 1
    for j in range(low, high):
        if arr[j] <= b2:
            b3 += 1
            arr[b3], arr[j] = arr[j], arr[b3]
    arr[b3 + 1], arr[high] = arr[high], arr[b3 + 1]
    return b3 + 1
def fonk3(arr, low, high):
    if low < high:
        b1 = fonk4(arr, low, high)
        fonk3(arr, low, b1 - 1)
        fonk3(arr, b1 + 1, high)
def fonk4(arr, low, high):
    b4 = random.randint(low, high)
    arr[high], arr[b4] = arr[b4], arr[high]
    return fonk2(arr, low, high)
def fonk5(arr, low, high):
    if low < high:
        b1 = fonk6(arr, low, high)
        fonk5(arr, low, b1 - 1)
        fonk5(arr, b1 + 1, high)
def fonk6(arr, low, high):
    b5 = fonk7(arr, low, high)
    arr[high], arr[b5] = arr[b5], arr[high]
    return fonk2(arr, low, high)
def fonk7(arr, low, high):
    b6 = (low + high)
    if arr[low] <= arr[b6] <= arr[high] or arr[high] <= arr[b6] <= arr[low]:
        return b6
    elif arr[b6] <= arr[low] <= arr[high] or arr[high] <= arr[low] <= arr[b6]:
        return low
    else:
        return high
if b7 = = "__main__":
    print("Quick Sort")
    for size in [1000, 10000, 100000]:
        b8 = [random.random() for _ in range(size)]
        print(f"{size} elements:")
        print(min(timeit.Timer('b9 = b8[:]; fonk1(b9, 0, len(b9) - 1)', globals=globals()).repeat(10, 100)))
    print("Random Quick Sort")
    for size in [1000, 10000, 100000]:
        b8 = [random.random() for _ in range(size)]
        print(f"{size} elements:")
        print(min(timeit.Timer('b9 = b8[:]; fonk3(b9, 0, len(b9) - 1)', globals=globals()).repeat(10, 100)))
    print("Median Random Quick Sort")
    for size in [1000, 10000, 100000]:
        b8 = [random.random() for _ in range(size)]
        print(f"{size} elements:")
        print(min(timeit.Timer('b9 = b8[:]; fonk5(b9, 0, len(b9) - 1)', globals=globals()).repeat(10, 100)))