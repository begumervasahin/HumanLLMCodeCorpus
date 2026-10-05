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
            b12 = self.b8[b10]
            if b11.b4 = = 2 * b12.b4:
                b12.b5 = b11
            else:
                b12.b6 = b11
            b11.b7 = b12
            self.fonk6(b4)
        else:
            self.b8[b4] = data
    def fonk4(self):
        b4 = self.tree_size
        if b4 <= 0:
            return None
        self.fonk8(1, b4)
        b13 = self.b8[1]
        self.b8.pop(b4)
        self.fonk7(1, len(self.b8))
        return b13
    def fonk5(self, data):
        if 'b2' in self.b9 and 'b3' in self.b9:
            return data.b2 + data.b3
        elif 'b2' in self.b9:
            return data.b2
        elif 'b3' in self.b9:
            return data.b3
        else:
            raise ValueError('<---Dimension Error--->')
    def fonk6(self, b4):
        while b4 > 1:
            b10 = int(b4 / 2)
            if self.fonk5(self.b8[b4]) < self.fonk5(self.b8[b10]):
                self.fonk8(b4, b10)
                b4 = b10
            else:
                break
    def fonk7(self, root, length):
        b14 = 2 * root
        b15 = 2 * root + 1
        b16 = root
        if b14 < length and self.fonk5(self.b8[b14]) < self.fonk5(self.b8[b16]):
            b16 = b14
        if b15 < length and self.fonk5(self.b8[b15]) < self.fonk5(self.b8[b16]):
            b16 = b15
        if b16 != root:
            self.fonk8(root, b16)
            self.fonk7(b16, length)
    def fonk8(self, x, y):
        if x != y:
            self.b8[x], self.b8[y] = self.b8[y], self.b8[x]
    @property
    def fonk9(self):
        return len(self.b8)
b17 = class2(['b2', 'b3'])
b18 = class1(1, 10, 5, 1)
b19 = class1(2, 8, 4, 2)
b20 = class1(3, 12, 6, 3)
b17.fonk3(b18)
b17.fonk3(b19)
b17.fonk3(b20)
print("Tree size:", b17.tree_size)
print("Extracted min:", b17.fonk4().b1)
print("Tree size after extraction:", b17.tree_size)