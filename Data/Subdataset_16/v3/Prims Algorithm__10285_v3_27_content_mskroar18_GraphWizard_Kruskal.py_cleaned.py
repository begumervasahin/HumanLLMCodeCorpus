class class1:
    def fonk1(self, b1, b2, b3):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = False
def fonk2(edge):
    return edge.b3
def fonk3(edge, b10):
    b5 = b7 = False
    b6 = b8 = -1
    for set_index, edge_set in enumerate(b10):
        for e in edge_set:
            if e.b1 = = edge.b1 or e.b2 == edge.b1:
                b5 = True
                b6 = set_index
            if e.b1 = = edge.b2 or e.b2 == edge.b2:
                b7 = True
                b8 = set_index
    return b5, b7, b6, b8
def fonk4(edge, b10, b6, b8):
    if b6 < b8:
        b10[b6].update(b10[b8])
        b10[b6].add(edge)
        b10[b8].clear()
    else:
        b10[b8].update(b10[b6])
        b10[b6].clear()
        b10[b8].add(edge)
    edge.b4 = True
def fonk5(edgelist, a2):
    edgelist.sort(b9 = return_weight)
    b10 = [set([edgelist[0]])]
    edgelist[0].b4 = True
    a1 = 1
    for edge in edgelist[1:]:
        b5, b7, b6, b8 = fonk3(edge, b10)
        if b5 and b7:
            if b6 != b8:
                fonk4(edge, b10, b6, b8)
        elif b5:
            b10[b6].add(edge)
            edge.b4 = True
        elif b7:
            b10[b8].add(edge)
            edge.b4 = True
        else:
            b11 = set([edge])
            b10.append(b11)
            a1 += 1
            edge.b4 = True
    return edgelist
b12 = [
    class1(1, 2, 1),
    class1(2, 3, 2),
    class1(3, 4, 3),
    class1(1, 4, 4)
]
a2 = 4
b13 = fonk5(b12, a2)
for edge in b13:
    if edge.b4:
        print(f"class1 ({edge.b1}, {edge.b2}) with b3 {edge.b3} is b4")