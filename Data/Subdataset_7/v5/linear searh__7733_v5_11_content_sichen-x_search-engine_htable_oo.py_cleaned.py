class class1:
    def fonk1(self, b1 = 31):
        self.b1 = b1
        self.b2 = [[] for _ in range(self.b1)]
    def fonk2(self, key):
        if isinstance(key, int):
            return key
        elif isinstance(key, str):
            a1 = 0
            for char in key:
                a1 = a1 * 31 + ord(char)
            return a1
        else:
            return None
    def fonk3(self, b8):
        b3 = ""
        for key, value in b8:
            b3 += f"{key}:{value}, "
        return "{" + b3.rstrip(", ") + "}"
    def fonk4(self):
        b4 = ""
        for i, b8 in enumerate(self.b2):
            b5 = self.fonk3(b8)
            b4 += f"{str(i).zfill(4)}->{b5}\n"
        return b4
    def fonk5(self):
        b6 = ""
        for b8 in self.b2:
            b6 += self.fonk3(b8)
        return "{" + b6.rstrip(", ") + "}"
    def fonk6(self, key, value):
        b7 = self.fonk2(key) % len(self.b2)
        b8 = self.b2[b7]
        for i, (b9, v) in enumerate(b8):
            if b9 = = key:
                b8[i] = (key, v | value)
                return
        b8.append((key, value))
    def fonk7(self, key):
        b7 = self.fonk2(key) % len(self.b2)
        b8 = self.b2[b7]
        for b9, v in b8:
            if b9 = = key:
                return v
        return None
    def fonk8(self, key):
        b7 = self.fonk2(key) % len(self.b2)
        b8 = self.b2[b7]
        return self.fonk3(b8)
    def fonk9(self, key):
        return self.fonk7(key)
    def fonk10(self, key, value):
        self.fonk6(key, value)
if b10 = = '__main__':
    b11 = class1()
    b11['a'] = 34
    print(b11['a'])
    b12 = class1(5)
    for i in range(1, 11):
        b12.fonk6(i, i)
    print(b12.fonk8(0))