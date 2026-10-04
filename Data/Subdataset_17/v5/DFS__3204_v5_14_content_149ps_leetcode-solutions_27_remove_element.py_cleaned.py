def remove_element(nums, val):
    while val in nums:
        nums.remove(val)
        print(f"Current list after removing {val}: {nums}")
    return nums
nums = [3, 2, 2, 3]
result = remove_element(nums, 2)
print(f"Final list after removing 2: {result}")
nums = [1, 2, 3, 4, 2, 2, 5]
result = remove_element(nums, 2)
print(f"Final list after removing 2: {result}")
nums = [4, 4, 4, 4]
result = remove_element(nums, 4)
print(f"Final list after removing 4: {result}")
nums = [1, 2, 3, 4, 5]
result = remove_element(nums, 6)
print(f"Final list after removing 6: {result}")
