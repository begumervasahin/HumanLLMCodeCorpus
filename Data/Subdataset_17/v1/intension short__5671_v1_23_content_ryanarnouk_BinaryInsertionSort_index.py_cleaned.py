def binary_search(arr, val, start, end):
    if start == end:
        return start if arr[start] > val else start + 1
    if start > end:
        return start
    mid = (start + end)
    if arr[mid] < val:
        return binary_search(arr, val, mid + 1, end)
    elif arr[mid] > val:
        return binary_search(arr, val, start, mid - 1)
    else:
        return mid
def insertion_sort(arr):
    for i in range(1, len(arr)):
        val = arr[i]
        j = binary_search(arr, val, 0, i - 1)
        arr = arr[:j] + [val] + arr[j:i] + arr[i+1:]
    return arr
if __name__ == "__main__":
    arr = [37, 23, 0, 17, 12, 72, 31, 46, 100, 88, 54]
    sorted_arr = insertion_sort(arr)
    print("Sorted array:", sorted_arr)