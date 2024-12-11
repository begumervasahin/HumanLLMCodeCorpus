from Node import Node
class class1:
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
        self.fonk2()
    def fonk2(self):
        self.b3 = []
        self.b3.append(self.b1[0])
    def fonk3(self):
        return self.b3.pop(0)
    def fonk4(self):
        return len(self.b3)
    def fonk5(self, b4):
        for node in self.b1:
            if node.b4 = = b4:
                return node
    def fonk6(self):
        if self.fonk4() == 0:
            raise Exception("The b3 is empty")
    def fonk7(self, b5):
        if b5 = = self.b2:
            raise Exception("City found: %s" % b5)
    def fonk8(self):
        pass
    def fonk9(self, node):
        b6 = node.get_children_nodes()
        for child in b6:
            b7 = self.fonk5(child.b4)
            if isinstance(b7, Node):
                self.add_queue(b7)
if b8 = = "__main__":
    b9 = Node("b9")
    b10 = Node("b10")
    b11 = Node("b11")
    b12 = Node("b12")
    b13 = Node("b13")
    b14 = Node("b14")
    b15 = Node("b15")
    b16 = Node("b16")
    b17 = Node("b17")
    b18 = Node("b18")
    b9.add_child(b10)
    b9.add_child(b11)
    b9.add_child(b12)
    b10.add_child(b13)
    b10.add_child(b14)
    b11.add_child(b14)
    b12.add_child(b14)
    b12.add_child(b17)
    b13.add_child(b15)
    b14.add_child(b18)
    b14.add_child(b16)
    b15.add_child(b18)
    b16.add_child(b18)
    b17.add_child(b18)
    b19 = class1([b9, b10, b11, b12, b13, b14, b15, b16, b17, b18], "b18")
    try:
        b19.fonk8()
    except Exception as e:
        print(e)