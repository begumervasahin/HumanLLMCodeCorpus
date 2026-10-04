def remove_element(nums,val):
    while val in nums:
        nums.remove(val)
        print(nums)
    return nums
nums=[3,2,2,3]
print(remove_element(nums,2))