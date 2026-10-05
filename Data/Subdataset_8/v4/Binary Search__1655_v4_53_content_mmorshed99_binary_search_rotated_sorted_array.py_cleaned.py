class Solution:
    def search_rotated_array(self, nums, target):
        def find_pivot(start, end, nums):
            mid = start + (end - start)
            if len(nums) < 3:
                return start
            if nums[mid] < nums[mid - 1] and nums[mid] < nums[mid + 1]:
                return mid
            elif nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] > nums[len(nums) - 1]:
                return find_pivot(mid, len(nums), nums)
            elif nums[mid] < nums[0]:
                return find_pivot(start, mid, nums)
            else:
                return -1
        def binary_search(start, end, target, nums):
            mid = start + (end - start)
            if target == nums[mid]:
                return mid
            if end - start < 3:
                if target == nums[start]:
                    return start
                elif target == nums[end]:
                    return end
                else:
                    return -1
            elif target > nums[mid]:
                return binary_search(mid, end, target, nums)
            else:
                return binary_search(start, mid, target, nums)
        pivot_index = find_pivot(0, len(nums) - 1, nums)
        if pivot_index == -1:
            return binary_search(0, len(nums) - 1, target, nums)
        else:
            index_left_half = binary_search(0, pivot_index - 1, target, nums)
            if index_left_half != -1:
                return index_left_half
            else:
                return binary_search(pivot_index, len(nums) - 1, target, nums)
solution = Solution()
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
result = solution.search_rotated_array(nums, target)
print("Index of target in rotated array:", result)