def fonk1(edges):
    b1 = []
    for i in edges:
        if i[0] not in b1:
            b1.append(i[0])
        if i[1] not in b1:
            b1.append(i[1])
    return b1
class class1:
    def fonk2(self):
        self.b2 = []
        self.b3 = []
        self.b4 = {}
    def fonk3(self, n):
        self.b2.append(n)
    def fonk4(self, arrow, dist):
        self.b3.append(arrow)
        self.b4[arrow] = dist
    def fonk5(self, node):
        b5 = []
        for i in self.b3:
            if i[1] == node:
                b5.append(i[0])
            elif i[0] == node:
                b5.append(i[1])
        return b5
    def fonk6(self, node1, node2):
        if (node1, node2) in self.b3:
            return self.b4[(node1, node2)]
        elif (node2, node1) in self.b3:
            return self.b4[(node2, node1)]
        return None
    def fonk7(self, node):
        b6 = float('inf')
        b7 = None
        for i in self.b3:
            b8 = self.fonk6(i[0], i[1])
            if i[1] == node and b8 < b6:
                b6 = b8
                b7 = i[0]
            elif i[0] == node and b8 < b6:
                b6 = b8
                b7 = i[1]
        return [b7, b6]
    def fonk8(self, arrowlist):
        b9 = []
        b10 = set(self.b3) - set(arrowlist)
        b11 = fonk1(arrowlist)
        b12 = []
        for k in b10:
            if (k[1] in b11) and (k[0] in b11):
                b12.append(k)
        b10 = b10 - set(b12)
        for i in b10:
            for j in arrowlist:
                if (i[0] == j[0]) or (i[0] == j[1]) or (i[1] == j[0]) or (i[1] == j[1]):
                    b9.append(i)
        return b9
if b13 = = "__main__":
    b14 = class1()
    b14.fonk3('A')
    b14.fonk3('B')
    b14.fonk3('C')
    b14.fonk4(('A', 'B'), 5)
    b14.fonk4(('B', 'C'), 10)
    b14.fonk4(('A', 'C'), 15)
    print("Neighbors of B:", b14.fonk5('B'))
    print("Length between A and B:", b14.fonk6('A', 'B'))
    print("Closest neighbor of A:", b14.fonk7('A'))
    print("Edges near [('A', 'B')]:", b14.fonk8([('A', 'B')]))