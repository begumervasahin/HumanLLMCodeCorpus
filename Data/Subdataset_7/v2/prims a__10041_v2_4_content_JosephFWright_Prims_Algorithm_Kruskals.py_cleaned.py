class class1:
    def fonk1(self, edge_file_name):
        pass
def fonk2(edge_file_name, b1 = 0):
    def fonk3(b6, i):
        if b6[i] == i:
            return i
        return fonk3(b6, b6[i])
    def fonk4(b6, b7, b10, b11):
        b2 = fonk3(b6, b10)
        b3 = fonk3(b6, b11)
        if b7[b2] < b7[b3]:
            b6[b2] = b3
        elif b7[b2] > b7[b3]:
            b6[b3] = b2
        else:
            b6[b3] = b2
            b7[b2] += 1
    b4 = class1(edge_file_name)
    b5 = sorted(b4.edges(), key=lambda b10: b10[2])
    b6 = [i for i in range(len(b4.vertex_set()))]
    b7 = [0] * len(b4.vertex_set())
    b8 = []
    for edge in b5:
        u, v, b9 = edge
        b10 = fonk3(b6, u)
        b11 = fonk3(b6, v)
        if b10 != b11:
            b8.append(edge)
            fonk4(b6, b7, b10, b11)
    return b8
