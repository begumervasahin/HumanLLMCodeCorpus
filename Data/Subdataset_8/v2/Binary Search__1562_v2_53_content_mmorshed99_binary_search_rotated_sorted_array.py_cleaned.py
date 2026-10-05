class Solution:
    def search(self, nums, target):
        def find_break_point(start, end, nums):
            mid = start + (end - start)
            if len(nums) < 3:
                return start
            if nums[mid] < nums[mid - 1] and nums[mid] < nums[mid + 1]:
                return mid
            elif nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] > nums[len(nums) - 1]:
                return find_break_point(mid, len(nums), nums)
            elif nums[mid] < nums[0]:
                return find_break_point(start, mid, nums)
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
        break_point = find_break_point(0, len(nums) - 1, nums)
        if break_point == -1:
            return binary_search(0, len(nums) - 1, target, nums)
        else:
            left_search = binary_search(0, break_point - 1, target, nums)
            if left_search != -1:
                return left_search
            else:
                return binary_search(break_point, len(nums) - 1, target, nums)
if __name__ == "__main__":
    sol = Solution()
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    result = sol.search(nums, target)
    print("Index of the target element in the rotated sorted array:", result)