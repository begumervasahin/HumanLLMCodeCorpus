import common as c
def quick_sort(A, verbose=0, desc=0):
    def partition(lb, ub):
        pivot, start, end = A[lb], lb, ub
        while start < end:
            while A[start] <= pivot and start < ub:
                start += 1
            while A[end] > pivot and end > lb:
                end -= 1
            if start < end:
                A[start], A[end] = c.swap(A[start], A[end])
            if verbose == 2:
                print("  sub:", pivot, start, end, " :: ", A)
        A[lb], A[end] = c.swap(A[lb], A[end])
        return end
    def quick_sort_recursive(x, y):
        if x < y:
            loc = partition(x, y)
            if verbose:
                print("iter :", loc, x, y, " :: ", A)
            quick_sort_recursive(x, loc - 1)
            quick_sort_recursive(loc + 1, y)
    quick_sort_recursive(0, len(A) - 1)
    if desc:
        A = A[::-1]
    return A