def radix_sort(arr, base=10, verbose=False, desc=False):
    def calculate_digit_count(number, base):
        digit_count = 0
        while number > 0:
            digit_count += 1
            number
        return digit_count
    def get_digit_at_position(number, position, base):
        return (number
    def sort_into_buckets(arr, position, base):
        buckets = [[] for _ in range(base)]
        for number in arr:
            digit = get_digit_at_position(number, position, base)
            buckets[digit].append(number)
            if verbose == 2:
                print(f"Number {number} placed in bucket {digit}: {buckets}")
        return [num for bucket in buckets for num in bucket]
    min_value = min(arr)
    if min_value < 0:
        arr = [num - min_value for num in arr]
    max_value = max(arr)
    digit_count = calculate_digit_count(max_value, base)
    for position in range(digit_count):
        arr = sort_into_buckets(arr, position, base)
        if verbose:
            print(f"After pass {position + 1}: {arr}")
    if min_value < 0:
        arr = [num + min_value for num in arr]
    if desc:
        arr.reverse()
    return arr
if __name__ == "__main__":
    sample_array = [170, 45, 75, 90, 802, 24, 2, 66]
    sorted_array = radix_sort(sample_array, verbose=True, desc=False)
    print("Sorted Array:", sorted_array)