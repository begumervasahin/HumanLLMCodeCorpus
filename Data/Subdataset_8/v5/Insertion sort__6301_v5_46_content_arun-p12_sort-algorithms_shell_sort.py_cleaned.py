def shell_sort(arr, verbose=0, desc=0):
    def insertion_sort(gap, start_index=0):
        j = start_index + gap
        n = len(arr)
        if start_index < 0 or j >= n:
            return
        if verbose == 2:
            print("Sub:", start_index, "-", j, "::", arr)
        if arr[start_index] > arr[j]:
            arr[start_index], arr[j] = arr[j], arr[start_index]
            insertion_sort(gap, start_index - gap)
        insertion_sort(gap, start_index + 1)
    gap = len(arr)
    while gap:
        if verbose:
            print("Gap:", gap)
        insertion_sort(gap)
        gap
    if desc:
        arr = arr[::-1]
    return arr