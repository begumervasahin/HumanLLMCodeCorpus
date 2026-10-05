def selection_sort(nums):
    for i in range(len(nums)):
        min_pos = i
        for j in range(i, len(nums)):
            if nums[j] < nums[min_pos]:
                min_pos = j
        nums[i], nums[min_pos] = nums[min_pos], nums[i]
        print(nums)
nums = [5, 3, 7, 2, 4, 1, 11, 8, 10, 9, 6]
selection_sort(nums)
print(nums)