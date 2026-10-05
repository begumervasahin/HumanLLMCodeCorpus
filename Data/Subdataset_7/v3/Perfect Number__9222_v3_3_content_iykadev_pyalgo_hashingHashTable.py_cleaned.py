class class1:
    def fonk1(self, b1 = 11):
        self.b1 = b1
        self.b2 = [None] * self.b1
        self.b3 = [None] * self.b1
    def fonk2(self, key, b3):
        b4 = self.fonk3(key)
        if self.b2[b4] is None:
            self.b2[b4] = key
            self.b3[b4] = b3
        else:
            if self.b2[b4] == key:
                self.b3[b4] = b3
            else:
                b5 = self.fonk4(b4)
                while self.b2[b5] is not None and self.b2[b5] != key:
                    b5 = self.fonk4(b5)
                if self.b2[b5] is None:
                    self.b2[b5] = key
                    self.b3[b5] = b3
                else:
                    self.b3[b5] = b3
    def fonk3(self, key):
        return key % self.b1
    def fonk4(self, old_hash):
        return (old_hash + 1) % self.b1
    def fonk5(self, key):
        b6 = self.fonk3(key)
        b3 = None
        b7 = False
        b8 = False
        b9 = b6
        while self.b2[b9] is not None and not b8 and not b7:
            if self.b2[b9] == key:
                b8 = True
                b3 = self.b3[b9]
            else:
                b9 = self.fonk4(b9)
                if b9 = = b6:
                    b7 = True
        return b3
    def fonk6(self, key):
        return self.fonk5(key)
    def fonk7(self, key, b3):
        self.fonk2(key, b3)
if b10 = = "__main__":
    b11 = class1()
    b11[54] = "cat"
    b11[26] = "dog"
    b11[93] = "lion"
    b11[17] = "tiger"
    b11[77] = "bird"
    b11[31] = "cow"
    b11[44] = "goat"
    b11[55] = "pig"
    b11[20] = "chicken"
    print("Slots:", b11.b2)
    print("Data:", b11.b3)
    print("Value associated with key 20:", b11[20])
    print("Value associated with key 17:", b11[17])
    b11[20] = 'duck'
    print("Updated value associated with key 20:", b11[20])
    print("Value associated with key 99:", b11[99])