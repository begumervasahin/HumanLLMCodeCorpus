import random
class class1:
    class class2:
        def fonk1(self, b1, b2):
            self.b1 = b1
            self.b2 = b2
            self.b3 = True
            self.b4 = False
        def fonk2(self, size):
            b5 = []
            if self.b1 > 0:
                b5.append((self.b1 - 1, self.b2))
            else:
                b5.append(None)
            if self.b1 + 1 < size:
                b5.append((self.b1 + 1, self.b2))
            else:
                b5.append(None)
            if self.b2 > 0:
                b5.append((self.b1, self.b2 - 1))
            else:
                b5.append(None)
            if self.b2 + 1 < size:
                b5.append((self.b1, self.b2 + 1))
            else:
                b5.append(None)
            return b5
        def fonk3(self, size, b12):
            b6 = []
            for neighbour in self.fonk2(size):
                if neighbour is None:
                    continue
                b7 = b12[neighbour[0] + neighbour[1] * size]
                if b7.b3:
                    b6.append(b7)
            return b6
        def fonk4(self, b12, size):
            b9, b8 = -1, -1
            for neighbour in self.fonk2(size):
                if neighbour is None:
                    continue
                b7 = b12[neighbour[0] + neighbour[1] * size]
                if b7.b4:
                    b9, b8 = neighbour
                    break
            if b9 = = -1:
                print("No valid b5. SOMETHING IS WRONG?")
                return None
            nx, b10 = 2 * self.b1 - b9, 2 * self.b2 - b8
            if nx < 0 or b10 < 0 or nx >= size or b10 >= size:
                return None
            b11 = b12[nx + b10 * size]
            if not b11.b4:
                return b11
            return None
    def fonk5(self, size):
        self.b12 = [class1.class2(b1, b2) for b2 in range(size) for b1 in range(size)]
        b13 = random.randrange(1, size, 2)
        b14 = random.randrange(1, size, 2)
        b15 = self.b12[b13 + b14 * size]
        b16 = b15.fonk3(size, self.b12)
        b15.b4 = True
        b15.b3 = False
        while b16:
            b17 = random.choice(b16)
            b7 = b17.fonk4(self.b12, size)
            if b7:
                b17.b3 = False
                b7.b4 = True
                b16.extend(b7.fonk3(size, self.b12))
                b16 = list(set(b16))
            b16.remove(b17)