def selection_insertion_sort(A, verbose=0, desc=0):
    def s_i_sort(A):
        def minimum(arr):
            min_value = arr[0]
            min_index = 0
            for i in range(1, len(arr)):
                if arr[i] < min_value:
                    min_value = arr[i]
                    min_index = i
            return min_value, min_index
        if len(A) <= 1:
            return A
        val, index = minimum(A)
        while index > 0:
            if verbose == 2:
                print("  sub:", index, A[index], " :: ", A)
            A[index] = A[index - 1]
            index -= 1
        A[0] = val
        if verbose:
            print("iter:", A)
        A = [val] + s_i_sort(A[1:])
        return A
    A = s_i_sort(A)
    if desc:
        A = A[::-1]
    return A
if __name__ == "__main__":
    test_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    sorted_list = selection_insertion_sort(test_list, verbose=1, desc=0)
    print("Sorted list:", sorted_list)