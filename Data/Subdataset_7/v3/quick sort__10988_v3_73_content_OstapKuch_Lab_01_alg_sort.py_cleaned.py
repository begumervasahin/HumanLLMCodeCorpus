class class1:
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
class class2:
    def fonk2(self):
        self.a1 = 0
        self.a2 = 0
    def fonk3(self, arr):
        self.fonk6()
        b3 = True
        while b3:
            b3 = False
            for i in range(len(arr) - 1):
                self.a1 += 1
                if arr[i].b1 < arr[i + 1].b1:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    self.a2 += 1
                    b3 = True
        print("Bubble Sort:\nComparison times:", self.a1, "\nSwap times:", self.a2)
    def fonk4(self, b6, start, end, arr):
        b4 = arr[b6].b2
        arr[b6], arr[end - 1] = arr[end - 1], arr[b6]
        b5 = start
        for right_ptr in range(start, end - 1):
            self.a1 += 1
            if arr[right_ptr].b2 < b4:
                arr[b5], arr[right_ptr] = arr[right_ptr], arr[b5]
                self.a2 += 1
                b5 += 1
        arr[b5], arr[end - 1] = arr[end - 1], arr[b5]
        self.a2 += 1
        return b5
    def fonk5(self, start, end, arr):
        if start < end:
            b6 = (start + end)
            b7 = self.fonk4(b6, start, end, arr)
            self.fonk5(start, b7, arr)
            self.fonk5(b7 + 1, end, arr)
    def fonk6(self):
        self.a1 = 0
        self.a2 = 0
if b8 = = "__main__":
    b9 = class2()
    b10 = [
        class1(80, 170),
        class1(75, 165),
        class1(85, 175),
        class1(70, 160),
        class1(90, 180)
    ]
    print("Bubble Sort:")
    b9.fonk3(b10[:])
    print()
    print("Quick Sort:")
    b9.fonk5(0, len(b10), b10)
    print("Comparison times:", b9.a1)
    print("Swap times:", b9.a2)