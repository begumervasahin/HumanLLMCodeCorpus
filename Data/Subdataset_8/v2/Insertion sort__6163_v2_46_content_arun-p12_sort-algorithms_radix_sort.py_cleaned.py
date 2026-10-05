import common as c
def radix_sort(arr, verbose=0, desc=0):
    def passes(number, base):
        count = 0
        while number:
            count += 1
            number = number
        return count
    def positional_digit(number, position, base=10):
        count, remainder, is_valid = 0, 0, True
        while is_valid:
            count += 1
            remainder = number % base
            number = number
            if count > position:
                is_valid = False
        return remainder
    def bucketize(position, base):
        n = len(arr)
        buckets = [[] for _ in range(n)]
        for i in range(n):
            digit = positional_digit(arr[i], position, base)
            buckets[digit].append(arr[i])
            if verbose == 2:
                print("    Bucket:", i, " :: ", buckets)
        return [buckets[x][y] for x in range(len(buckets)) for y in range(len(buckets[x]))]
    base = 10
    smallest = c.minimum(arr)[0]
    if smallest:
        arr = [x - smallest for x in arr]
    largest = c.maximum(arr)[0]
    iter_count = passes(largest, base)
    for i in range(iter_count):
        arr = bucketize(i, base)
        if verbose:
            print("Iteration", i + 1, ":", arr)
    if smallest:
        arr = [x + smallest for x in arr]
    if desc:
        arr = arr[::-1]
    return arr
if __name__ == "__main__":
    array = [170, 45, 75, 90, 802, 24, 2, 66]
    print("Original Array:", array)
    sorted_array = radix_sort(array, verbose=1, desc=0)
    print("Sorted Array:", sorted_array)