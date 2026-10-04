import random
def quicksort(lst):
    if len(lst) <= 1:
        return lst
    pivot_index = random.randint(0, len(lst) - 1)
    pivot = lst[pivot_index]
    print(f"Pivoting {pivot} in {lst}")
    left = []
    right = []
    pivot_clones = [pivot]
    for i in range(len(lst)):
        if i == pivot_index:
            continue
        if lst[i] < pivot:
            left.append(lst[i])
        elif lst[i] > pivot:
            right.append(lst[i])
        else:
            pivot_clones.append(lst[i])
    print(f"Left becomes {left}; right becomes {right}")
    return quicksort(left) + pivot_clones + quicksort(right)
lst = [3, 6, 8, 10, 1, 2, 1]
print("Result:", quicksort(lst))