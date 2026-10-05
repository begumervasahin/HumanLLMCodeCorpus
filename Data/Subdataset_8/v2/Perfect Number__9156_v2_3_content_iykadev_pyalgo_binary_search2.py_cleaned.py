def binary_search(arr, target, low=0, high=-1):
    if not arr:
        return -1
    if high == -1:
        high = len(arr) - 1
    if low == high:
        if arr[low] == target:
            return low
        else:
            return -1
    mid = (low + high)
    if arr[mid] > target:
        return binary_search(arr, target, low, mid - 1)
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, high)
    else:
        return mid
test_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(binary_search(test_list, 13))
print(binary_search(test_list, 8))
