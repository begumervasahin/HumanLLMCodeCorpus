import random
class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
        self.b4 = random.random()
    def fonk2(self):
        return str(self.b1)
class class2:
    def fonk3(self):
        self.b5 = None
        self.a1 = 0
    def fonk4(self, node):
        b6 = node.b3
        b7 = b6.b2
        b6.b2 = node
        b6.b2.b3 = b7
        return b6
    def fonk5(self, node):
        b6 = node.b2
        b7 = b6.b3
        b6.b3 = node
        b6.b3.b2 = b7
        return b6
    def fonk6(self, e):
        self.a1 += 1
        if self.b5 is None:
            self.b5 = class1(e)
        else:
            self.b5 = self.fonk7(e, self.b5)
    def fonk7(self, e, ref_node):
        if ref_node is None:
            return class1(e)
        elif e < ref_node.b1:
            ref_node.b2 = self.fonk7(e, ref_node.b2)
            if ref_node.b2.b4 > ref_node.b4:
                return self.fonk5(ref_node)
        else:
            ref_node.b3 = self.fonk7(e, ref_node.b3)
            if ref_node.b3.b4 > ref_node.b4:
                return self.fonk4(ref_node)
        return ref_node
    def fonk8(self, element):
        return self.fonk9(self.b5, element)
    def fonk9(self, ref_node, element):
        if ref_node is None:
            return False
        elif ref_node.b1 = = element:
            return True
        if element < ref_node.b1:
            return self.fonk9(ref_node.b2, element)
        elif element > ref_node.b1:
            return self.fonk9(ref_node.b3, element)
        else:
            return False
    def fonk10(self):
        return self.fonk11(self.b5)
    def fonk11(self, node):
        if node is None:
            return 0
        else:
            return 1 + max(self.fonk11(node.b2), self.fonk11(node.b3))
    def fonk12(self):
        return self.a1