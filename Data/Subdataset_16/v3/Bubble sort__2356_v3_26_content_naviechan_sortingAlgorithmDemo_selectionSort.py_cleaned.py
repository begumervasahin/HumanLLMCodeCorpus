class class1:
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
    def fonk2(self):
        b1 = self.b1
        for start_idx in range(len(b1)):
            b3 = start_idx
            for i in range(start_idx + 1, len(b1)):
                if b1[i] < b1[b3]:
                    b3 = i
            b1[start_idx], b1[b3] = b1[b3], b1[start_idx]
            if self.b2:
                self.fonk3(b1, start_idx, b3)
        return b1
    def fonk3(self, b1, i, j):
        b4 = '|'
        for k, elm in enumerate(b1):
            b5 = '*' if k == i or k == j else ''
            b4 += f' {elm}{b5} |'
        print(b4)
        input("Press Enter to continue...")
def fonk4():
    b2 = True
    b1 = [64, 25, 12, 22, 11]
    b6 = class1(b1, b2)
    b7 = b6.fonk2()
    print('Sorted List:', b7)
if b8 = = "__main__":
    fonk4()