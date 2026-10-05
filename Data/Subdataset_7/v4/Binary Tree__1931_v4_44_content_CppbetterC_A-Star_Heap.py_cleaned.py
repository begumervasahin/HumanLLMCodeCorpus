from Edges import Edges
class class1:
    def fonk1(self, b2):
        self.b1 = {}
        self.b2 = b2
    def fonk2(self, data):
        b3 = self.tree_size + 1
        if b3 > 1:
            b4 = int(b3 / 2)
            b5 = Edges(data.id, data.distance, data.time, b3)
            self.b1[b3] = b5
            if b5.b3 = = 2 * self.b1[b4].b3:
                self.b1[b4].b6 = b5
            else:
                self.b1[b4].b7 = b5
            b5.b8 = self.b1[b4]
            while True:
                if self.fonk4(self.b1[b3]) < self.fonk4(self.b1[b4]):
                    self.fonk6(self.b1, b3, b4)
                    b3 = b4
                    b4 = int(b4 / 2)
                    if b4 = = 0:
                        break
                else:
                    break
        else:
            self.b1[b3] = data
    def fonk3(self):
        b3 = self.tree_size
        if b3 <= 0:
            return None
        self.fonk6(self.b1, 1, b3)
        b9 = self.b1[1]
        self.b1.pop(b3)
        self.fonk5(self.b1, 1, len(self.b1))
        return b9
    def fonk4(self, data):
        if 'distance' in self.b2 and 'time' in self.b2:
            return data.distance + data.time
        elif 'distance' in self.b2:
            return data.distance
        elif 'time' in self.b2:
            return data.time
        else:
            raise Exception('<---Dimension Error--->')
    def fonk5(self, data, root, length):
        b10 = 2 * root
        b11 = 2 * root + 1
        if b10 < length and self.fonk4(data[b10]) < self.fonk4(data[root]):
            b12 = b10
        else:
            b12 = root
        if b11 < length and self.fonk4(data[b11]) < self.fonk4(data[b12]):
            b12 = b11
        if b12 != root:
            self.fonk6(data, root, b12)
            self.fonk5(data, b12, length)
    @staticmethod
    def fonk6(data, x, y):
        if x != y:
            data[x], data[y] = data[y], data[x]
    @property
    def fonk7(self):
        return len(self.b1)