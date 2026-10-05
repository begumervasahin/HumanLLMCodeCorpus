def counting_sort(arr, verbose=0, desc=0):
    largest = max(arr)
    smallest = min(arr)
    if smallest:
        arr = [x - smallest for x in arr]
    if verbose:
        print("Normalized list:", arr)
    count = [0] * (largest - smallest + 1)
    for num in arr:
        count[num] += 1
    for i in range(1, len(count)):
        count[i] += count[i - 1]
        if verbose == 2:
            print("Cumulative count:", i, "::", count[i])
    n = len(arr)
    sorted_arr = [0] * n
    for i in range(n - 1, -1, -1):
        count[arr[i]] -= 1
        sorted_arr[count[arr[i]]] = arr[i]
        if verbose:
            print("Iteration", i, ":", sorted_arr)
    if smallest:
        sorted_arr = [x + smallest for x in sorted_arr]
    if desc:
        sorted_arr = sorted_arr[::-1]
    return sorted_arr