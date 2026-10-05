class class1:
    def fonk1(self):
        self.b1 = {}
    def fonk2(self, b4):
        b2 = class2(b4)
        self.b1[b4] = b2
    def fonk3(self, b4):
        return self.b1[b4]
    def fonk4(self, b4):
        return b4 in self.b1
    def fonk5(self, src_key, dest_key, b3 = 1):
        self.b1[src_key].fonk11(self.b1[dest_key], b3)
    def fonk6(self, src_key, dest_key):
        return self.b1[src_key].fonk14(self.b1[dest_key])
    def fonk7(self):
        return len(self.b1)
    def fonk8(self):
        return iter(self.b1.values())
class class2:
    def fonk9(self, b4):
        self.b4 = b4
        self.b5 = {}
    def fonk10(self):
        return self.b4
    def fonk11(self, dest, b3):
        self.b5[dest] = b3
    def fonk12(self):
        return self.b5.keys()
    def fonk13(self, dest):
        return self.b5[dest]
    def fonk14(self, dest):
        return dest in self.b5
def fonk15(b13):
    b6 = {v: dict.fromkeys(b13, float('inf')) for v in b13}
    b7 = {v: dict.fromkeys(b13, None) for v in b13}
    for v in b13:
        for n in v.fonk12():
            b6[v][n] = v.fonk13(n)
            b7[v][n] = n
    for v in b13:
        b6[v][v] = 0
        b7[v][v] = None
    for b8 in b13:
        for v in b13:
            for w in b13:
                if b6[v][w] > b6[v][b8] + b6[b8][w]:
                    b6[v][w] = b6[v][b8] + b6[b8][w]
                    b7[v][w] = b7[v][b8]
    return b6, b7
def fonk16(b7, u, v):
    b8 = u
    b9 = list()
    while b7[b8][v]:
        b9.append(b8.fonk10())
        b8 = b7[b8][v]
    b9.append(v.fonk10())
    return b9
def fonk17(b17):
    from map_distance import main
    b10 = fonk17(b17)[0]
    b11 = [(i, j, k) for i, j, k in b10 if k < 900]
    b12 = fonk17(b17)[1]
    b13 = class1()
    for i in range(b12):
        b13.fonk2(i + 1)
    for i, j, k in b11:
        b13.fonk5(i, j, k)
    b6, b7 = fonk15(b13)
    b14 = list()
    for start in b13:
        for end in b13:
            if b7[start][end]:
                b15 = fonk16(b7, start, end)
                b14.append([[start.fonk10(), end.fonk10()], b15, [b6[start][end]]])
    return b14
if b16 = = "__main__":
    b17 = "path_to_your_text_file.txt"
    b18 = fonk17(b17)
    print(b18)