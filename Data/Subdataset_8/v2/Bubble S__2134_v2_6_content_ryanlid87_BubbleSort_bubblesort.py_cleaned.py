
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr
arr1 = [64, 34, 25, 12, 22, 11, 90]
arr2 = [64, 34, 25, 12, 22, 11, 90]
print("Original array:")
print(arr1)
print("\nBubble sorted array:")
print(bubble_sort(arr1))
print("\nOriginal array:")
print(arr2)
print("\nMerge sorted array:")
print(merge_sort(arr2))