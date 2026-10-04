def counting_sort(arr, verbose=0, desc=0):
    smallest = min(arr)
    largest = max(arr)
    if smallest < 0:
        normalized_arr = [x - smallest for x in arr]
    else:
        normalized_arr = arr.copy()
    if verbose:
        print("Normalized array:", normalized_arr)
    count = [0] * (largest - smallest + 1)
    for num in normalized_arr:
        count[num] += 1
    for i in range(1, len(count)):
        count[i] += count[i - 1]
        if verbose == 2:
            print(f"Cumulative count at index {i}: {count[i]}")
    output = [0] * len(arr)
    for num in reversed(normalized_arr):
        count[num] -= 1
        output[count[num]] = num
    if verbose:
        print("Sorted output (before denormalization):", output)
    if smallest < 0:
        output = [x + smallest for x in output]
    if desc:
        output.reverse()
    return output