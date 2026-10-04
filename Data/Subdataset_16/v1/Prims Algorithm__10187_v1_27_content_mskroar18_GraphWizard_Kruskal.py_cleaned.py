class class1:
    def fonk1(self, vertex1, vertex2, b3):
        self.b1 = vertex1
        self.b2 = vertex2
        self.b3 = b3
        self.b4 = False
def fonk2(edge):
    return edge.b3
def fonk3(edgelist, nodecount):
    edgelist.sort(b5 = returnweight)
    a1 = 0
    b6 = []
    edgelist[a1].b4 = True
    a1 += 1
    b6.append(set())
    b6[0].add(edgelist[0])
    a2 = 1
    while a1 < len(edgelist):
        b7 = False
        b8 = False
        b9 = False
        a3 = -1
        a4 = -1
        for j in range(a2):
            for edge in b6[j]:
                if edge.b2 = = edgelist[a1].b1:
                    b7 = True
                    a3 = j
                if edge.b2 = = edgelist[a1].b2:
                    b8 = True
                    a4 = j
                if edge.b1 = = edgelist[a1].b1:
                    b7 = True
                    a3 = j
                if edge.b1 = = edgelist[a1].b2:
                    b8 = True
                    a4 = j
        if b7 and b8 and a3 = = a4:
            b9 = True
        else:
            if b7 and b8:
                if a3 < a4:
                    b6[a3] = b6[a3].union(b6[a4])
                    b6[a3].add(edgelist[a1])
                    b6[a4].clear()
                    edgelist[a1].b4 = True
                else:
                    b6[a4] = b6[a4].union(b6[a3])
                    b6[a3].clear()
                    b6[a4].add(edgelist[a1])
                    edgelist[a1].b4 = True
            else:
                if b7 and not b8:
                    b6[a3].add(edgelist[a1])
                    edgelist[a1].b4 = True
                if not b7 and b8:
                    b6[a4].add(edgelist[a1])
                    edgelist[a1].b4 = True
        if not b7 and not b8:
            edgelist[a1].b4 = True
            b6.append(set())
            b6[a2].add(edgelist[a1])
            a2 += 1
        a1 += 1
    return edgelist
b10 = [class1(1, 2, 1), class1(2, 3, 2), class1(3, 4, 3), class1(1, 4, 4)]
a5 = 4
b11 = fonk3(b10, a5)
for edge in b11:
    if edge.b4:
        print(f"class1 ({edge.b1}, {edge.b2}) with b3 {edge.b3} is b4")