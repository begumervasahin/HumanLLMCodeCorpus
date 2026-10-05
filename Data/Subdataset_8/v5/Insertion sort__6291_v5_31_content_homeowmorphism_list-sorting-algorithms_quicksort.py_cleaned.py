import random
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]
    left, right, pivot_clones = [], [], [pivot]
    for i, val in enumerate(arr):
        if i == pivot_index:
            continue
        if val < pivot:
            left.append(val)
        elif val > pivot:
            right.append(val)
        else:
            pivot_clones.append(val)
    sorted_left = quicksort(left)
    sorted_right = quicksort(right)
    return sorted_left + pivot_clones + sorted_right
original_list = [3, 6, 8, 10, 1, 2, 1]
print("Original list:", original_list)
print("Sorted list:", quicksort(original_list))