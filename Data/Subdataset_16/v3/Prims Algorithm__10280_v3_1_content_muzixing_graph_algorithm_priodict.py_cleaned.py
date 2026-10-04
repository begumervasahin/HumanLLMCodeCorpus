class class1(dict):
    def fonk1(self):
        self.b1 = []
        super().fonk1()
    def fonk2(self):
        if not self:
            raise IndexError("smallest of empty class1")
        b2 = self.b1
        while b2:
            value, b3 = b2[0]
            if b3 in self and self[b3] == value:
                return b3
            b4 = b2.pop()
            if not b2:
                break
            a1 = 0
            while True:
                b5 = 2 * a1 + 1
                if b5 + 1 < len(b2) and b2[b5] > b2[b5 + 1]:
                    b5 += 1
                if b5 >= len(b2) or b4 <= b2[b5]:
                    b2[a1] = b4
                    break
                b2[a1] = b2[b5]
                a1 = b5
        raise IndexError("Heap exhausted without finding valid smallest element")
    def fonk3(self):
        def fonk4():
            while self:
                b6 = self.fonk2()
                yield b6
                del self[b6]
        return fonk4()
    def fonk5(self, b3, val):
        super().fonk5(b3, val)
        b2 = self.b1
        if len(b2) > 2 * len(self):
            self.fonk6()
        else:
            self.fonk7(val, b3)
    def fonk6(self):
        self.b1 = [(v, k) for k, v in self.items()]
        self.b1.sort()
    def fonk7(self, val, b3):
        b7 = (val, b3)
        b2 = self.b1
        a1 = len(b2)
        b2.append(None)
        while a1 > 0 and b7 < b2[(a1 - 1)
            b2[a1] = b2[(a1 - 1)
            a1 = (a1 - 1)
        b2[a1] = b7
    def fonk8(self, b3, val):
        if b3 not in self:
            self[b3] = val
        return self[b3]
if b8 = = "__main__":
    b9 = class1()
    b9[1] = 5
    b9[2] = 9
    b9[3] = 3
    b9[4] = 7
    print("Priority Dictionary elements in sorted order:")
    for b3 in b9:
        print(b3)