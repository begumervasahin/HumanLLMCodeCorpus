def insertion_sort(arr, verbose=0, desc=False):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            if verbose == 2:
                print("  sub:", j, " :: ", arr)
        arr[j + 1] = key
        if verbose >= 1:
            print(f"Iteration {i}: {arr}")
    if desc:
        arr = arr[::-1]
    return arr
if __name__ == "__main__":
    sample_array = [12, 11, 13, 5, 6]
    sorted_array = insertion_sort(sample_array, verbose=1, desc=False)
    print("Sorted array:", sorted_array)