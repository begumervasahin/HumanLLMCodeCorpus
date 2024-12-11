def quick_sort(arr, left, right):
    if left < right:
        pivot = arr[left]
        s = left
        for i in range(left + 1, right):
            if arr[i] < pivot:
                s += 1
                arr[s], arr[i] = arr[i], arr[s]
        arr[left], arr[s] = arr[s], arr[left]
        quick_sort(arr, left, s - 1)
        quick_sort(arr, s + 1, right)