import random
def quicksort(lst):
    if len(lst) <= 1:
        return lst
    pivot_index = random.randint(0, len(lst) - 1)
    pivot = lst[pivot_index]
    print(f"Pivoting {pivot} in {lst}")
    left = []
    right = []
    pivot_clones = []
    for i, value in enumerate(lst):
        if i == pivot_index:
            pivot_clones.append(value)
        elif value < pivot:
            left.append(value)
        elif value > pivot:
            right.append(value)
        else:
            pivot_clones.append(value)
    print(f"Left: {left}; Right: {right}; Pivot clones: {pivot_clones}")
    return quicksort(left) + pivot_clones + quicksort(right)
lst = [3, 6, 8, 10, 1, 2, 1]
sorted_lst = quicksort(lst)
print("Sorted result:", sorted_lst)