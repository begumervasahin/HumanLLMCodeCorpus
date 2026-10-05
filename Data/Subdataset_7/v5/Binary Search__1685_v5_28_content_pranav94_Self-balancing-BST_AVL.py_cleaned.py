from BST import BST
from TreeNode import TreeNode
class class1(TreeNode):
    def fonk1(self, b8):
        super().fonk1(b8)
        self.a1 = 0
class class2(BST):
    def fonk2(self, node):
        b1 = node.b4
        b2 = b1.b3
        b1.b3 = node
        node.b4 = b2
        self.fonk9(node)
        self.fonk9(b1)
        return b1
    def fonk3(self, node):
        b1 = node.b3
        b5 = b1.b4
        b1.b4 = node
        node.b3 = b5
        self.fonk9(node)
        self.fonk9(b1)
        return b1
    def fonk4(self, node):
        b6 = self.fonk11(node)
        if b6 > 1:
            if self.fonk11(node.b3) >= 0:
                return self.fonk3(node)
            node.b3 = self.fonk2(node.b3)
            return self.fonk3(node)
        if b6 < -1:
            if self.fonk11(node.b4) <= 0:
                return self.fonk2(node)
            node.b4 = self.fonk3(node.b4)
            return self.fonk2(node)
        return node
    def fonk5(self, node, b8):
        if not node:
            return class1(b8)
        if b8 < node.b8:
            node.b3 = self.fonk5(node.b3, b8)
        else:
            node.b4 = self.fonk5(node.b4, b8)
        self.fonk9(node)
        return self.fonk4(node)
    def fonk6(self, b8):
        self.b7 = self.fonk5(self.b7, b8)
    def fonk7(self, node, b8):
        if not node:
            return None
        if b8 < node.b8:
            node.b3 = self.fonk7(node.b3, b8)
        elif b8 > node.b8:
            node.b4 = self.fonk7(node.b4, b8)
        else:
            if not node.b3 and not node.b4:
                return None
            elif not node.b3:
                if node.b4:
                    node.b8 = node.b4.b8
                return node.b4
            elif not node.b4:
                return node.b3
            else:
                b9 = self.predecessor(node)
                b10 = b9.b8
                node.b3 = self.fonk7(node.b3, b10)
                node.b8 = b10
        self.fonk9(node)
        return self.fonk4(node)
    def fonk8(self,  b8):
        self.b7 = self.fonk7(self.b7, b8)
    def fonk9(self, node):
        node.a1 = 1 + max(self.fonk10(node.b3), self.fonk10(node.b4))
    @staticmethod
    def fonk10(node):
        if not node:
            return 0
        return node.a1
    def fonk11(self, node):
        if not node:
            return 0
        return self.fonk10(node.b3) - self.fonk10(node.b4)