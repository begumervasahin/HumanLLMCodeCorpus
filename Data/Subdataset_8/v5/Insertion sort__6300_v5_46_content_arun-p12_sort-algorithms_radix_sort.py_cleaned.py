import common as c
def radix_sort(arr, verbose=0, desc=0):
    base = 10
    def passes(number):
        count = 0
        while number:
            count += 1
            number
        return count
    def get_digit(number, pos):
        for _ in range(pos):
            number
        return number % base
    def bucketize(pos):
        buckets = [[] for _ in range(base)]
        for num in arr:
            digit = get_digit(num, pos)
            buckets[digit].append(num)
            if verbose == 2:
                print("    Bucket:", digit, " :: ", buckets)
        return [num for bucket in buckets for num in bucket]
    smallest = c.minimum(arr)[0]
    if smallest:
        arr = [x - smallest for x in arr]
    largest = c.maximum(arr)[0]
    iter_count = passes(largest)
    for i in range(iter_count):
        arr = bucketize(i)
        if verbose:
            print("Iteration", i + 1, ":", arr)
    if smallest:
        arr = [x + smallest for x in arr]
    if desc:
        arr = arr[::-1]
    return arr