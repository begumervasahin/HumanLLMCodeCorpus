def shell_sort(arr, verbose=0, desc=False):
    def insertion_sort_with_gap(arr, gap):
        for i in range(gap, len(arr)):
            current_value = arr[i]
            j = i
            while j >= gap and arr[j - gap] > current_value:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = current_value
            if verbose == 2:
                print(f"  Current state after gap {gap}: {arr}")
    gap = len(arr)
    while gap > 0:
        if verbose >= 1:
            print(f"Gap: {gap}")
        insertion_sort_with_gap(arr, gap)
        gap
    if desc:
        arr.reverse()
    return arr