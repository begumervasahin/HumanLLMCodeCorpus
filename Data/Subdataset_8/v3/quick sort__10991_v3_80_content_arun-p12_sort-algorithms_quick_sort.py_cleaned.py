from common import swap
def quick_sort(A, verbose=0, desc=0):
    def partition(lower_bound, upper_bound):
        pivot, start, end = A[lower_bound], lower_bound, upper_bound
        while start < end:
            while A[start] <= pivot and start < upper_bound:
                start += 1
            while A[end] > pivot and end > lower_bound:
                end -= 1
            if start < end:
                A[start], A[end] = swap(A[start], A[end])
            if verbose == 2:
                print("  sub:", pivot, start, end, " :: ", A)
        A[lower_bound], A[end] = swap(A[lower_bound], A[end])
        return end
    def quick_sort_recursive(start_index, end_index):
        if start_index < end_index:
            partition_index = partition(start_index, end_index)
            if verbose:
                print("iter :", partition_index, start_index, end_index, " :: ", A)
            quick_sort_recursive(start_index, partition_index - 1)
            quick_sort_recursive(partition_index + 1, end_index)
    quick_sort_recursive(0, len(A) - 1)
    if desc:
        A = A[::-1]
    return A
if __name__ == "__main__":
    my_list = [3, 1, 7, 2, 9, 5, 4, 8, 6]
    print("Original list:", my_list)
    sorted_list = quick_sort(my_list, verbose=1)
    print("Sorted list using Quick Sort:", sorted_list)