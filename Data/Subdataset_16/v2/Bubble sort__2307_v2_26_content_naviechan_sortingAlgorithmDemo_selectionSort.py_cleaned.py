class class1:
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
    def fonk2(self):
        a1 = 0
        b1 = self.b1
        while a1 < len(b1):
            b3 = b1[a1]
            b4 = a1
            for i, elm in enumerate(b1[a1:]):
                if elm < b3:
                    b3 = elm
                    b4 = i + a1
            b1[a1], b1[b4] = b1[b4], b1[a1]
            if self.b2:
                self.fonk3(b1, a1, b4)
            a1 += 1
        return b1
    def fonk3(self, b1, i, j):
        b1 = [str(b6) for b6 in b1]
        b5 = '|'
        for b6, elm in enumerate(b1):
            if b6 = = i or b6 == j:
                elm += '*'
            b5 += f' {elm} |'
        print(b5)
        input("Press Enter to continue...")
def fonk4():
    b2 = True
    b1 = [64, 25, 12, 22, 11]
    b7 = class1(b1, b2)
    b8 = b7.fonk2()
    print('Sorted List:', b8)
if b9 = = "__main__":
    fonk4()