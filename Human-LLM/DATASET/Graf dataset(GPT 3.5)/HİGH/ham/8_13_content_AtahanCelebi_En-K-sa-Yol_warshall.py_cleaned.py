def fonk1(path_v1):
    from map_distance import main
    b1 = fonk1(path_v1)[0]
    b2 = list()
    for i in range(len(b1)):
        if b1[i][2] < 900:
            b2.append(b1[i])
    print("b1 coor", b2)
    b3 = fonk1(path_v1)[1]
    class class1:
        def fonk2(self):
            self.b4 = {}
        def fonk3(self, b7):
            b5 = class2(b7)
            self.b4[b7] = b5
        def fonk4(self, b7):
            return self.b4[b7]
        def fonk5(self, b7):
            return b7 in self.b4
        def fonk6(self, src_key, dest_key, b6 = 1):
            self.b4[src_key].fonk12(self.b4[dest_key], b6)
        def fonk7(self, src_key, dest_key):
            return self.b4[src_key].fonk15(self.b4[dest_key])
        def fonk8(self):
            return len(self.b4)
        def fonk9(self):
            return iter(self.b4.values())
    class class2:
        def fonk10(self, b7):
            self.b7 = b7
            self.b8 = {}
        def fonk11(self):
            return self.b7
        def fonk12(self, dest, b6):
            self.b8[dest] = b6
        def fonk13(self):
            return self.b8.keys()
        def fonk14(self, dest):
            return self.b8[dest]
        def fonk15(self, dest):
            return dest in self.b8
    def fonk16(b13):
        b9 = {v:dict.fromkeys(b13, float('inf')) for v in b13}
        b10 = {v:dict.fromkeys(b13, None) for v in b13}
        for v in b13:
            for n in v.fonk13():
                b9[v][n] = v.fonk14(n)
                b10[v][n] = n
        for v in b13:
             b9[v][v] = 0
             b10[v][v] = None
        for b11 in b13:
            for v in b13:
                for w in b13:
                    if b9[v][w] > b9[v][b11] + b9[b11][w]:
                        b9[v][w] = b9[v][b11] + b9[b11][w]
                        b10[v][w] = b10[v][b11]
        return b9, b10
    def fonk17(b10, u, v):
        b11 = u
        b12 = list()
        while (b10[b11][v]):
            b12.append(b11.fonk11())
            b11 = b10[b11][v]
        b12.append(v.fonk11())
        return b12
    b13 = class1()
    for i in range(b3):
        b13.fonk3(i+1)
    for i,j,k in b2:
        b13.fonk6(i, j, k)
    b9, b10 = fonk16(b13)
    b14 = list()
    for start in b13:
        for end in b13:
            if b10[start][end]:
                b14.append([[start.fonk11(),end.fonk11()],fonk17(b10, start, end),[b9[start][end]]])
    return b14