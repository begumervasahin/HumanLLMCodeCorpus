def fonk1(edges):
    b1 = set()
    for edge in edges:
        b1.update(edge)
    return list(b1)
class class1:
    def fonk2(self):
        self.b1 = []
        self.b2 = []
        self.b3 = {}
    def fonk3(self, node):
        if node not in self.b1:
            self.b1.append(node)
    def fonk4(self, arrow, dist):
        if arrow not in self.b2:
            self.b2.append(arrow)
            self.b3[arrow] = dist
    def fonk5(self, node):
        b4 = []
        for arrow in self.b2:
            if arrow[0] == node:
                b4.append(arrow[1])
            elif arrow[1] == node:
                b4.append(arrow[0])
        return b4
    def fonk6(self, node1, node2):
        if (node1, node2) in self.b3:
            return self.b3[(node1, node2)]
        elif (node2, node1) in self.b3:
            return self.b3[(node2, node1)]
        return None
    def fonk7(self, node):
        b5 = float('inf')
        b6 = None
        for arrow in self.b2:
            b7 = self.fonk6(arrow[0], arrow[1])
            if (arrow[0] == node or arrow[1] == node) and b7 < b5:
                b5 = b7
                b6 = arrow[1] if arrow[0] == node else arrow[0]
        return [b6, b5]
    def fonk8(self, arrow_list):
        b8 = []
        b9 = set(self.b2) - set(arrow_list)
        b10 = fonk1(arrow_list)
        b11 = {arrow for arrow in b9 if not (arrow[0] in b10 and arrow[1] in b10)}
        for arrow in b11:
            if any(node in b10 for node in arrow):
                b8.append(arrow)
        return b8
if b12 = = "__main__":
    b13 = class1()
    b13.fonk3('A')
    b13.fonk3('B')
    b13.fonk3('C')
    b13.fonk4(('A', 'B'), 5)
    b13.fonk4(('B', 'C'), 10)
    b13.fonk4(('A', 'C'), 15)
    print("Neighbors of B:", b13.fonk5('B'))
    print("Length between A and B:", b13.fonk6('A', 'B'))
    print("Closest neighbor of A:", b13.fonk7('A'))
    print("Edges near [('A', 'B')]:", b13.fonk8([('A', 'B')]))