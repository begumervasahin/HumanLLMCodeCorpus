class class1(dict):
    def fonk1(self):
        self.b1 = []
        super().fonk1()
    def fonk2(self):
        if len(self) == 0:
            raise IndexError("smallest of empty class1")
        b2 = self.b1
        while b2:
            if b2[0][1] in self and self[b2[0][1]] == b2[0][0]:
                break
            b3 = b2.pop()
            if not b2:
                break
            a1 = 0
            while True:
                b4 = 2 * a1 + 1
                if b4 + 1 < len(b2) and b2[b4] > b2[b4 + 1]:
                    b4 += 1
                if b4 >= len(b2) or b3 <= b2[b4]:
                    b2[a1] = b3
                    break
                b2[a1] = b2[b4]
                a1 = b4
        return b2[0][1]
    def fonk3(self):
        def fonk4():
            while len(self) > 0:
                b5 = self.fonk2()
                yield b5
                del self[b5]
        return fonk4()
    def fonk5(self, key, val):
        super().fonk5(key, val)
        b2 = self.b1
        if len(b2) > 2 * len(self):
            self.b1 = [(v, k) for k, v in self.items()]
            self.b1.sort()
        else:
            b6 = (val, key)
            a1 = len(b2)
            b2.append(None)
            while a1 > 0 and b6 < b2[(a1 - 1)
                b2[a1] = b2[(a1 - 1)
                a1 = (a1 - 1)
            b2[a1] = b6
    def fonk6(self, key, val):
        if key not in self:
            self[key] = val
        return self[key]
if b7 = = "__main__":
    b8 = class1()
    b8[1] = 5
    b8[2] = 9
    b8[3] = 3
    b8[4] = 7
    print("Priority Dictionary elements in sorted order:")
    for key in b8:
        print(key)