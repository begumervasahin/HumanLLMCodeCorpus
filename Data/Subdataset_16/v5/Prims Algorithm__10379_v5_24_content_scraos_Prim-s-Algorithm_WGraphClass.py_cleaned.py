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
    def fonk4(self, arrow, b8):
        self.b2.append(arrow)
        self.b3[arrow] = b8
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
            if node in arrow:
                b7 = arrow[1] if arrow[0] == node else arrow[0]
                b8 = self.b3[arrow]
                if b8 < b5:
                    b5 = b8
                    b6 = b7
        return b6, b5
    def fonk8(self, arrow_list):
        b9 = []
        b10 = set(self.b2) - set(arrow_list)
        b11 = set(fonk1(arrow_list))
        b10 = {edge for edge in b10 if not (edge[0] in b11 and edge[1] in b11)}
        for edge in b10:
            if any(set(edge) & set(arrow) for arrow in arrow_list):
                b9.append(edge)
        return b9