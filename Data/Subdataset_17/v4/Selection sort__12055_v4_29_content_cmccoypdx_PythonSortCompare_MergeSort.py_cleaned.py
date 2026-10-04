def merge(arr, left, right):
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
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        merge(arr, left, right)
if __name__ == "__main__":
    sample_list = [38, 27, 43, 3, 9, 82, 10]
    print(f"Unsorted list: {sample_list}")
    merge_sort(sample_list)
    print(f"Sorted list: {sample_list}")