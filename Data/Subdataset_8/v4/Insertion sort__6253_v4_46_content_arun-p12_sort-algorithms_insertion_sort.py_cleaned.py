def insertion_sort(arr, verbose=0, desc=0):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            if verbose == 2:
                print("Shifting:", j, "::", arr)
        arr[j + 1] = key
        if verbose:
            print("Iteration", i, ":", arr)
    if desc:
        arr = arr[::-1]
    return arr