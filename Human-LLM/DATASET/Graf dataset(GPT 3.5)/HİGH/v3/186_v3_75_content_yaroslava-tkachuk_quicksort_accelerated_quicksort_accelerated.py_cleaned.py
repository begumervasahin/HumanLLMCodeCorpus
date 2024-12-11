import random
def fonk1(arr):
    if not isinstance(arr, list):
        raise TypeError('Input must be a list.')
    for b5 in range(1, len(arr)):
        b1 = arr[b5]
        b2 = b5 - 1
        while b2 >= 0 and arr[b2] > b1:
            arr[b2 + 1] = arr[b2]
            b2 -= 1
        arr[b2 + 1] = b1
    return arr
def fonk2(arr, low, high, pivot_type):
    b3 = {'first': low, 'last': high, 'middle': (low + high)
    b4 = arr[b3[pivot_type]]
    arr[b3[pivot_type]], arr[high] = arr[high], arr[b3[pivot_type]]
    return b4
def fonk3(arr, low, high, pivot_type):
    b4 = fonk2(arr, low, high, pivot_type)
    b5 = low - 1
    for b2 in range(low, high):
        if arr[b2] <= b4:
            b5 += 1
            arr[b5], arr[b2] = arr[b2], arr[b5]
    arr[b5 + 1], arr[high] = arr[high], arr[b5 + 1]
    return b5 + 1
def fonk4(arr, low, high, pivot_type, b6 = False, insertion_sort_threshold=10):
    if low < high:
        if b6 and (high - low) < insertion_sort_threshold:
            fonk1(arr[low:high + 1])
        else:
            try:
                b7 = fonk3(arr, low, high, pivot_type)
                fonk4(arr, low, b7 - 1, pivot_type, b6, insertion_sort_threshold)
                fonk4(arr, b7 + 1, high, pivot_type, b6, insertion_sort_threshold)
            except KeyError:
                print('Pivot options: first, last, middle, random.')
if b8 = = "__main__":
    b9 = [3, 1, 7, 2, 9, 5, 4, 8, 6]
    print("Original list:", b9)
    fonk4(b9, 0, len(b9) - 1, 'first')
    print("Sorted list using Quicksort:", b9)