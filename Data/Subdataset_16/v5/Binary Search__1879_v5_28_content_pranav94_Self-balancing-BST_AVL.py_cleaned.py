from BST import BST
from TreeNode import TreeNode
class class1(TreeNode):
    def fonk1(self, b7):
        super().fonk1(b7)
        self.a1 = 1
class class2(BST):
    def fonk2(self, node):
        b1 = node.b2
        node.b2 = b1.b3
        b1.b3 = node
        self.fonk9(node)
        self.fonk9(b1)
        return b1
    def fonk3(self, node):
        b1 = node.b3
        node.b3 = b1.b2
        b1.b2 = node
        self.fonk9(node)
        self.fonk9(b1)
        return b1
    def fonk4(self, node):
        b4 = self.fonk11(node)
        if b4 > 1:
            if self.fonk11(node.b3) >= 0:
                return self.fonk3(node)
            else:
                node.b3 = self.fonk2(node.b3)
                return self.fonk3(node)
        if b4 < -1:
            if self.fonk11(node.b2) <= 0:
                return self.fonk2(node)
            else:
                node.b2 = self.fonk3(node.b2)
                return self.fonk2(node)
        return node
    def fonk5(self, node, b7):
        if not node:
            return class1(b7)
        if b7 < node.b7:
            node.b3 = self.fonk5(node.b3, b7)
        else:
            node.b2 = self.fonk5(node.b2, b7)
        self.fonk9(node)
        return self.fonk4(node)
    def fonk6(self, b7):
        self.b5 = self.fonk5(self.b5, b7)
    def fonk7(self, node, b7):
        if not node:
            return None
        if b7 < node.b7:
            node.b3 = self.fonk7(node.b3, b7)
        elif b7 > node.b7:
            node.b2 = self.fonk7(node.b2, b7)
        else:
            if not node.b3 and not node.b2:
                return None
            elif not node.b3:
                return node.b2
            elif not node.b2:
                return node.b3
            else:
                b6 = self.fonk12(node)
                node.b7 = b6.b7
                node.b3 = self.fonk7(node.b3, b6.b7)
        self.fonk9(node)
        return self.fonk4(node)
    def fonk8(self, b7):
        self.b5 = self.fonk7(self.b5, b7)
    def fonk9(self, node):
        node.a1 = 1 + max(self.fonk10(node.b3), self.fonk10(node.b2))
    @staticmethod
    def fonk10(node):
        return node.a1 if node else 0
    def fonk11(self, node):
        return self.fonk10(node.b3) - self.fonk10(node.b2) if node else 0
    def fonk12(self, node):
        b8 = node.b3
        while b8.b2:
            b8 = b8.b2
        return b8