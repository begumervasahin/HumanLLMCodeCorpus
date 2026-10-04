import insertionsort as ins
class class1:
    def fonk1(self):
        pass
    def fonk2(self, array, b7, b6):
        def fonk3(b7, length):
            return b7 + (length
        def fonk4(b4, j, k):
            return j if b4 < j < k or k < j < b4 else k if j < k < b4 or b4 < k < j else b4
        b1 = fonk3(b7, b6 - b7)
        start_value, end_value, b2 = array[b7], array[b6 - 1], array[b1]
        return fonk4(start_value, end_value, b2)
    def fonk5(self, array, b7, b6, b9):
        b1 = self.fonk2(array, b7, b6) if b9 else b7
        b3 = array[b1]
        array[b1], array[b7] = array[b7], array[b1]
        b4 = b7 + 1
        for j in range(b7 + 1, b6):
            if array[j] < b3:
                array[j], array[b4] = array[b4], array[j]
                b4 += 1
        array[b7], array[b4 - 1] = array[b4 - 1], array[b7]
        return b4 - 1
    def fonk6(self, b12, b9):
        b5 = [0, len(b12)]
        while b5:
            b6 = b5.pop()
            b7 = b5.pop()
            if b6 - b7 < 2:
                continue
            b8 = self.fonk5(b12, b7, b6, b9)
            b5.extend([b8 + 1, b6, b7, b8])
    def fonk7(self, b12):
        if len(b12) <= 1:
            return b12
        self.fonk6(b12, b9 = False)
        return b12
    def fonk8(self, b12):
        if len(b12) <= 1:
            return b12
        self.fonk6(b12, b9 = True)
        return b12
    def fonk9(self, b12):
        if len(b12) > 16:
            return self.fonk8(b12)
        return ins.InsertionSort().fonk6(b12)
if b10 = = "__main__":
    b11 = class1()
    b12 = [3, 6, 8, 10, 1, 2, 1]
    print("Original array:", b12)
    print("Sorted array (class1):", b11.fonk7(b12[:]))
    print("Sorted array (Median of Three):", b11.fonk8(b12[:]))
    print("Optimized Sorted array:", b11.fonk9(b12[:]))