def quick_sort_lomuto(arr):
    def lomuto_partition(arr, start, end):
        pivot = arr[end]
        i = start - 1
        for j in range(start, end):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[end] = arr[end], arr[i + 1]
        return i + 1
    def quick_sort_lomuto_helper(arr, start, end):
        if start < end:
            pivot_index = lomuto_partition(arr, start, end)
            quick_sort_lomuto_helper(arr, start, pivot_index - 1)
            quick_sort_lomuto_helper(arr, pivot_index + 1, end)
    quick_sort_lomuto_helper(arr, 0, len(arr) - 1)
    return arr
def quick_sort_hoare(arr):
    def hoare_partition(arr, start, end):
        pivot = arr[start]
        i = start - 1
        j = end + 1
        while True:
            i += 1
            while arr[i] < pivot:
                i += 1
            j -= 1
            while arr[j] > pivot:
                j -= 1
            if i >= j:
                return j
            arr[i], arr[j] = arr[j], arr[i]
    def quick_sort_hoare_helper(arr, start, end):
        if start < end:
            pivot_index = hoare_partition(arr, start, end)
            quick_sort_hoare_helper(arr, start, pivot_index)
            quick_sort_hoare_helper(arr, pivot_index + 1, end)
    quick_sort_hoare_helper(arr, 0, len(arr) - 1)
    return arr
if __name__ == "__main__":
    arr = [15, 4, 68, 24, 75, 16, 42]
    arr_hoare = arr.copy()
    sorted_hoare = quick_sort_hoare(arr_hoare)
    print("Sorted using Hoare partition:", sorted_hoare)
    arr_lomuto = arr.copy()
    sorted_lomuto = quick_sort_lomuto(arr_lomuto)
    print("Sorted using Lomuto partition:", sorted_lomuto)