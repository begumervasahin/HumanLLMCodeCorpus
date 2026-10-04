from typing import List
import collections
class class1:
    def fonk1(self, b4: List[int], b5: List[int]) -> List[int]:
        b1 = []
        b2 = dict(collections.Counter(b5))
        for num in b4:
            if b2.get(num):
                b1.append(num)
                b2[num] -= 1
        return b1
b3 = class1()
b4 = [1, 2, 2, 1]
b5 = [2, 2]
print(b3.fonk1(b4, b5))
b4 = [4, 9, 5]
b5 = [9, 4, 9, 8, 4]
print(b3.fonk1(b4, b5))
