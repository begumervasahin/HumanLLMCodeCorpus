def counting_sort(arr, verbose=0, desc=False):
    if not arr:
        return []
    min_value = min(arr)
    max_value = max(arr)
    normalized_arr = [x - min_value for x in arr] if min_value < 0 else arr
    if verbose:
        print("Normalized array:", normalized_arr)
    range_size = max_value - min_value + 1
    count = [0] * range_size
    for number in normalized_arr:
        count[number] += 1
    for i in range(1, range_size):
        count[i] += count[i - 1]
        if verbose == 2:
            print(f"Cumulative count at index {i}: {count}")
    output = [0] * len(arr)
    for number in reversed(normalized_arr):
        count[number] -= 1
        output[count[number]] = number
    sorted_arr = [x + min_value for x in output] if min_value < 0 else output
    if desc:
        sorted_arr.reverse()
    return sorted_arr
if __name__ == "__main__":
    sample_array = [4, 2, 2, 8, 3, 3, 1]
    sorted_array = counting_sort(sample_array, verbose=1)
    print("Sorted array:", sorted_array)