def selection_sort(nums):
    n = len(nums)
    for i in range(n - 1):
        minpos = i
        for j in range(i + 1, n):
            if nums[j] < nums[minpos]:
                minpos = j
        nums[i], nums[minpos] = nums[minpos], nums[i]
        print(nums)
nums = [5, 3, 7, 2, 4, 1, 11, 8, 10, 9, 6]
selection_sort(nums)
print("Sorted list:", nums)