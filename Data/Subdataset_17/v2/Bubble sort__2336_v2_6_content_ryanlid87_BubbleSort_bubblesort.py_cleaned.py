def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        print('Left:', left, 'Right:', right)
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
        print('Merged:', arr)
if __name__ == "__main__":
    array1 = [64, 34, 25, 12, 22, 11, 90]
    print("Original array for bubble sort:", array1)
    sorted_array1 = bubble_sort(array1[:])
    print("Sorted array with bubble sort:", sorted_array1)
    array2 = [64, 34, 25, 12, 22, 11, 90]
    print("Original array for merge sort:", array2)
    merge_sort(array2)
    print("Sorted array with merge sort:", array2)