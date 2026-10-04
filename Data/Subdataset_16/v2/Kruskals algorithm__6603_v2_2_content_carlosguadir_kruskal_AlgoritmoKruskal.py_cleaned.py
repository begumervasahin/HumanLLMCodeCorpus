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
        for b10 in self.b2:
            if b10.fonk8() == destination:
                return b10
        return -1
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
        return self.b6[b1]
    def fonk16(self):
        return sorted(self.b2, b7 = lambda b10: b10.fonk9())
class class4:
    def fonk17(self, b13):
        b8 = class3()
        b9 = b13.fonk14()
        for b1 in b9:
            b8.fonk12(b1)
        b2 = b13.fonk16()
        while b2:
            b10 = b2.pop(0)
            if not self.fonk18(b8, b10, b8.fonk15(b10.fonk8()), b10.fonk8()):
                b8.fonk13(b10.fonk7(), b10.fonk8(), b10.fonk9())
        return b8
    def fonk18(self, b13, edge_to_check, terminal_node, last_node_name):
        b2 = terminal_node.fonk16()
        if not b2:
            return False
        if terminal_node.fonk5(edge_to_check.fonk7()) != -1:
            return True
        for b10 in b2:
            b11 = b13.fonk15(b10.fonk8())
            if b11.fonk3() != last_node_name:
                if self.fonk18(b13, edge_to_check, b11, terminal_node.fonk3()):
                    return True
        return False
if b12 = = "__main__":
    b13 = class3()
    b13.fonk12("A")
    b13.fonk12("B")
    b13.fonk12("C")
    b13.fonk12("D")
    b13.fonk13("A", "B", 1)
    b13.fonk13("A", "C", 3)
    b13.fonk13("B", "C", 1)
    b13.fonk13("B", "D", 4)
    b13.fonk13("C", "D", 2)
    b14 = class4()
    b8 = b14.fonk17(b13)
    print("Minimum Spanning Tree:")
    for node_name in b8.fonk14():
        b2 = b8.fonk15(node_name).fonk16()
        for b10 in b2:
            print(f"{b10.fonk7()} -- {b10.fonk8()} == {b10.fonk9()}")