def remove_element(nums, val):
    while val in nums:
        nums.remove(val)
        print(f"Current list after removing {val}: {nums}")
    return nums
nums = [3, 2, 2, 3]
print(f"After removing 2: {remove_element(nums, 2)}")
nums = [1, 2, 3, 4, 2, 2, 5]
print(f"After removing 2: {remove_element(nums, 2)}")
nums = [4, 4, 4, 4]
print(f"After removing 4: {remove_element(nums, 4)}")
nums = [1, 2, 3, 4, 5]
print(f"After removing 6: {remove_element(nums, 6)}")
