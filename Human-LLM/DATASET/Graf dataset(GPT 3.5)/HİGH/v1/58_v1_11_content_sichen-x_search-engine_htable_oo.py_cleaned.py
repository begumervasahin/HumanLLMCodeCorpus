class class1:
    def fonk1(self, b1 = 31):
        self.b2 = b1
        self.b3 = []
        for i in range(self.b2):
            self.b3.append([])
    def fonk2(self, o):
        if isinstance(o, int):
            return o
        elif isinstance(o, str):
            a1 = 0
            for char in o:
                a1 = a1 * 31 + ord(char)
            return a1
        else:
            return None
    def fonk3(self):
        if self.b3 is None:
            return None
        b4 = ""
        for i in range(len(self.b3)):
            b4 += str(i).zfill(4)
            b4 += '->'
            for node in self.b3[i]:
                b4 += str(node[0]) + ':' + str(node[1])
                b4 += ', '
            b4 = b4.rstrip(', ')
            b4 += '\n'
        return b4
    def fonk4(self):
        if self.b3 is None:
            return None
        b4 = '{'
        for i in range(len(self.b3)):
            for node in self.b3[i]:
                b4 += str(node[0]) + ':' + str(node[1])
                b4 += ', '
        b4 = b4.rstrip(', ')
        b4 += '}'
        return b4
    def fonk5(self, key, value):
        if self.b3 is None or len(self.b3) == 0:
            return
        b5 = self.fonk2(key) % len(self.b3)
        b6 = self.b3[b5]
        b7 = True
        for i in range(len(b6)):
            if b6[i][0] == key:
                b8 = b6[i][1] | value
                b6[i] = (key, b8)
                b7 = False
                break
        if b7:
            b6.append((key, value))
    def fonk6(self, key):
        if self.b3 is None or len(self.b3) == 0:
            return None
        b5 = self.fonk2(key) % len(self.b3)
        b6 = self.b3[b5]
        for node in b6:
            if node[0] == key:
                return node[1]
        return None
    def fonk7(self, key):
        if self.b3 is None or len(self.b3) == 0:
            return None
        b4 = '{'
        for node in self.b3[key]:
            b4 += str(node[0]) + ':' + str(node[1])
            b4 += ', '
        b4 = b4.rstrip(', ')
        b4 += '}'
        return b4
    def fonk8(self, key):
        return self.fonk6(key)
    def fonk9(self, key, value):
        self.fonk5(key, value)
if b9 = = '__main__':
    a1 = class1()
    a1['a'] = 34
    print(a1['a'])
    b10 = class1(5)
    for i in range(1, 11):
        b10.fonk5(i, i)
    print(b10.fonk7(0))