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
            b5 = arr[len(arr) - 1]
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
if b7 = = "__main__":
    b8 = class1()
    b9 = [34, 7, 23, 32, 5, 62, 32, 7]
    for b6 in b9:
        b8.fonk2(b6)
    print("Original list:")
    b8.fonk4()
    b10 = b8.fonk5(b8.fonk3())
    print("\nSorted list:")
    for b6 in b10:
        print(b6)