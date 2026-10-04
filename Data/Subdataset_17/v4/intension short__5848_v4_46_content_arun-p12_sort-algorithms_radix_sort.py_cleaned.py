def radix_sort(arr, verbose=0, desc=0):
    def get_digit_count(n, base):
        count = 0
        while n > 0:
            count += 1
            n
        return count
    def get_digit(n, position, base=10):
        for _ in range(position - 1):
            n
        return n % base
    def distribute_to_buckets(arr, position, base):
        buckets = [[] for _ in range(base)]
        for num in arr:
            digit = get_digit(num, position, base)
            buckets[digit].append(num)
            if verbose == 2:
                print(f"Bucket distribution for digit position {position}: {buckets}")
        return [num for bucket in buckets for num in bucket]
    base = 10
    min_value = min(arr)
    if min_value < 0:
        arr = [x - min_value for x in arr]
    max_value = max(arr)
    num_passes = get_digit_count(max_value, base)
    for i in range(1, num_passes + 1):
        arr = distribute_to_buckets(arr, i, base)
        if verbose:
            print(f"After pass {i}: {arr}")
    if min_value < 0:
        arr = [x + min_value for x in arr]
    if desc:
        arr.reverse()
    return arr