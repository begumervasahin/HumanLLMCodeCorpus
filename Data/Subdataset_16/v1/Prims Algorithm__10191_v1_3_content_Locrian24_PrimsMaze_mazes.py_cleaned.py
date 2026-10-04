import random
class class1:
    class class2:
        def fonk1(self, b6, b7):
            self.b1 = b6
            self.b2 = b7
            self.b3 = True
            self.b4 = False
        def fonk2(self, b19):
            b5 = []
            b6 = self.b1
            b7 = self.b2
            if b6 > 0:
                b5.append([b6 - 1, b7])
            else:
                b5.append(None)
            if b6 + 1 < b19:
                b5.append([b6 + 1, b7])
            else:
                b5.append(None)
            if b7 > 0:
                b5.append([b6, b7 - 1])
            else:
                b5.append(None)
            if b7 + 1 < b19:
                b5.append([b6, b7 + 1])
            else:
                b5.append(None)
            return b5
        def fonk3(self, b19, b15):
            b8 = []
            for b5 in self.fonk2(b19):
                if b5 is None:
                    continue
                b9 = b15[b5[0] + b5[1] * b19]
                if b9.b3:
                    b8.append(b9)
            return b8
        def fonk4(self, b15, b19):
            b11, b10 = -1, -1
            for b5 in self.fonk2(b19):
                if b5 is None:
                    continue
                b9 = b15[b5[0] + b5[1] * b19]
                if b9.b4:
                    b11 = b5[0]
                    b10 = b5[1]
                    break
            if b11 = = -1:
                print("No valid neighbours. SOMETHING IS WRONG?")
                return None
            b12 = 2 * self.b1 - b11
            b13 = 2 * self.b2 - b10
            if b12 < 0 or b13 < 0 or b12 >= b19 or b13 >= b19:
                return None
            b14 = b15[b12 + b13 * b19]
            if not b14.b4:
                return b14
            else:
                return None
    def fonk5(self, b19):
        self.b15 = []
        for i in range(0, b19):
            for j in range(0, b19):
                self.b15.append(class1.class2(j, i))
        b6 = random.randrange(1, b19, 2)
        b7 = random.randrange(1, b19, 2)
        b16 = self.b15[b6 + b7 * b19]
        b17 = b16.fonk3(b19, self.b15)
        b16.b4 = True
        b16.b3 = False
        b9 = None
        while len(b17) != 0:
            b18 = b17[random.randint(0, len(b17) - 1)]
            b9 = b18.fonk4(self.b15, b19)
            if b9:
                b18.b3 = False
                b9.b4 = True
                b17.extend(b9.fonk3(b19, self.b15))
                b17 = list(set(b17))
            b17.remove(b18)
    def fonk6(self):
        b19 = int(len(self.b15) ** 0.5)
        b20 = [['
        for b9 in self.b15:
            if not b9.b3:
                b20[b9.b2][b9.b1] = ' '
        for row in b20:
            print(''.join(row))
b19 = 15
b20 = class1(b19)
b20.fonk6()