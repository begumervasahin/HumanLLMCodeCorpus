class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = []
    def fonk2(self, destination, b5):
        self.b2.append(class2(self.b1, destination, b5))
    def fonk3(self):
        return self.b1
    def fonk4(self):
        return self.b2
    def fonk5(self, destination):
        for edge in self.b2:
            if edge.fonk8() == destination:
                return edge
        return None
class class2:
    def fonk6(self, b3, b4, b5):
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
    def fonk7(self):
        return self.b3
    def fonk8(self):
        return self.b4
    def fonk9(self):
        return self.b5
    def fonk10(self, other):
        return self.b5 < other.b5
class class3:
    def fonk11(self):
        self.b6 = {}
        self.b2 = []
    def fonk12(self, b1):
        if b1 not in self.b6:
            self.b6[b1] = class1(b1)
    def fonk13(self, b3, b4, b5):
        if b3 in self.b6 and b4 in self.b6:
            self.b6[b3].fonk13(b4, b5)
            self.b6[b4].fonk13(b3, b5)
            self.b2.append(class2(b3, b4, b5))
    def fonk14(self):
        return list(self.b6.keys())
    def fonk15(self, b1):
        return self.b6.get(b1)
    def fonk16(self):
        return sorted(self.b2)
class class4:
    def fonk17(self, b14):
        b7 = class3()
        b8 = b14.fonk14()
        for b1 in b8:
            b7.fonk12(b1)
        b2 = b14.fonk16()
        for edge in b2:
            if not self.fonk18(b7, edge):
                b7.fonk13(edge.fonk7(), edge.fonk8(), edge.fonk9())
        return b7
    def fonk18(self, b14, edge_to_check):
        b9 = {}
        b10 = {}
        def fonk19(vertex):
            if b9[vertex] != vertex:
                b9[vertex] = fonk19(b9[vertex])
            return b9[vertex]
        def fonk20(vertex1, vertex2):
            b11 = fonk19(vertex1)
            b12 = fonk19(vertex2)
            if b11 != b12:
                if b10[b11] > b10[b12]:
                    b9[b12] = b11
                elif b10[b11] < b10[b12]:
                    b9[b11] = b12
                else:
                    b9[b12] = b11
                    b10[b11] += 1
        for node in b14.fonk14():
            b9[node] = node
            b10[node] = 0
        for edge in b14.fonk16():
            b11 = fonk19(edge.fonk7())
            b12 = fonk19(edge.fonk8())
            if b11 != b12:
                fonk20(b11, b12)
        b11 = fonk19(edge_to_check.fonk7())
        b12 = fonk19(edge_to_check.fonk8())
        return b11 = = b12
if b13 = = "__main__":
    b14 = class3()
    b14.fonk12("A")
    b14.fonk12("B")
    b14.fonk12("C")
    b14.fonk12("D")
    b14.fonk13("A", "B", 1)
    b14.fonk13("A", "C", 3)
    b14.fonk13("B", "C", 1)
    b14.fonk13("B", "D", 4)
    b14.fonk13("C", "D", 2)
    b15 = class4()
    b7 = b15.fonk17(b14)
    print("Minimum Spanning Tree:")
    for node_name in b7.fonk14():
        b2 = b7.fonk15(node_name).fonk16()
        for edge in b2:
            print(f"{edge.fonk7()} -- {edge.fonk8()} == {edge.fonk9()}")