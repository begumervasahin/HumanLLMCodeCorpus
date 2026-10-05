class class1:
    def fonk1(self, key):
        self.b1 = key
        self.b2 = {}
    def fonk2(self, nbr, b3 = 0):
        self.b2[nbr] = b3
    def fonk3(self):
        return f"{self.b1} connectedTo: {[x.b1 for x in self.b2]}"
    def fonk4(self):
        return self.b2.keys()
    def fonk5(self):
        return self.b1
    def fonk6(self, nbr):
        return self.b2[nbr]
class class2:
    def fonk7(self):
        self.b4 = {}
        self.a1 = 0
    def fonk8(self, key):
        self.a1 += 1
        b5 = class1(key)
        self.b4[key] = b5
        return b5
    def fonk9(self, n):
        return self.b4.get(n)
    def fonk10(self, n):
        return n in self.b4
    def fonk11(self, f, t, b6 = 0):
        if f not in self.b4:
            self.fonk8(f)
        if t not in self.b4:
            self.fonk8(t)
        self.b4[f].fonk2(self.b4[t], b6)
    def fonk12(self):
        return self.b4.keys()
    def fonk13(self):
        return iter(self.b4.values())
b7 = class2()
for a2 in range(6):
    b7.fonk8(a2)
print(b7.b4)
b7.fonk11(0, 1, 5)
b7.fonk11(0, 5, 2)
b7.fonk11(1, 2, 4)
b7.fonk11(2, 3, 9)
b7.fonk11(3, 4, 7)
b7.fonk11(3, 5, 3)
b7.fonk11(4, 0, 1)
b7.fonk11(5, 4, 8)
b7.fonk11(5, 2, 1)
for v in b7:
    for w in v.fonk4():
        print(f"( {v.fonk5()} , {w.fonk5()} )")
def fonk14(word_file):
    b8 = {}
    b7 = class2()
    with open(word_file, 'r') as wfile:
        for line in wfile:
            b9 = line.strip()
            for a2 in range(len(b9)):
                b10 = b9[:a2] + '_' + b9[a2 + 1:]
                b8.setdefault(b10, []).append(b9)
    for b10 in b8.keys():
        for word1 in b8[b10]:
            for word2 in b8[b10]:
                if word1 != word2:
                    b7.fonk11(word1, word2)
    return b7
def fonk15(bd_size):
    b11 = class2()
    for row in range(bd_size):
        for col in range(bd_size):
            b12 = fonk16(row, col, bd_size)
            b13 = fonk17(row, col, bd_size)
            for e in b13:
                b14 = fonk16(e[0], e[1], bd_size)
                b11.fonk11(b12, b14)
    return b11
def fonk16(row, column, board_size):
    return (row * board_size) + column
def fonk17(x, y, bd_size):
    b15 = []
    b16 = [(-1, -2), (-1, 2), (-2, -1), (-2, 1),
                    (1, -2), (1, 2), (2, -1), (2, 1)]
    for a2 in b16:
        b17 = x + a2[0]
        b18 = y + a2[1]
        if fonk18(b17, bd_size) and fonk18(b18, bd_size):
            b15.append((b17, b18))
    return b15
def fonk18(x, bd_size):
    return 0 <= x < bd_size
def fonk19(n, path, u, limit):
    u.set_color('gray')
    path.append(u)
    if n < limit:
        b19 = list(u.fonk4())
        a2 = 0
        b20 = False
        while a2 < len(b19) and not b20:
            if b19[a2].get_color() == 'white':
                b20 = fonk19(n + 1, path, b19[a2], limit)
            a2 += 1
        if not b20:
            path.pop()
            u.set_color('white')
    else:
        b20 = True
    return b20