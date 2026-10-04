from typing import List
import collections
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count_nums2 = collections.Counter(nums2)
        result = []
        for num in nums1:
            if count_nums2[num] > 0:
                result.append(num)
                count_nums2[num] -= 1
        return result
solution = Solution()
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(f"Intersection of {nums1} and {nums2}: {solution.intersect(nums1, nums2)}")
nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
print(f"Intersection of {nums1} and {nums2}: {solution.intersect(nums1, nums2)}")
