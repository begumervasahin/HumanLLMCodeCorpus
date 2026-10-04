class class1:
    def fonk1(self, b2, b1 = False):
        self.b2 = b2
        self.b1 = b1
    def fonk2(self):
        b3 = len(self.b2)
        for start_idx in range(b3):
            b4 = start_idx
            for i in range(start_idx + 1, b3):
                if self.b2[i] < self.b2[b4]:
                    b4 = i
            self.fonk3(start_idx, b4)
            if self.b1:
                self.fonk4(start_idx, b4)
        return self.b2
    def fonk3(self, i, j):
        self.b2[i], self.b2[j] = self.b2[j], self.b2[i]
    def fonk4(self, i, j):
        b5 = [f"{elm}*" if idx == i or idx == j else str(elm) for idx, elm in enumerate(self.b2)]
        b6 = '| ' + ' | '.join(b5) + ' |'
        print(b6)
        input("Press Enter to continue...")
if b7 = = "__main__":
    b2 = [64, 25, 12, 22, 11]
    b8 = class1(b2, b1=True)
    b9 = b8.fonk2()
    print("Sorted list:", b9)