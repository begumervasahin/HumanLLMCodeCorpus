def binary_search(arr, target, low=0, high=None):
    if not arr:
        return -1
    if high is None:
        high = len(arr) - 1
    while low <= high:
        mid = (low + high)
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
test_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(binary_search(test_list, 13))
print(binary_search(test_list, 8))
