class class1:
    def fonk1(self, edge_file_name):
        pass
def fonk2(edge_file_name, b1 = 0):
    def fonk3(b7, i):
        if b7[i] == i:
            return i
        return fonk3(b7, b7[i])
    def fonk4(b7, b8, b11, b12):
        b2 = fonk3(b7, b11)
        b3 = fonk3(b7, b12)
        if b8[b2] < b8[b3]:
            b7[b2] = b3
        elif b8[b2] > b8[b3]:
            b7[b3] = b2
        else:
            b7[b3] = b2
            b8[b2] += 1
    b4 = class1(edge_file_name)
    b5 = sorted(b4.edges(), key=lambda b11: b11[2])
    b6 = len(b4.vertex_set())
    b7 = [i for i in range(b6)]
    b8 = [0] * b6
    b9 = []
    for edge in b5:
        u, v, b10 = edge
        b11 = fonk3(b7, u)
        b12 = fonk3(b7, v)
        if b11 != b12:
            b9.append(edge)
            fonk4(b7, b8, b11, b12)
    return b9
