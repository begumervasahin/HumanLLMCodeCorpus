class class1:
    def fonk1(self):
        self.a1 = 11
        self.b1 = [None] * self.a1
        self.b2 = [None] * self.a1
    def fonk2(self, key, b2):
        b3 = self.fonk3(key, len(self.b1))
        if self.b1[b3] is None:
            self.b1[b3] = key
            self.b2[b3] = b2
        else:
            if self.b1[b3] == key:
                self.b2[b3] = b2
            else:
                b4 = self.fonk4(b3, len(self.b1))
                while self.b1[b4] is not None and self.b1[b4] != key:
                    b4 = self.fonk4(b4, len(self.b1))
                if self.b1[b4] is None:
                    self.b1[b4] = key
                    self.b2[b4] = b2
                else:
                    self.b2[b4] = b2
    def fonk3(self, key, a1):
        return key % a1
    def fonk4(self, oldhash, a1):
        return (oldhash + 1) % a1
    def fonk5(self, key):
        b5 = self.fonk3(key, len(self.b1))
        b2 = None
        b6 = False
        b7 = False
        b8 = b5
        while self.b1[b8] is not None and not b7 and not b6:
            if self.b1[b8] == key:
                b7 = True
                b2 = self.b2[b8]
            else:
                b8 = self.fonk4(b8, len(self.b1))
                if b8 = = b5:
                    b6 = True
        return b2
    def fonk6(self, key):
        return self.fonk5(key)
    def fonk7(self, key, b2):
        self.fonk2(key, b2)
if b9 = = "__main__":
    b10 = class1()
    b10[54] = "cat"
    b10[26] = "dog"
    b10[93] = "lion"
    b10[17] = "tiger"
    b10[77] = "bird"
    b10[31] = "cow"
    b10[44] = "goat"
    b10[55] = "pig"
    b10[20] = "chicken"
    print(b10.b1)
    print(b10.b2)
    print(b10[20])
    print(b10[17])
    b10[20] = 'duck'
    print(b10[20])
    print(b10[99])