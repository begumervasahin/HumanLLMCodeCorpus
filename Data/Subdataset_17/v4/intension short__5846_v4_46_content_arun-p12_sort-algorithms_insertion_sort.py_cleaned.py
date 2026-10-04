def insertion_sort(arr, verbose=0, desc=False):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            if verbose == 2:
                print(f"  Subarray after shifting: {arr}")
        arr[j + 1] = key
        if verbose >= 1:
            print(f"Iteration {i}: {arr}")
    if desc:
        arr.reverse()
    return arr