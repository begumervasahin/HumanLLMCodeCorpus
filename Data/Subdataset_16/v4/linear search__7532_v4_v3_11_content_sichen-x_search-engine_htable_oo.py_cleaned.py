class class1:
    def fonk1(self, b1 = 31):
        self.b2 = b1
        self.b3 = [[] for _ in range(self.b2)]
    def fonk2(self, key):
        if isinstance(key, int):
            return key
        elif isinstance(key, str):
            a1 = 0
            for char in key:
                a1 = a1 * 31 + ord(char)
            return a1
        else:
            raise TypeError("Unsupported key type")
    def fonk3(self):
        b4 = ""
        for i, b6 in enumerate(self.b3):
            b4 += f"{str(i).zfill(4)}->"
            b4 += ', '.join([f"{node[0]}:{node[1]}" for node in b6])
            b4 += '\n'
        return b4
    def fonk4(self):
        b4 = '{'
        for b6 in self.b3:
            for key, value in b6:
                b4 += f"{key}:{value}, "
        b4 = b4.rstrip(', ')
        b4 += '}'
        return b4
    def fonk5(self, key, value):
        b5 = self.fonk2(key) % self.b2
        b6 = self.b3[b5]
        for i, (b7, v) in enumerate(b6):
            if b7 = = key:
                b6[i] = (key, v | value)
                break
        else:
            b6.append((key, value))
    def fonk6(self, key):
        b5 = self.fonk2(key) % self.b2
        b6 = self.b3[b5]
        for b7, v in b6:
            if b7 = = key:
                return v
        return None
    def fonk7(self, index):
        if index < 0 or index >= self.b2:
            raise IndexError("Bucket index out of range")
        b4 = '{'
        for b7, v in self.b3[index]:
            b4 += f"{b7}:{v}, "
        b4 = b4.rstrip(', ')
        b4 += '}'
        return b4
    def fonk8(self, key):
        return self.fonk6(key)
    def fonk9(self, key, value):
        self.fonk5(key, value)
if b8 = = '__main__':
    a1 = class1()
    a1['a'] = 34
    print(a1['a'])
    b9 = class1(5)
    for i in range(1, 11):
        b9.fonk5(i, i)
    print(b9.fonk7(0))