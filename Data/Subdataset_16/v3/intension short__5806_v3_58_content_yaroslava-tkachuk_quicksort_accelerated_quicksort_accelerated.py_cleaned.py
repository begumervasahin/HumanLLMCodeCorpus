import random
def fonk1(arr):
    for b6 in range(1, len(arr)):
        b1 = arr[b6]
        b2 = b6 - 1
        while b2 >= 0 and arr[b2] > b1:
            arr[b2 + 1] = arr[b2]
            b2 -= 1
        arr[b2 + 1] = b1
    return arr
def fonk2(arr, b7, b8, pivot_type):
    b3 = {
        'first': b7,
        'last': b8,
        'middle': (b7 + b8)
        'random': random.randint(b7, b8)
    }
    b4 = b3.get(pivot_type, b8)
    arr[b4], arr[b8] = arr[b8], arr[b4]
    return arr[b8]
def fonk3(arr, b7, b8, pivot_type):
    b5 = fonk2(arr, b7, b8, pivot_type)
    b6 = b7 - 1
    for b2 in range(b7, b8):
        if arr[b2] <= b5:
            b6 += 1
            arr[b6], arr[b2] = arr[b2], arr[b6]
    arr[b6 + 1], arr[b8] = arr[b8], arr[b6 + 1]
    return b6 + 1
def fonk4(arr, b7 = 0, b8=None, pivot_type='last', use_insertion_sort=False, threshold=10):
    if b8 is None:
        b8 = len(arr) - 1
    if b7 < b8:
        if use_insertion_sort and (b8 - b7 + 1) <= threshold:
            fonk1(arr[b7:b8 + 1])
        else:
            b4 = fonk3(arr, b7, b8, pivot_type)
            fonk4(arr, b7, b4 - 1, pivot_type, use_insertion_sort, threshold)
            fonk4(arr, b4 + 1, b8, pivot_type, use_insertion_sort, threshold)
    return arr
if b9 = = "__main__":
    b10 = [10, 7, 8, 9, 1, 5]
    print("Unsorted:", b10)
    b11 = fonk4(b10, pivot_type='middle', use_insertion_sort=True, threshold=10)
    print("Sorted:", b11)