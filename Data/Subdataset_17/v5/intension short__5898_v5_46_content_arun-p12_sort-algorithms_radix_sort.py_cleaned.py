def radix_sort(arr, verbose=0, desc=0):
    def get_digit_count(n, base=10):
        count = 0
        while n > 0:
            count += 1
            n
        return count
    def get_digit_at_position(n, position, base=10):
        return (n
    def bucket_sort(arr, position, base=10):
        buckets = [[] for _ in range(base)]
        for num in arr:
            digit = get_digit_at_position(num, position, base)
            buckets[digit].append(num)
            if verbose == 2:
                print(f"Digit {digit} at position {position}: {buckets}")
        return [num for bucket in buckets for num in bucket]
    base = 10
    offset = -min(arr) if min(arr) < 0 else 0
    arr = [x + offset for x in arr]
    max_value = max(arr)
    num_passes = get_digit_count(max_value, base)
    for position in range(1, num_passes + 1):
        arr = bucket_sort(arr, position, base)
        if verbose:
            print(f"After pass {position}: {arr}")
    arr = [x - offset for x in arr]
    if desc:
        arr.reverse()
    return arr