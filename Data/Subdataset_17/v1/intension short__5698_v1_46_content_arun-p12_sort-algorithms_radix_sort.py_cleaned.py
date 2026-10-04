def radix_sort(arr, base=10, verbose=False, desc=False):
    def passes(n, base):
        cnt = 0
        while n > 0:
            cnt += 1
            n
        return cnt
    def positional_digit(n, pos, base=10):
        return (n
    def bucketize(arr, pos, base):
        buckets = [[] for _ in range(base)]
        for number in arr:
            digit = positional_digit(number, pos, base)
            buckets[digit].append(number)
            if verbose == 2:
                print(f"Number {number} goes to bucket {digit}: {buckets}")
        return [num for bucket in buckets for num in bucket]
    min_value = min(arr)
    if min_value < 0:
        arr = [num - min_value for num in arr]
    max_value = max(arr)
    num_passes = passes(max_value, base)
    for pos in range(num_passes):
        arr = bucketize(arr, pos, base)
        if verbose:
            print(f"After pass {pos + 1}: {arr}")
    if min_value < 0:
        arr = [num + min_value for num in arr]
    if desc:
        arr = arr[::-1]
    return arr
if __name__ == "__main__":
    sample_array = [170, 45, 75, 90, 802, 24, 2, 66]
    sorted_array = radix_sort(sample_array, verbose=True, desc=False)
    print("Sorted Array:", sorted_array)