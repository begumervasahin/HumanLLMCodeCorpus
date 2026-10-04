from typing import List
import collections
class class1:
    def fonk1(self, b4: List[int], b5: List[int]) -> List[int]:
        b1 = collections.Counter(b5)
        b2 = []
        for num in b4:
            if b1[num] > 0:
                b2.append(num)
                b1[num] -= 1
        return b2
b3 = class1()
b4 = [1, 2, 2, 1]
b5 = [2, 2]
print(f"Intersection of {b4} and {b5}: {b3.fonk1(b4, b5)}")
b4 = [4, 9, 5]
b5 = [9, 4, 9, 8, 4]
print(f"Intersection of {b4} and {b5}: {b3.fonk1(b4, b5)}")
