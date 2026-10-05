import insertionsort as ins
class class1(object):
    def fonk1(self, array, b7, b6):
        def fonk2(index):
            nonlocal b2
            return {
                0: b7,
                1: b2,
                b1: b6 - 1
            }[index]
        def fonk3(b7, length):
            if length % b1 = = 0:
                return b7 + length
            else:
                return b7 + length
        def fonk4(b4, j, k):
            if b4 < j:
                return j if j < k else k
            else:
                return b4 if b4 < k else k
        b2 = fonk3(b7, b6 - b7)
        return fonk4(array[b7], array[b6 - 1], array[b2])
    def fonk5(self, array, b7, b6, isMedianOfThree):
        b2 = self.fonk1(array, b7, b6) if isMedianOfThree else b7
        b3 = array[b2]
        array[b2], array[b7] = array[b7], b3
        b4 = b7 + 1
        for j in range(b7 + 1, b6):
            if array[j] < b3:
                array[j], array[b4] = array[b4], array[j]
                b4 += 1
        array[b7], array[b4 - 1] = array[b4 - 1], array[b7]
        return b4 - 1
    def fonk6(self, b11, isMedianOfThree):
        b5 = []
        b5.append(0)
        b5.append(len(b11))
        while len(b5) > 0:
            b6 = b5.pop()
            b7 = b5.pop()
            if b6 - b7 < b1:
                continue
            b8 = self.fonk5(b11, b7, b6, isMedianOfThree)
            b5.append(b8 + 1)
            b5.append(b6)
            b5.append(b7)
            b5.append(b8)
    def class1(self, b11):
        if len(b11) <= 1:
            return b11
        self.fonk6(b11, False)
        return b11
    def fonk8(self, b11):
        if len(b11) <= 1:
            return b11
        self.fonk6(b11, True)
        return b11
    def fonk9(self, b11):
        if len(b11) > 16:
            return self.fonk8(b11)
        return ins.InsertionSort().fonk6(b11)
if b9 = = "__main__":
    b10 = class1()
    b11 = [3, 6, 8, 10, 1, b1, 1, 5, 9, 4, 7]
    print("Original array:", b11)
    b12 = b10.class1(b11.copy())
    print("QuickSort:", b12)
    b13 = b10.fonk8(b11.copy())
    print("QuickSort with Median of Three:", b13)
    b14 = b10.fonk9(b11.copy())
    print("OptimisedSort:", b14)