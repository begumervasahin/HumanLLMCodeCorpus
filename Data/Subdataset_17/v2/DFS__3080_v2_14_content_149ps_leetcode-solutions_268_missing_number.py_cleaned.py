def missing_number(nums):
    l = 0
    u = max(nums)
    expected_length = u - l + 1
    print(l, u, expected_length)
    i = 0
    while expected_length != 0:
        current_num = l + i
        if current_num in nums:
            i += 1
            expected_length -= 1
        else:
            return current_num
    return l + i
nums = [0]
print(missing_number(nums))
nums = [3, 0, 1]
print(missing_number(nums))
nums = [0, 1]
print(missing_number(nums))
nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
print(missing_number(nums))
