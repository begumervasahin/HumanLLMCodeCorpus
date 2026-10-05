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
        b5 = [str(b7) for b7 in b1]
        b6 = '|'
        for b7, b8 in enumerate(b5):
            if b7 = = i or b7 == b4:
                b8 = b8 + '*'
            b6 = b6 + ' ' + str(b8) + ' |'
        print(b6)
        input("Press Enter to continue...")