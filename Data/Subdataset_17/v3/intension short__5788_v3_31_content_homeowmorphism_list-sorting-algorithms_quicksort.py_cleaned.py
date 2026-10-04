import random
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]
    print(f"Pivoting {pivot} in {arr}")
    left = [x for i, x in enumerate(arr) if x < pivot and i != pivot_index]
    right = [x for i, x in enumerate(arr) if x > pivot and i != pivot_index]
    pivot_clones = [x for x in arr if x == pivot]
    print(f"Left becomes {left}; right becomes {right}")
    return quicksort(left) + pivot_clones + quicksort(right)
unsorted_list = [random.randint(1, 100) for _ in range(10)]
print("Unsorted list:", unsorted_list)
sorted_list = quicksort(unsorted_list)
print("Sorted list:", sorted_list)