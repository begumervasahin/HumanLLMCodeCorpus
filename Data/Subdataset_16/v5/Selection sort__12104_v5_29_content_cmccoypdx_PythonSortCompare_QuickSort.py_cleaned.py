import random
def fonk1(arr, low, high):
    b1 = arr[low]
    b2 = low
    b3 = high + 1
    while True:
        while True:
            b2 += 1
            if b2 >= len(arr) or arr[b2] >= b1:
                break
        while True:
            b3 -= 1
            if b3 <= 0 or arr[b3] <= b1:
                break
        if b2 >= b3:
            break
        arr[b2], arr[b3] = arr[b3], arr[b2]
    arr[low], arr[b3] = arr[b3], arr[low]
    return b3
def fonk2(arr, low, high):
    if low < high:
        b4 = fonk1(arr, low, high)
        fonk2(arr, low, b4 - 1)
        fonk2(arr, b4 + 1, high)
def fonk3(arr):
    fonk2(arr, 0, len(arr) - 1)
if b5 = = "__main__":
    b6 = [random.randint(0, 100) for _ in range(10)]
    print(f"Unsorted list: {b6}")
    fonk3(b6)
    print(f"Sorted list: {b6}")