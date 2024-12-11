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
        b2 = QuickSort.fonk1(self, array, b7, b6) if isMedianOfThree else b7
        b3 = array[b2]
        array[b2], array[b7] = array[b7], b3
        b4 = b7 + 1
        for j in range(b7 + 1, b6):
            if array[j] < b3:
                array[j], array[b4] = array[b4], array[j]
                b4 += 1
        array[b7], array[b4 - 1] = array[b4 - 1], array[b7]
        return b4 - 1
    def fonk6(self, arr, isMedianOfThree):
        b5 = []
        b5.append(0)
        b5.append(len(arr))
        while len(b5) > 0:
            b6 = b5.pop()
            b7 = b5.pop()
            if b6 - b7 < b1: continue
            b8 = QuickSort.fonk5(self, arr, b7, b6, isMedianOfThree)
            b5.append(b8 + 1)
            b5.append(b6)
            b5.append(b7)
            b5.append(b8)
    def class1(self, arr):
        if len(arr) <= 1:
            return arr
        QuickSort.fonk6(self, arr, False)
        return arr
    def fonk8(self, arr):
        if len(arr) <= 1:
            return arr
        QuickSort.fonk6(self, arr, True)
        return arr
    def fonk9(self, arr):
        if len(arr) > 16:
            return QuickSort.fonk8(self, arr)
        return ins.InsertionSort().fonk6(arr)