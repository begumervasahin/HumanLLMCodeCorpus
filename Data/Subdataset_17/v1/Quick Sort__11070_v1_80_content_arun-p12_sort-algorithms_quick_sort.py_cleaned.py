def quick_sort(A, verbose=0, desc=0):
    '''Quick sort -- time taken as a function of size
       - best ==> size  O(n.log(n))  worst ==> size**2 i.e. O(n**2)
       Take a pivot element, any element (say the first element). Generate two sub-lists;
       one that has numbers lower in value to the pivot. Another that has numbers higher in value.
       Repeat process for the sublists.'''
    def swap(x, y):
        return y, x
    def partition(lb, ub):
        pivot, start, end = A[lb], lb, ub
        while start < end:
            while A[start] <= pivot and start < ub:
                start += 1
            while A[end] > pivot and end > lb:
                end -= 1
            if start < end:
                A[start], A[end] = swap(A[start], A[end])
            if verbose == 2:
                print("  sub:", pivot, start, end, " :: ", A)
        A[lb], A[end] = swap(A[lb], A[end])
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
if __name__ == "__main__":
    A = [3, 6, 8, 10, 1, 2, 1]
    sorted_list = quick_sort(A, verbose=1, desc=0)
    print("Sorted list:", sorted_list)