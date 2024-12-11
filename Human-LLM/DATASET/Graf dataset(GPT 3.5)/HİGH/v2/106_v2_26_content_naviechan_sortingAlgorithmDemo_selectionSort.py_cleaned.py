class class1:
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
    def fonk2(self):
        b1 = self.b1
        for start_idx in range(len(b1)):
            b3 = self.fonk3(start_idx)
            b1[start_idx], b1[b3] = b1[b3], b1[start_idx]
            if self.b2:
                self.fonk4(b1, start_idx, b3)
        return b1
    def fonk3(self, start_idx):
        b3 = start_idx
        for i in range(start_idx, len(self.b1)):
            if self.b1[i] < self.b1[b3]:
                b3 = i
        return b3
    def fonk4(self, b1, i, j):
        b4 = ['*' if k == i or k == j else '' for k in range(len(b1))]
        b5 = '| ' + ' | '.join(str(elm) + indicator for elm, indicator in zip(b1, b4)) + ' |'
        print(b5)
        input("Press Enter to continue...")
def fonk5():
    b6 = [25, 66, 1, 4, 77, 55, 13, 5, 3]
    b2 = True
    b7 = class1(b6, b2)
    b8 = b7.fonk2()
    print("Sorted list:", b8)
if b9 = = "__main__":
    fonk5()