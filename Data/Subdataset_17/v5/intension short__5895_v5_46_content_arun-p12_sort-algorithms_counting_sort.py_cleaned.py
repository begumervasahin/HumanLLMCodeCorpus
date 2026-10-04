def counting_sort(arr, verbose=0, desc=0):
    if not arr:
        return []
    smallest = min(arr)
    largest = max(arr)
    normalized_arr = [x - smallest for x in arr]
    if verbose:
        print("Normalized array:", normalized_arr)
    range_size = largest - smallest + 1
    count = [0] * range_size
    for num in normalized_arr:
        count[num] += 1
    for i in range(1, range_size):
        count[i] += count[i - 1]
        if verbose == 2:
            print(f"Cumulative count at index {i}: {count[i]}")
    output = [0] * len(arr)
    for num in reversed(normalized_arr):
        count[num] -= 1
        output[count[num]] = num
    if verbose:
        print("Sorted output (before denormalization):", output)
    denormalized_output = [x + smallest for x in output]
    if desc:
        denormalized_output.reverse()
    return denormalized_output