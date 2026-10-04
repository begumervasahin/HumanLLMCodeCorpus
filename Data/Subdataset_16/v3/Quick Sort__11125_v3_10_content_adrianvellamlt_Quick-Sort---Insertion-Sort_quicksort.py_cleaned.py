import insertionsort as ins
class class1:
    def fonk1(self, b9, b6, b5):
        def fonk2(index):
            return {0: b6, 1: b1, 2: b5 - 1}[index]
        def fonk3(b6, length):
            return b6 + length
        def fonk4(b3, j, k):
            return j if b3 < j < k or k < j < b3 else k if b3 < k < j or j < k < b3 else b3
        b1 = fonk3(b6, b5 - b6)
        return fonk4(fonk2(0), fonk2(1), fonk2(2))
    def fonk5(self, b9, b6, b5, is_median_of_three):
        b1 = self.fonk1(b9, b6, b5) if is_median_of_three else b6
        b2 = b9[b1]
        b9[b1], b9[b6] = b9[b6], b2
        b3 = b6 + 1
        for j in range(b6 + 1, b5):
            if b9[j] < b2:
                b9[j], b9[b3] = b9[b3], b9[j]
                b3 += 1
        b9[b6], b9[b3 - 1] = b9[b3 - 1], b9[b6]
        return b3 - 1
    def fonk6(self, arr, is_median_of_three):
        b4 = [0, len(arr)]
        while b4:
            b5 = b4.pop()
            b6 = b4.pop()
            if b5 - b6 < 2:
                continue
            b7 = self.fonk5(arr, b6, b5, is_median_of_three)
            b4.extend([b7 + 1, b5, b6, b7])
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
if b8 = = "__main__":
    b9 = [33, 10, 55, 71, 29, 14, 37, 93, 52, 65]
    b10 = class1()
    print("Quick Sort:", b10.fonk7(b9[:]))
    print("Quick Sort with Median of Three:", b10.fonk8(b9[:]))
    print("Optimised Sort:", b10.fonk9(b9[:]))