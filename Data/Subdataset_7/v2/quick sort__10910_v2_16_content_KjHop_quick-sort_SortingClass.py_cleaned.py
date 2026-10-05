class class1:
    def fonk1(self):
        self.b1 = []
    def fonk2(self, b6):
        self.b1.append(b6)
    def fonk3(self):
        return self.b1
    def fonk4(self):
        for b6 in self.b1:
            print(b6)
    def fonk5(self, arr):
        b2 = []
        b3 = []
        b4 = []
        if len(arr) > 1:
            b5 = arr[-1]
            for b6 in arr:
                if b6 < b5:
                    b2.append(b6)
                elif b6 = = b5:
                    b3.append(b6)
                else:
                    b4.append(b6)
            return self.fonk5(b2) + b3 + self.fonk5(b4)
        else:
            return arr
b7 = class1()
b7.fonk2(3)
b7.fonk2(1)
b7.fonk2(5)
b7.fonk2(2)
b7.fonk2(4)
print("Original list:", b7.fonk3())
b8 = b7.fonk5(b7.fonk3())
print("Sorted list:", b8)