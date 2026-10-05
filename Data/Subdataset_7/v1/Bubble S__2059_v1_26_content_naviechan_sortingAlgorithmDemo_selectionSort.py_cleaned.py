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
            for i, b8 in enumerate(b1[a1:], b5 = a1):
                if b8 < b3:
                    b3 = b8
                    b4 = i
            b1[a1], b1[b4] = b1[b4], b1[a1]
            if self.b2:
                self.fonk3(b1, a1, b4)
            a1 += 1
        return b1
    def fonk3(self, b1, i, j):
        b1 = [str(b7) for b7 in b1]
        b6 = '|'
        for b7, b8 in enumerate(b1):
            if b7 = = i or b7 == j:
                b8 = b8 + '*'
            b6 = b6 + ' ' + b8 + ' |'
        print(b6)
        input("Press Enter to continue...")
def fonk4():
    b9 = [25, 66, 1, 4, 77, 55, 13, 5, 3]
    b2 = True
    b10 = class1(b9, b2)
    b11 = b10.fonk2()
    print("Sorted list:", b11)
if b12 = = "__main__":
    fonk4()