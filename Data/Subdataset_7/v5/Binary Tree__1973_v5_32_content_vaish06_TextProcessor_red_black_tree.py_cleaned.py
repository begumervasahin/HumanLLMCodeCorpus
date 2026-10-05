from binary_search_tree import TreeMap
class class1(TreeMap):
    class class2(TreeMap.class2):
        b1 = 'b3'
        def fonk1(self, element, b2 = None, left=None, right=None):
            super().fonk1(element, b2, left, right)
            self.b3 = True
    def fonk2(self, node):
        node._node.b3 = True
    def fonk3(self, node):
        node._node.b3 = False
    def fonk4(self, node, make_red):
        node._node.b3 = make_red
    def fonk5(self, node):
        return node is not None and node._node.b3
    def fonk6(self, node):
        return self.fonk5(node) and self.is_leaf(node)
    def fonk7(self, node):
        for b8 in (self.left(node), self.right(node)):
            if self.fonk5(b8):
                return b8
        return None
    def fonk8(self, node):
        self.fonk9(node)
    def fonk9(self, node):
        if self.is_root(node):
            self.fonk3(node)
        else:
            b2 = self.b2(node)
            if self.fonk5(b2):
                b4 = self.sibling(b2)
                if not self.fonk5(b4):
                    b5 = self._restructure(node)
                    self.fonk3(b5)
                    self.fonk2(self.left(b5))
                    self.fonk2(self.right(b5))
                else:
                    b6 = self.b2(b2)
                    self.fonk2(b6)
                    self.fonk3(self.left(b6))
                    self.fonk3(self.right(b6))
                    self.fonk9(b6)
    def fonk10(self, node):
        if len(self) == 1:
            self.fonk3(self.root())
        elif node is not None:
            b7 = self.num_children(node)
            if b7 = = 1:
                b8 = next(self.children(node))
                if not self.fonk6(b8):
                    self.fonk11(node, b8)
            elif b7 = = 2:
                if self.fonk6(self.left(node)):
                    self.fonk3(self.left(node))
                else:
                    self.fonk3(self.right(node))
    def fonk11(self, b11, y):
        if not self.fonk5(y):
            b9 = self.fonk7(y)
            if b9 is not None:
                b10 = self.fonk5(b11)
                b5 = self._restructure(b9)
                self.fonk4(b5, b10)
                self.fonk3(self.left(b5))
                self.fonk3(self.right(b5))
            else:
                self.fonk2(y)
                if self.fonk5(b11):
                    self.fonk3(b11)
                elif not self.is_root(b11):
                    self.fonk11(self.b2(b11), self.sibling(b11))
        else:
            self._rotate(y)
            self.fonk3(y)
            self.fonk2(b11)
            if b11 = = self.right(y):
                self.fonk11(b11, self.left(b11))
            else:
                self.fonk11(b11, self.right(b11))