import random
def fonk1(b5):
    if not isinstance(b5, list):
        raise TypeError('Input must be a list.')
    if len(b5) < 2:
        return b5
    for b6 in range(1, len(b5)):
        b1 = b5[b6]
        b2 = b6 - 1
        while b2 >= 0 and b5[b2] > b1:
            b5[b2 + 1] = b5[b2]
            b2 -= 1
        b5[b2 + 1] = b1
    return b5
def fonk2(b5, low, high, pivot_type):
    b3 = {'first': low, 'last': high, 'middle': (low + high)
    b4 = b5[b3[pivot_type]]
    b5[b3[pivot_type]], b5[high] = b5[high], b5[b3[pivot_type]]
    return b4, b5
def fonk3(b5, low, high, pivot_type):
    b4, b5 = fonk2(b5, low, high, pivot_type)
    b6 = low - 1
    for b2 in range(low, high):
        if b5[b2] <= b4:
            b6 += 1
            b5[b6], b5[b2] = b5[b2], b5[b6]
    b5[b6 + 1], b5[high] = b5[high], b5[b6 + 1]
    return b6 + 1
def fonk4(b5, low, high, pivot_type, b7 = False, insertion_sort_threshold=10):
    if not isinstance(b5, list):
        raise TypeError('Input must be a list.')
    if low < high:
        if b7 and (high - low) < insertion_sort_threshold:
            fonk1(b5[low:high + 1])
        else:
            try:
                b8 = fonk3(b5, low, high, pivot_type)
                fonk4(b5, low, b8 - 1, pivot_type, b7, insertion_sort_threshold)
                fonk4(b5, b8 + 1, high, pivot_type, b7, insertion_sort_threshold)
            except KeyError:
                print('Pivot options: first, last, middle, random.')
if b9 = = "__main__":
    b10 = [3, 1, 7, 2, 9, 5, 4, 8, 6]
    print("Original list:", b10)
    b11 = fonk4(b10, 0, len(b10) - 1, 'first')
    print("Sorted list using Quicksort:", b11)