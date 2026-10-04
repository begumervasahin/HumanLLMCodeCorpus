def quick_sort(arr, verbose=0, desc=0):
    def swap(x, y):
        return y, x
    def partition(low, high):
        pivot = arr[low]
        start = low
        end = high
        while start < end:
            while start < high and arr[start] <= pivot:
                start += 1
            while end > low and arr[end] > pivot:
                end -= 1
            if start < end:
                arr[start], arr[end] = swap(arr[start], arr[end])
            if verbose == 2:
                print("  sub:", pivot, start, end, " :: ", arr)
        arr[low], arr[end] = swap(arr[low], arr[end])
        return end
    def quick_sort_recursive(low, high):
        if low < high:
            pivot_index = partition(low, high)
            if verbose >= 1:
                print("iter:", pivot_index, low, high, "::", arr)
            quick_sort_recursive(low, pivot_index - 1)
            quick_sort_recursive(pivot_index + 1, high)
    quick_sort_recursive(0, len(arr) - 1)
    if desc:
        arr.reverse()
    return arr
if __name__ == "__main__":
    A = [3, 6, 8, 10, 1, 2, 1]
    sorted_list = quick_sort(A, verbose=1, desc=0)
    print("Sorted list:", sorted_list)