def missing_number(nums):
    lower_bound = 0
    upper_bound = max(nums)
    expected_length = upper_bound - lower_bound + 1
    print(f"Lower bound: {lower_bound}, Upper bound: {upper_bound}, Expected length: {expected_length}")
    index = 0
    while expected_length != 0:
        current_number = lower_bound + index
        if current_number in nums:
            index += 1
            expected_length -= 1
        else:
            return current_number
    return lower_bound + index
nums = [0]
print(f"Missing number: {missing_number(nums)}")
nums = [3, 0, 1]
print(f"Missing number: {missing_number(nums)}")
nums = [0, 1]
print(f"Missing number: {missing_number(nums)}")
nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
print(f"Missing number: {missing_number(nums)}")
