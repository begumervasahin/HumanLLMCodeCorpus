def plus_one(nums):
    number = int(''.join(str(x) for x in nums))
    number += 1
    result = [int(digit) for digit in str(number)]
    return result
nums = [1, 2, 4, 5, 3, 2, 2, 9]
print(plus_one(nums))
nums = [9, 9, 9]
print(plus_one(nums))
nums = [0]
print(plus_one(nums))
nums = [1, 0, 0, 0]
print(plus_one(nums))
