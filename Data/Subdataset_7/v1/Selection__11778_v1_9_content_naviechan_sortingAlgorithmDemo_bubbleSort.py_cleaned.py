class class1:
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
    def fonk2(self):
        b3 = False
        b1 = self.b1
        while not b3:
            b3 = True
            for i in range(len(b1) - 1):
                b4 = i + 1
                if b1[i] > b1[b4]:
                    b1[i], b1[b4] = b1[b4], b1[i]
                    b3 = False
                if self.b2:
                    self.fonk3(b1, i, b4)
        return b1
    def fonk3(self, b1, i, b4):
        b1 = [str(b6) for b6 in b1]
        b5 = '|'
        for b6, b7 in enumerate(b1):
            if b6 = = i or b6 == b4:
                b7 = b7 + '*'
            b5 = b5 + ' ' + str(b7) + ' |'
        print(b5)
        input("Press Enter to continue...")
def fonk4():
    b1 = [64, 25, 12, 22, 11]
    b2 = True
    b8 = class1(b1, b2)
    b9 = b8.fonk2()
    print("Sorted array:", b9)
if b10 = = "__main__":
    fonk4()