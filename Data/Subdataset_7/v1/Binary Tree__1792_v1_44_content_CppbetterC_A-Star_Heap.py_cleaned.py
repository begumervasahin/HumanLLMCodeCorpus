class class1:
    def fonk1(self, b1, b2, b3, b4):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = None
        self.b6 = None
        self.b7 = None
class class2:
    def fonk2(self, b9):
        self.b8 = {}
        self.b9 = b9
    def fonk3(self, data):
        b4 = self.tree_size + 1
        if b4 > 1:
            b10 = int(b4 / 2)
            b11 = class1(data.b1, data.b2, data.b3, b4)
            self.b8[b4] = b11
            if b11.b4 = = 2 * self.b8[b10].b4:
                self.b8[b10].b5 = b11
            else:
                self.b8[b10].b6 = b11
            b11.b7 = self.b8[b10]
            while True:
                if self.fonk5(self.b8[b4]) < self.fonk5(self.b8[b10]):
                    self.fonk7(self.b8, b4, b10)
                    b4 = b10
                    b10 = int(b10 / 2)
                    if b10 = = 0:
                        break
                else:
                    break
        else:
            self.b8[b4] = data
    def fonk4(self):
        b4 = self.tree_size
        if b4 <= 0:
            return None
        self.fonk7(self.b8, 1, b4)
        b12 = self.b8[1]
        self.b8.pop(b4)
        self.fonk6(self.b8, 1, len(self.b8))
        return b12
    def fonk5(self, data):
        if 'b2' in self.b9 and 'b3' in self.b9:
            return data.b2 + data.b3
        elif 'b2' in self.b9:
            return data.b2
        elif 'b3' in self.b9:
            return data.b3
        else:
            raise Exception('<---Dimension Error--->')
    def fonk6(self, data, root, length):
        b13 = 2 * root
        b14 = 2 * root + 1
        if b13 < length and self.fonk5(data[b13]) < self.fonk5(data[root]):
            b15 = b13
        else:
            b15 = root
        if b14 < length and self.fonk5(data[b14]) < self.fonk5(data[b15]):
            b15 = b14
        if b15 != root:
            self.fonk7(data, root, b15)
            self.fonk6(data, b15, length)
    @staticmethod
    def fonk7(data, x, y):
        if x != y:
            data[x], data[y] = data[y], data[x]
    @property
    def fonk8(self):
        return len(self.b8)
b16 = class2(['b2', 'b3'])
b17 = class1(1, 10, 5, 1)
b18 = class1(2, 8, 4, 2)
b19 = class1(3, 12, 6, 3)
b16.fonk3(b17)
b16.fonk3(b18)
b16.fonk3(b19)
print("Tree size:", b16.tree_size)
print("Extracted max:", b16.fonk4().b1)
print("Tree size after extraction:", b16.tree_size)