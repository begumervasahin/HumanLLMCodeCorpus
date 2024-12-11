from Edges import Edges
class class1:
    def fonk1(self, b2):
        self.b1 = []
        self.b2 = b2
    def fonk2(self, data):
        self.b1.append(data)
        b3 = len(self.b1) - 1
        self.fonk5(b3)
    def fonk3(self):
        if not self.b1:
            return None
        b4 = self.b1[0]
        self.b1[0] = self.b1[-1]
        self.b1.pop()
        self.fonk6(0)
        return b4
    def fonk4(self, data):
        if 'distance' in self.b2 and 'time' in self.b2:
            return data.distance + data.time
        elif 'distance' in self.b2:
            return data.distance
        elif 'time' in self.b2:
            return data.time
        else:
            raise Exception('<---Dimension Error--->')
    def fonk5(self, b3):
        while b3 > 0:
            b5 = (b3 - 1)
            if self.fonk4(self.b1[b3]) < self.fonk4(self.b1[b5]):
                self.b1[b3], self.b1[b5] = self.b1[b5], self.b1[b3]
                b3 = b5
            else:
                break
    def fonk6(self, b3):
        b6 = len(self.b1)
        while True:
            b7 = 2 * b3 + 1
            b8 = 2 * b3 + 2
            b9 = b3
            if b7 < b6 and self.fonk4(self.b1[b7]) < self.fonk4(self.b1[b9]):
                b9 = b7
            if b8 < b6 and self.fonk4(self.b1[b8]) < self.fonk4(self.b1[b9]):
                b9 = b8
            if b9 != b3:
                self.b1[b3], self.b1[b9] = self.b1[b9], self.b1[b3]
                b3 = b9
            else:
                break
    @property
    def fonk7(self):
        return len(self.b1)