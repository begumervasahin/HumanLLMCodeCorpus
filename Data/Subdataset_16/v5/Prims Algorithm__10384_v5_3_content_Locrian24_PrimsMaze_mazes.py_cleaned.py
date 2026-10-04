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
                if neighbour is not None:
                    b9 = b14[neighbour[0] + neighbour[1] * b13]
                    if b9.b3:
                        b8.append(b9)
            return b8
        def fonk4(self, b14, b13):
            b11, b10 = -1, -1
            for neighbour in self.fonk2(b13):
                if neighbour is not None:
                    b9 = b14[neighbour[0] + neighbour[1] * b13]
                    if b9.b4:
                        b11, b10 = neighbour
                        break
            if b11 = = -1:
                print("No valid b5. SOMETHING IS WRONG?")
                return None
            nx, b7 = 2 * self.b1 - b11, 2 * self.b2 - b10
            if 0 <= nx < b13 and 0 <= b7 < b13:
                b12 = b14[nx + b7 * b13]
                if not b12.b4:
                    return b12
            return None
    def fonk5(self, b13):
        self.b13 = b13
        self.b14 = [class1.class2(b1, b2) for b2 in range(b13) for b1 in range(b13)]
        self.fonk6()
    def fonk6(self):
        b15 = self.fonk7()
        b16 = b15.fonk3(self.b13, self.b14)
        b15.b4 = True
        b15.b3 = False
        while b16:
            b17 = random.choice(b16)
            b9 = b17.fonk4(self.b14, self.b13)
            if b9:
                b17.b3 = False
                b9.b4 = True
                b16.extend(b9.fonk3(self.b13, self.b14))
                b16 = list(set(b16))
            b16.remove(b17)
    def fonk7(self):
        b18 = random.randrange(1, self.b13, 2)
        b19 = random.randrange(1, self.b13, 2)
        return self.b14[b18 + b19 * self.b13]