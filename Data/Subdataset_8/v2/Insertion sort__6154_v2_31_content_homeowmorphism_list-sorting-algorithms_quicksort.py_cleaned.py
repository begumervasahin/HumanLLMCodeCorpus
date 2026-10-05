import random
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]
    print("Pivoting", pivot, "in", arr)
    left = []
    right = []
    pivot_clones = [pivot]
    for i in range(len(arr)):
        if i == pivot_index:
            continue
        elif arr[i] < pivot:
            left.append(arr[i])
        elif arr[i] > pivot:
            right.append(arr[i])
        else:
            pivot_clones.append(arr[i])
    print("Left becomes", left, "; right becomes", right)
    sorted_left = quicksort(left)
    sorted_right = quicksort(right)
    return sorted_left + pivot_clones + sorted_right
original_list = [3, 6, 8, 10, 1, 2, 1]
print("Original list:", original_list)
print("Sorted list:", quicksort(original_list))