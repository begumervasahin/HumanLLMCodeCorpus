def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    low_vals = [x for x in arr if x < pivot]
    pivots = [x for x in arr if x == pivot]
    high_vals = [x for x in arr if x > pivot]
    low_sorted = quicksort(low_vals)
    high_sorted = quicksort(high_vals)
    sorted_arr = low_sorted + pivots + high_sorted
    return sorted_arr
if __name__ == "__main__":
    sorted_list = quicksort([1, 3, 5, 2])
    print("Sorted list:", sorted_list)