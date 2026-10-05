import random
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]
    print("Pivot element:", pivot, "in list:", arr)
    left = []
    right = []
    pivot_clones = [pivot]
    for i, num in enumerate(arr):
        if i == pivot_index:
            continue
        elif num < pivot:
            left.append(num)
        elif num > pivot:
            right.append(num)
        else:
            pivot_clones.append(num)
    print("Left sublist:", left, "; Right sublist:", right)
    sorted_left = quicksort(left)
    sorted_right = quicksort(right)
    return sorted_left + pivot_clones + sorted_right
original_list = [3, 6, 8, 10, 1, 2, 1]
print("Original list:", original_list)
print("Sorted list:", quicksort(original_list))