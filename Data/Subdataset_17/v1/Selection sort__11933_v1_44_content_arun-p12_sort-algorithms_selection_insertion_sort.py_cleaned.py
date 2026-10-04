def selection_insertion_sort(A, verbose=0, desc=0):
    def find_minimum(A):
        if not isinstance(A, list) or len(A) == 0:
            print("List expected. Got:", A)
            exit(1)
        min_val, index = A[0], 0
        for i in range(1, len(A)):
            if A[i] < min_val:
                min_val = A[i]
                index = i
        return (min_val, index)
    def s_i_sort(A):
        if len(A) <= 1:
            return A
        n = len(A)
        val, index = find_minimum(A)
        while index > 0:
            if verbose == 2:
                print("  sub:", index, A[index], " :: ", A)
            A[index] = A[index - 1]
            index -= 1
        A[0] = val
        if verbose:
            print("iteration:", A)
        A = [val] + s_i_sort(A[1:])
        return A
    A = s_i_sort(A)
    if desc:
        A = A[::-1]
    return A
if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    print("Array before sorting:")
    print(arr)
    sorted_arr = selection_insertion_sort(arr, verbose=1, desc=0)
    print("Sorted array is:")
    print(sorted_arr)