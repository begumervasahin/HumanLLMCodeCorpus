
def fonk1(b16):
    from map_distance import main as get_edge_data
    edges, b1 = get_edge_data(b16)
    b2 = [(i, j, k) for i, j, k in edges if k < 900]
    class class1:
        def fonk2(self):
            self.b3 = {}
        def fonk3(self, b6):
            b4 = class2(b6)
            self.b3[b6] = b4
        def fonk4(self, b6):
            return self.b3[b6]
        def fonk5(self, b6):
            return b6 in self.b3
        def fonk6(self, src_key, dest_key, b5 = 1):
            self.b3[src_key].fonk12(self.b3[dest_key], b5)
        def fonk7(self, src_key, dest_key):
            return self.b3[src_key].fonk15(self.b3[dest_key])
        def fonk8(self):
            return len(self.b3)
        def fonk9(self):
            return iter(self.b3.values())
    class class2:
        def fonk10(self, b6):
            self.b6 = b6
            self.b7 = {}
        def fonk11(self):
            return self.b6
        def fonk12(self, dest, b5):
            self.b7[dest] = b5
        def fonk13(self):
            return self.b7.keys()
        def fonk14(self, dest):
            return self.b7[dest]
        def fonk15(self, dest):
            return dest in self.b7
    def fonk16(b12):
        b8 = {v: {u: float('inf') for u in b12} for v in b12}
        b9 = {v: {u: None for u in b12} for v in b12}
        for v in b12:
            for n in v.fonk13():
                b8[v][n] = v.fonk14(n)
                b9[v][n] = n
        for v in b12:
            b8[v][v] = 0
            b9[v][v] = None
        for b10 in b12:
            for v in b12:
                for w in b12:
                    if b8[v][w] > b8[v][b10] + b8[b10][w]:
                        b8[v][w] = b8[v][b10] + b8[b10][w]
                        b9[v][w] = b9[v][b10]
        return b8, b9
    def fonk17(b9, u, v):
        b10 = u
        b11 = []
        while b9[b10][v]:
            b11.append(b10.fonk11())
            b10 = b9[b10][v]
        b11.append(v.fonk11())
        return b11
    b12 = class1()
    for i in range(b1):
        b12.fonk3(i + 1)
    for i, j, k in b2:
        b12.fonk6(i, j, k)
    b8, b9 = fonk16(b12)
    b13 = []
    for start in b12:
        for end in b12:
            if b9[start][end]:
                b14 = fonk17(b9, start, end)
                b13.append([[start.fonk11(), end.fonk11()], b14, [b8[start][end]]])
    return b13
if b15 = = "__main__":
    b16 = "path_to_your_text_file.txt"
    b17 = fonk1(b16)
    print(b17)