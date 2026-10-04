class class1:
    def fonk1(self, b1, b2, b3):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = False
def fonk2(edge):
    return edge.b3
def fonk3(edgelist, a5):
    edgelist.sort(b5 = return_weight)
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
                    b6[a3].update(b6[a4])
                    b6[a3].add(edgelist[a1])
                    b6[a4].clear()
                    edgelist[a1].b4 = True
                else:
                    b6[a4].update(b6[a3])
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
            b10 = set()
            b10.add(edgelist[a1])
            b6.append(b10)
            a2 += 1
        a1 += 1
    return edgelist
b11 = [
    class1(1, 2, 1),
    class1(2, 3, 2),
    class1(3, 4, 3),
    class1(1, 4, 4)
]
a5 = 4
b12 = fonk3(b11, a5)
for edge in b12:
    if edge.b4:
        print(f"class1 ({edge.b1}, {edge.b2}) with b3 {edge.b3} is b4")