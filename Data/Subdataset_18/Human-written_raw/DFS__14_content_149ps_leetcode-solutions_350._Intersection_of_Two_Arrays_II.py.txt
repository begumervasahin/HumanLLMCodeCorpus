class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        hmap2 = dict(collections.Counter(nums2))
        for num in nums1:
            if hmap2.get(num):
                res.append(num)
                hmap2[num] -=1
        return res
