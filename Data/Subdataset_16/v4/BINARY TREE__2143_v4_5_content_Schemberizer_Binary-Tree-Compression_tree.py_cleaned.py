from Node import Node
class class1:
    def fonk1(self):
        self.b1 = None
        self.b2 = []
    def fonk2(self):
        return self.b1 is None
    def fonk3(self):
        return self.fonk4(self.b1)
    def fonk4(self, node):
        if not node:
            return 0
        return 1 + self.fonk4(node.get_left()) + self.fonk4(node.get_right())
    def fonk5(self):
        return self.fonk6(self.b1)
    def fonk6(self, node):
        if not node:
            return 0
        return 1 + max(self.fonk6(node.get_left()), self.fonk6(node.get_right()))
    def fonk7(self, query):
        b3 = Node(query)
        if not self.b2:
            self.fonk8(self.b1, "")
            self.b2 = sorted(self.b2, key=lambda x: x.get_datum()[1], reverse=True)
        for node in self.b2:
            if node.get_datum()[0] == b3.get_datum():
                return node.get_datum()[2]
        return "error"
    def fonk8(self, node, path):
        if node.get_datum()[0] == '':
            if node.get_left():
                self.fonk8(node.get_left(), path + "0")
            if node.get_right():
                self.fonk8(node.get_right(), path + "1")
        if not node.get_right() and not node.get_left():
            node.datum.append(path)
            self.b2.append(node)
    def fonk9(self, bit):
        return self.fonk10(self.b1, bit)
    def fonk10(self, node, bit):
        if len(bit) > 0:
            if bit[0] == "0":
                if node.get_left():
                    return self.fonk10(node.get_left(), bit[1:])
                else:
                    return node.get_datum()[0], bit
            if bit[0] == "1":
                if node.get_right():
                    return self.fonk10(node.get_right(), bit[1:])
                else:
                    return node.get_datum()[0], bit
        return node.get_datum()[0], bit
    def fonk11(self, b5):
        if isinstance(b5[0], list):
            b4 = [Node(item) for item in b5]
            b5 = b4
        if len(b5) > 1:
            b6 = Node(['', b5[0].get_datum()[1] + b5[1].get_datum()[1]])
            b6.insert_left(b5[0])
            b6.insert_right(b5[1])
            b5.append(b6)
            b5 = sorted(b5[2:], key=lambda x: x.get_datum()[1])
            self.fonk11(b5)
        else:
            self.b1 = b5[0]
    def fonk12(self):
        self.fonk13(self.b1)
        print()
    def fonk13(self, node):
        if node.get_left():
            self.fonk13(node.get_left())
        print(node.get_datum(), b7 = " ")
        if node.get_right():
            self.fonk13(node.get_right())
if b8 = = "__main__":
    b9 = class1()
    b9.fonk11([['a', 1], ['b', 1], ['c', 1], ['d', 2], ['e', 6], ['f', 10], ['g', 15]])
    b10 = b9.fonk7('c')
    b11 = b9.fonk7('a')
    b12 = str(b10 + b11)
    print(b12)
    while b12:
        char, b12 = b9.fonk9(b12)
        print(char, b7 = "")