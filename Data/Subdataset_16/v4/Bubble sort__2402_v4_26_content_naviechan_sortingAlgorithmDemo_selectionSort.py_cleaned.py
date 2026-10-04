class class1:
    def fonk1(self, b2, b1 = False):
        self.b2 = b2
        self.b1 = b1
    def fonk2(self):
        for start_idx in range(len(self.b2)):
            b3 = start_idx
            for i in range(start_idx + 1, len(self.b2)):
                if self.b2[i] < self.b2[b3]:
                    b3 = i
            self.b2[start_idx], self.b2[b3] = self.b2[b3], self.b2[start_idx]
            if self.b1:
                self.fonk3(start_idx, b3)
        return self.b2
    def fonk3(self, i, j):
        b4 = [f"{elm}*" if idx == i or idx == j else str(elm) for idx, elm in enumerate(self.b2)]
        b5 = '| ' + ' | '.join(b4) + ' |'
        print(b5)
        input("Press Enter to continue...")
if b6 = = "__main__":
    b2 = [64, 25, 12, 22, 11]
    b7 = class1(b2, b1=True)
    b8 = b7.fonk2()
    print("Sorted list:", b8)