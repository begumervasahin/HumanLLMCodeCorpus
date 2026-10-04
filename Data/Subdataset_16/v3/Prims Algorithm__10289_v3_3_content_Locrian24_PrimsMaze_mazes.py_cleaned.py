import random
class class1:
    class class2:
        def fonk1(self, b1, b2):
            self.b1 = b1
            self.b2 = b2
            self.b3 = True
            self.b4 = False
        def fonk2(self, b13):
            b5 = []
            b6 = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dx, dy in b6:
                nx, b7 = self.b1 + dx, self.b2 + dy
                if 0 <= nx < b13 and 0 <= b7 < b13:
                    b5.append((nx, b7))
                else:
                    b5.append(None)
            return b5
        def fonk3(self, b13, b14):
            b8 = []
            for neighbour in self.fonk2(b13):
                if neighbour is None:
                    continue
                b9 = b14[neighbour[0] + neighbour[1] * b13]
                if b9.b3:
                    b8.append(b9)
            return b8
        def fonk4(self, b14, b13):
            for neighbour in self.fonk2(b13):
                if neighbour is None:
                    continue
                b9 = b14[neighbour[0] + neighbour[1] * b13]
                if b9.b4:
                    cx, b10 = neighbour
                    break
            else:
                print("No valid b5. SOMETHING IS WRONG?")
                return None
            ox, b11 = 2 * self.b1 - cx, 2 * self.b2 - b10
            if 0 <= ox < b13 and 0 <= b11 < b13:
                b12 = b14[ox + b11 * b13]
                if not b12.b4:
                    return b12
            return None
    def fonk5(self, b13):
        self.b13 = b13
        self.b14 = [class1.class2(j, i) for i in range(b13) for j in range(b13)]
        b15 = random.randrange(1, b13, 2)
        b16 = random.randrange(1, b13, 2)
        b17 = self.b14[b15 + b16 * b13]
        b18 = b17.fonk3(b13, self.b14)
        b17.b4 = True
        b17.b3 = False
        while b18:
            b19 = random.choice(b18)
            b12 = b19.fonk4(self.b14, b13)
            if b12:
                b19.b3 = False
                b12.b4 = True
                b18.extend(b12.fonk3(b13, self.b14))
                b18 = list(set(b18))
            b18.remove(b19)
    def fonk6(self):
        b20 = [['
        for b9 in self.b14:
            if not b9.b3:
                b20[b9.b2][b9.b1] = ' '
        for row in b20:
            print(''.join(row))
b13 = 15
b20 = class1(b13)
b20.fonk6()