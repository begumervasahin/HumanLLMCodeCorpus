class class1:
    def fonk1(self, nbuckets):
        self.b1 = [[] for _ in range(nbuckets)]
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
    def fonk3(self, key, value):
        if self.b1 is None or len(self.b1) == 0:
            return
        b2 = self.fonk2(key) % len(self.b1)
        b3 = self.b1[b2]
        b4 = False
        for i in range(len(b3)):
            if b3[i][0] == key:
                b3[i] = (key, value)
                b4 = True
                break
        if not b4:
            b3.append((key, value))
    def fonk4(self, key):
        if self.b1 is None or len(self.b1) == 0:
            return None
        b2 = self.fonk2(key) % len(self.b1)
        b3 = self.b1[b2]
        for b5, node_value in b3:
            if b5 = = key:
                return node_value
        return None
    def fonk5(self):
        if self.b1 is None:
            return None
        b6 = '{'
        for b3 in self.b1:
            for key, value in b3:
                b6 += str(key) + ':' + str(value) + ', '
        b6 = b6.rstrip(', ')
        b6 += '}'
        return b6
    def fonk6(self):
        return str(self)
    def fonk7(self):
        if self.b1 is None:
            return None
        b6 = ""
        for i, b3 in enumerate(self.b1):
            b6 += str(i).zfill(4) + '->'
            for key, value in b3:
                b6 += str(key) + ':' + str(value) + ', '
            b6 = b6.rstrip(', ')
            b6 += '\n'
        return b6
b7 = class1(5)
b7.fonk3("apple", 10)
b7.fonk3("banana", 20)
b7.fonk3("apple", 5)
print("class1:", b7)
print("Buckets:", b7.fonk7())
print("Get 'apple':", b7.fonk4("apple"))
print("Get 'banana':", b7.fonk4("banana"))
print("Get 'orange':", b7.fonk4("orange"))