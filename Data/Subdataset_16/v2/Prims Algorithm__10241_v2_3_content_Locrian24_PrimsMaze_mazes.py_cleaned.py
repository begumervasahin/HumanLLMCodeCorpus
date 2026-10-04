import random
class class1:
    class class2:
        def fonk1(self, b14, b6):
            self.b1 = b14
            self.b2 = b6
            self.b3 = True
            self.b4 = False
        def fonk2(self, b18):
            b5 = []
            b14, b6 = self.b1, self.b2
            if b14 > 0:
                b5.append([b14 - 1, b6])
            else:
                b5.append(None)
            if b14 + 1 < b18:
                b5.append([b14 + 1, b6])
            else:
                b5.append(None)
            if b6 > 0:
                b5.append([b14, b6 - 1])
            else:
                b5.append(None)
            if b6 + 1 < b18:
                b5.append([b14, b6 + 1])
            else:
                b5.append(None)
            return b5
        def fonk3(self, b18, b13):
            b7 = []
            for neighbour in self.fonk2(b18):
                if neighbour is None:
                    continue
                b8 = b13[neighbour[0] + neighbour[1] * b18]
                if b8.b3:
                    b7.append(b8)
            return b7
        def fonk4(self, b13, b18):
            b10, b9 = -1, -1
            for neighbour in self.fonk2(b18):
                if neighbour is None:
                    continue
                b8 = b13[neighbour[0] + neighbour[1] * b18]
                if b8.b4:
                    b10, b9 = neighbour
                    break
            if b10 = = -1:
                print("No valid b5. SOMETHING IS WRONG?")
                return None
            nx, b11 = 2 * self.b1 - b10, 2 * self.b2 - b9
            if nx < 0 or b11 < 0 or nx >= b18 or b11 >= b18:
                return None
            b12 = b13[nx + b11 * b18]
            if not b12.b4:
                return b12
            else:
                return None
    def fonk5(self, b18):
        self.b13 = [class1.class2(j, i) for i in range(b18) for j in range(b18)]
        b14 = random.randrange(1, b18, 2)
        b6 = random.randrange(1, b18, 2)
        b15 = self.b13[b14 + b6 * b18]
        b16 = b15.fonk3(b18, self.b13)
        b15.b4 = True
        b15.b3 = False
        while b16:
            b17 = random.choice(b16)
            b8 = b17.fonk4(self.b13, b18)
            if b8:
                b17.b3 = False
                b8.b4 = True
                b16.extend(b8.fonk3(b18, self.b13))
                b16 = list(set(b16))
            b16.remove(b17)
    def fonk6(self):
        b18 = int(len(self.b13) ** 0.5)
        b19 = [['
        for b8 in self.b13:
            if not b8.b3:
                b19[b8.b2][b8.b1] = ' '
        for row in b19:
            print(''.join(row))
b18 = 15
b19 = class1(b18)
b19.fonk6()