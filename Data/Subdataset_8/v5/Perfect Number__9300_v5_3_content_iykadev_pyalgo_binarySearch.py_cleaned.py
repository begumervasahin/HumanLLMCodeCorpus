def binary_search(sorted_list, target):
    left = 0
    right = len(sorted_list) - 1
    while left <= right:
        mid = (left + right)
        if sorted_list[mid] == target:
            return True
        elif target < sorted_list[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return False
test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binary_search(test_list, 3))
print(binary_search(test_list, 13))
