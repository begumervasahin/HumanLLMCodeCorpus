def quick_sort(arr, verbose=0, desc=0):
    def partition(left, right):
        pivot = arr[left]
        low = left + 1
        high = right
        done = False
        while not done:
            while low <= high and arr[low] <= pivot:
                low += 1
            while arr[high] >= pivot and high >= low:
                high -= 1
            if high < low:
                done = True
            else:
                arr[low], arr[high] = arr[high], arr[low]
        arr[left], arr[high] = arr[high], arr[left]
        return high
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