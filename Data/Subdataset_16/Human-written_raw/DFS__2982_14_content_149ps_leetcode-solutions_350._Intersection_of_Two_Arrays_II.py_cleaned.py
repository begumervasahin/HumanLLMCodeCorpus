class class1:
    def fonk1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        b1 = []
        b2 = dict(collections.Counter(nums2))
        for num in nums1:
            if b2.get(num):
                b1.append(num)
                b2[num] -=1
        return b1