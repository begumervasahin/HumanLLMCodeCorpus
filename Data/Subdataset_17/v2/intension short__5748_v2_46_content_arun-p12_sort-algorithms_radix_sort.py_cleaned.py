def radix_sort(arr, base=10, verbose=False, desc=False):
    def get_digit_count(number, base):
        count = 0
        while number > 0:
            count += 1
            number
        return count
    def extract_digit(number, position, base):
        return (number
    def distribute_to_buckets(arr, position, base):
        buckets = [[] for _ in range(base)]
        for number in arr:
            digit = extract_digit(number, position, base)
            buckets[digit].append(number)
            if verbose == 2:
                print(f"Placing number {number} in bucket {digit}: {buckets}")
        return [num for bucket in buckets for num in bucket]
    min_value = min(arr)
    if min_value < 0:
        arr = [num - min_value for num in arr]
    max_value = max(arr)
    num_passes = get_digit_count(max_value, base)
    for pos in range(num_passes):
        arr = distribute_to_buckets(arr, pos, base)
        if verbose:
            print(f"After pass {pos + 1}: {arr}")
    if min_value < 0:
        arr = [num + min_value for num in arr]
    if desc:
        arr.reverse()
    return arr
if __name__ == "__main__":
    sample_array = [170, 45, 75, 90, 802, 24, 2, 66]
    sorted_array = radix_sort(sample_array, verbose=True, desc=False)
    print("Sorted Array:", sorted_array)