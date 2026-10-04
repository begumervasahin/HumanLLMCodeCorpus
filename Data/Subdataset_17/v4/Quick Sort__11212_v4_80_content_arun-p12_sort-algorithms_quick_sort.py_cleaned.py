import common as c
def quick_sort(arr, verbose=0, desc=0):
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
                arr[start], arr[end] = c.swap(arr[start], arr[end])
            if verbose == 2:
                print("  sub:", pivot, start, end, " :: ", arr)
        arr[low], arr[end] = c.swap(arr[low], arr[end])
        return end
    def quick_sort_recursive(low, high):
        if low < high:
            pivot_index = partition(low, high)
            if verbose:
                print("iter :", pivot_index, low, high, " :: ", arr)
            quick_sort_recursive(low, pivot_index - 1)
            quick_sort_recursive(pivot_index + 1, high)
    quick_sort_recursive(0, len(arr) - 1)
    if desc:
        arr.reverse()
    return arr