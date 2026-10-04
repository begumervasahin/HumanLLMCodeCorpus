def fonk1(edges):
    b1 = []
    for i in edges:
        if i[0] not in b1:
            b1.append(i[0])
        if i[1] not in b1:
            b1.append(i[1])
    return b1
class class1():
    def fonk2(self):
        self.b2 = []
        self.b3 = []
        self.b4 = {}
    def fonk3(self,n):
        self.b2.append(n)
    def fonk4(self,arrow,dist):
        self.b3.append(arrow)
        self.b4[arrow] = dist
    def fonk5(self,node):
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
    def fonk7(self, node):
        a1 = 10e3
        b6 = None
        for i in self.b3:
            b7 = self.fonk6(i[0],i[1])
            if i[1] == node and b7 < a1:
                a1 = b7
                b6 = i[0]
            elif i[0] == node and b7 < a1:
                a1 = b7
                b6 = i[1]
        return [b6, a1]
    def fonk8(self,arrowlist):
        b8 = []
        b9 = set(self.b3)-set(arrowlist)
        b10 = fonk1(arrowlist)
        b11 = []
        for k in b9:
            if (k[1] in b10) and (k[0] in b10):
                b11.append(k)
        b9 = b9 - set(b11)
        for i in b9:
            for j in arrowlist:
                if (i[0] == j[0]) or (i[0] == j[1]) or (i[1] == j[0]) or (i[1] == j[1]):
                    b8.append(i)
        return b8