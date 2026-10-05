from Node import Node
class class1:
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
        self.fonk2()
    def fonk2(self):
        self.b3 = [self.b1[0]]
    def fonk3(self):
        return self.b3.pop(0)
    def fonk4(self):
        return len(self.b3)
    def fonk5(self, b4):
        for node in self.b1:
            if node.b4 = = b4:
                return node
    def fonk6(self, b5):
        if b5 = = self.b2:
            raise Exception("City found: %s" % b5)
    def fonk7(self):
        pass
    def fonk8(self, node):
        b6 = node.get_children_nodes()
        for child in b6:
            b7 = self.fonk5(child.b4)
            if isinstance(b7, Node):
                self.fonk9(b7)
    def fonk9(self, node):
        self.b3.append(node)