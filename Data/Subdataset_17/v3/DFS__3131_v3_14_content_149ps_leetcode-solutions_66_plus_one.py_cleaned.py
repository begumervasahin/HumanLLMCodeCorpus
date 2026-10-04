def plus_one(nums):
    number_str = ''.join(map(str, nums))
    number = int(number_str)
    incremented_number = number + 1
    result = [int(digit) for digit in str(incremented_number)]
    return result
nums = [1, 2, 4, 5, 3, 2, 2, 9]
print(plus_one(nums))
nums = [9, 9, 9]
print(plus_one(nums))
nums = [0]
print(plus_one(nums))
nums = [1, 0, 0, 0]
print(plus_one(nums))
