'''
Quick sort -- time taken as a function of size
    - best ==> size  O(n.log(n))  worst ==> size**2 i.e. O(n**2)
Take a pivot element, any element (say the first element). Generate two sub-lists;
one that has numbers lower in value to the pivot. Another that has numbers higher in value.
Repeat process for the sublists.
'''
def quick_sort(A, verbose=0, desc=0):
    import common as c
    def partition(lb, ub):
        pivot, start, end = A[lb], lb, ub
        while(start < end):
            while((A[start] <= pivot) and (start < ub)): start += 1
            while ((A[end] > pivot) and (end > lb)): end -= 1
            if(start < end):
                A[start], A[end] = c.swap(A[start], A[end])
            if(verbose == 2): print("  sub:", pivot, start, end, " :: ", A)
        A[lb], A[end] = c.swap(A[lb], A[end])
        return(end)
    def quick_sort(x, y):
        if(x < y):
            loc = partition(x, y)
            if(verbose): print("iter :", loc, x, y, " :: ", A)
            quick_sort(x, loc-1)
            quick_sort(loc+1, y)
    quick_sort(0, len(A) -1)
    if(desc): A = A[::-1]
    return(A)