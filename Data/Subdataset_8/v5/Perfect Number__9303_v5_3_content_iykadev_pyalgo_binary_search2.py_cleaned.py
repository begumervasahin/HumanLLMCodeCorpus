def binary_search(sorted_list, target, low=0, high=None):
    if not sorted_list:
        return -1
    if high is None:
        high = len(sorted_list) - 1
    if low > high:
        return -1
    mid = (low + high)
    if sorted_list[mid] == target:
        return mid
    elif sorted_list[mid] > target:
        return binary_search(sorted_list, target, low, mid - 1)
    else:
        return binary_search(sorted_list, target, mid + 1, high)
sorted_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target_value = 13
print(binary_search(sorted_list, target_value))