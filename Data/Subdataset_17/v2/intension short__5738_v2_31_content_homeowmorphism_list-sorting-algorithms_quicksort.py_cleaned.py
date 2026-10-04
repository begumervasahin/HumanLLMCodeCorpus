import random
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]
    print(f"Pivoting {pivot} in {arr}")
    left = []
    right = []
    pivot_clones = []
    for i, value in enumerate(arr):
        if i == pivot_index:
            pivot_clones.append(pivot)
        elif value < pivot:
            left.append(value)
        elif value > pivot:
            right.append(value)
        else:
            pivot_clones.append(value)
    print(f"Left becomes {left}; right becomes {right}")
    return quicksort(left) + pivot_clones + quicksort(right)
unsorted_list = [random.randint(1, 100) for _ in range(10)]
print("Unsorted list:", unsorted_list)
sorted_list = quicksort(unsorted_list)
print("Sorted list:", sorted_list)