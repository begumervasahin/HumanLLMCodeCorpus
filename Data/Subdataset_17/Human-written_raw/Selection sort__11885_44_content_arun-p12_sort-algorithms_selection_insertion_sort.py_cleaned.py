def selection_insertion_sort(A, verbose=0, desc=0):
    def s_i_sort(A):
        import common as c
        if (len(A) <= 1): return (A)
        n = len(A)
        val, index = c.minimum(A)
        while(index > 0):
            if(verbose == 2): print("  sub:", index, A[index], " :: ", A)
            A[index] = A[index-1]
            index -= 1
        A[0] = val
        if(verbose): print("iter
        A = [val] + s_i_sort(A[1:])
        return(A)
    A = s_i_sort(A)
    if(desc): A = A[::-1]
    return(A)