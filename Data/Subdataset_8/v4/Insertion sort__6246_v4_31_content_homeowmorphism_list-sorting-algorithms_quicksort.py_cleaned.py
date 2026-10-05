import random
def quicksort(arr):
    n = len(arr)
    if n > 1:
        pivot_index = random.randint(0, n - 1)
        pivot = arr[pivot_index]
        print("Pivoting", pivot, "in", arr)
        left = []
        right = []
        pivot_clones = [pivot]
        for i in range(n):
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
    return arr
l = [3, 6, 8, 10, 1, 2, 1]
print("Original list:", l)
print("Sorted list:", quicksort(l))