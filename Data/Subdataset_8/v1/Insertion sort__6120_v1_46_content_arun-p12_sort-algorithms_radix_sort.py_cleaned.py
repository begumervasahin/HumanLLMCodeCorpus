import common as c
def radix_sort(A, verbose=0, desc=0):
    def passes(n, b):
        cnt = 0
        while n:
            cnt += 1
            n = n
        return cnt
    def positional_digit(n, pos, b=10):
        cnt, rem, ok = 0, 0, True
        while ok:
            cnt += 1
            rem = n % b
            n = n
            if cnt > pos:
                ok = False
        return rem
    def bucketize(pos, b):
        n = len(A)
        B = [[] for _ in range(n)]
        for i in range(n):
            bucket = positional_digit(A[i], pos, b)
            B[bucket].append(A[i])
            if verbose == 2:
                print("    B:", i, " :: ", B)
        return [B[x][y] for x in range(len(B)) for y in range(len(B[x]))]
    b = 10
    smallest = c.minimum(A)[0]
    if smallest:
        A = [x - smallest for x in A]
    largest = c.maximum(A)[0]
    iter_count = passes(largest, b)
    for i in range(iter_count):
        A = bucketize(i, b)
        if verbose:
            print("Iteration", i + 1, ":", A)
    if smallest:
        A = [x + smallest for x in A]
    if desc:
        A = A[::-1]
    return A
if __name__ == "__main__":
    array = [170, 45, 75, 90, 802, 24, 2, 66]
    print("Original Array:", array)
    sorted_array = radix_sort(array, verbose=1, desc=0)
    print("Sorted Array:", sorted_array)