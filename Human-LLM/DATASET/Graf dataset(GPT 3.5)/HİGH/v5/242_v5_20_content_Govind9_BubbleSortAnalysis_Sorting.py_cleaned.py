class class1:
    def fonk1(self):
        self.b1 = []
        self.b2 = []
        self.b3 = []
    def fonk2(self):
        b4 = sum(self.b1)
        b5 = sum(self.b2)
        b6 = sum(self.b3)
        print("Qsort\tBubble\tBetterBubble")
        for q, b, bb in zip(self.b1, self.b2, self.b3):
            print(f"{q}\t{b}\t{bb}")
        print(f"{b4}\t{b5}\t{b6}")
    def fonk3(self, x):
        b7 = []
        if len(x) == len(self.b10):
            b8 = "".join(self.b10[int(i)] for i in x)
            for i in b8:
                b7.append(int(i))
            self.fonk4(b7)
        for i in range(len(self.b10)):
            if str(i) not in x:
                self.fonk3(x + str(i))
    def fonk4(self, b7):
        self.b2.append(self.fonk5(b7))
        self.b1.append(self.fonk6(b7))
        self.b3.append(self.fonk7(b7))
        self.fonk2()
    @staticmethod
    def fonk5(b7):
        a1 = 0
        for j in range(len(b7)):
            a1 += 3
            for i in range(len(b7) - 1 - j):
                a1 += 2
                if b7[i] > b7[i + 1]:
                    a1 += 2
                    b7[i], b7[i + 1] = b7[i + 1], b7[i]
        return a1
    @staticmethod
    def fonk6(b7):
        a1 = 0
        for j in range(len(b7)):
            a1 += 3
            a2 = 0
            for i in range(len(b7) - 1 - j):
                a1 += 2
                if b7[i] > b7[i + 1]:
                    a1 += 2
                    a2 += 1
                    b7[i], b7[i + 1] = b7[i + 1], b7[i]
            if a2 < 2:
                break
        return a1
    @staticmethod
    def fonk7(b7):
        a1 = 0
        for j in range(len(b7)):
            a1 += 3
            b9 = False
            for i in range(len(b7) - 1 - j):
                a1 += 2
                if b7[i] > b7[i + 1]:
                    a1 += 2
                    b9 = True
                    b7[i], b7[i + 1] = b7[i + 1], b7[i]
            if not b9:
                break
        return a1
    def fonk8(self):
        self.b10 = '123456'
        self.fonk3("")
if b11 = = "__main__":
    b12 = class1()
    b12.fonk8()