from math import sqrt
class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = []
    def fonk2(self, point):
        self.b2.append(point)
    def fonk3(self, point):
        return point in self.b2
class class2:
    def fonk4(self, b3, b4):
        self.b3 = b3
        self.b4 = b4
        self.b5 = []
        self.b6 = []
        self.b7 = []
        self.b8 = []
    def fonk5(self, b5):
        self.b5 = b5
        a1 = -1
        for point in self.b5:
            if point not in self.b6:
                self.b6.append(point)
                b9 = self.fonk7(point)
                if len(b9) < self.b4:
                    self.b8.append(point)
                else:
                    a1 += 1
                    b10 = class1(f'class1{a1}')
                    self.fonk6(point, b9, b10)
                    self.b7.append(b10)
    def fonk6(self, point, b9, b10):
        b10.fonk2(point)
        a2 = 0
        while a2 < len(b9):
            b11 = b9[a2]
            if b11 not in self.b6:
                self.b6.append(b11)
                b12 = self.fonk7(b11)
                if len(b12) >= self.b4:
                    b9 += b12
            if not any(c.fonk3(b11) for c in self.b7):
                b10.fonk2(b11)
            a2 += 1
    def fonk7(self, point):
        return [d for d in self.b5 if self.fonk8(d, point) <= self.b3]
    @staticmethod
    def fonk8(point1, point2):
        return sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)
if b13 = = "__main__":
    b2 = [
        [1, 2], [2, 2], [2, 3], [8, 7], [8, 8], [25, 80],
        [0, 2], [1, 1], [2, 1], [7, 8], [8, 9], [25, 81]
    ]
    b14 = class2(b3=2, b4=2)
    b14.fonk5(b2)
    for b10 in b14.b7:
        print(f'{b10.b1}: {b10.b2}')
    print(f'Noise: {b14.b8}')