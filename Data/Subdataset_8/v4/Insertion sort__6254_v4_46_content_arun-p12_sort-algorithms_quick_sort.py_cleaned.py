def quick_sort(arr, verbose=0, desc=0):
    def partition(left, right):
        pivot = arr[left]
        start, end = left, right
        while start < end:
            while start < right and arr[start] <= pivot:
                start += 1
            while end > left and arr[end] > pivot:
                end -= 1
            if start < end:
                arr[start], arr[end] = arr[end], arr[start]
                if verbose == 2:
                    print("Swapping:", start, end, "::", arr)
        arr[left], arr[end] = arr[end], arr[left]
        return end
    def quick_sort_recursion(left, right):
        if left < right:
            pivot_index = partition(left, right)
            if verbose:
                print("Iteration:", pivot_index, left, right, "::", arr)
            quick_sort_recursion(left, pivot_index - 1)
            quick_sort_recursion(pivot_index + 1, right)
    quick_sort_recursion(0, len(arr) - 1)
    if desc:
        arr = arr[::-1]
    return arr