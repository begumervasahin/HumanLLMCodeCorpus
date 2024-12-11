class class1:
    def fonk1(self, b2, b1 = False):
        self.b2 = b2
        self.b1 = b1
    def fonk2(self):
        b3 = False
        b2 = self.b2
        while not b3:
            b3 = True
            for i in range(len(b2) - 1):
                b4 = i + 1
                if b2[i] > b2[b4]:
                    b2[i], b2[b4] = b2[b4], b2[i]
                    b3 = False
                if self.b1:
                    self.fonk3(b2, i, b4)
        return b2
    @staticmethod
    def fonk3(b2, i, b4):
        b5 = [f"{elm}*" if k in (i, b4) else elm for k, elm in enumerate(b2)]
        b6 = ' | '.join(map(str, b5))
        print(b6)
        input("Press Enter to continue...")
def fonk4():
    b7 = [64, 25, 12, 22, 11]
    b1 = True
    b8 = class1(b7, b1)
    b9 = b8.fonk2()
    print("Sorted array:", b9)
if b10 = = "__main__":
    fonk4()