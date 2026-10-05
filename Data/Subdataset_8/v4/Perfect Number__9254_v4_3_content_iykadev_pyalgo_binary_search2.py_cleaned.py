def binary_search(sorted_list, target, low=0, high=-1):
    if not sorted_list:
        return -1
    if high == -1:
        high = len(sorted_list) - 1
    if low == high:
        if sorted_list[low] == target:
            return low
        else:
            return -1
    mid = (low + high)
    if sorted_list[mid] > target:
        return binary_search(sorted_list, target, low, mid - 1)
    elif sorted_list[mid] < target:
        return binary_search(sorted_list, target, mid + 1, high)
    else:
        return mid
sorted_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target_value = 13
print(binary_search(sorted_list, target_value))