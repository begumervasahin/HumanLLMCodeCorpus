import insertionsort as ins
class class1:
    def fonk1(self, b10, b7, b6):
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
        return fonk4(b10[b7], b10[b6 - 1], b10[b2])
    def fonk5(self, b10, b7, b6, is_median_of_three):
        b2 = self.fonk1(b10, b7, b6) if is_median_of_three else b7
        b3 = b10[b2]
        b10[b2], b10[b7] = b10[b7], b3
        b4 = b7 + 1
        for j in range(b7 + 1, b6):
            if b10[j] < b3:
                b10[j], b10[b4] = b10[b4], b10[j]
                b4 += 1
        b10[b7], b10[b4 - 1] = b10[b4 - 1], b10[b7]
        return b4 - 1
    def fonk6(self, arr, is_median_of_three):
        b5 = []
        b5.append(0)
        b5.append(len(arr))
        while len(b5) > 0:
            b6 = b5.pop()
            b7 = b5.pop()
            if b6 - b7 < b1:
                continue
            b8 = self.fonk5(arr, b7, b6, is_median_of_three)
            b5.append(b8 + 1)
            b5.append(b6)
            b5.append(b7)
            b5.append(b8)
    def fonk7(self, arr):
        if len(arr) <= 1:
            return arr
        self.fonk6(arr, False)
        return arr
    def fonk8(self, arr):
        if len(arr) <= 1:
            return arr
        self.fonk6(arr, True)
        return arr
    def fonk9(self, arr):
        if len(arr) > 16:
            return self.fonk8(arr)
        return ins.InsertionSort().fonk6(arr)
if b9 = = "__main__":
    b10 = [33, 10, 55, 71, 29, 14, 37, 93, 52, 65]
    b11 = class1()
    print("Quick Sort:", b11.fonk7(b10[:]))
    print("Quick Sort with Median of Three:", b11.fonk8(b10[:]))
    print("Optimised Sort:", b11.fonk9(b10[:]))