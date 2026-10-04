from typing import List
import collections
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        hmap2 = dict(collections.Counter(nums2))
        for num in nums1:
            if hmap2.get(num):
                res.append(num)
                hmap2[num] -= 1
        return res
solution = Solution()
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(solution.intersect(nums1, nums2))
nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
print(solution.intersect(nums1, nums2))
