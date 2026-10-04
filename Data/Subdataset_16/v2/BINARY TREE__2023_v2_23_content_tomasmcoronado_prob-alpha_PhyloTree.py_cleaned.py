from Shape import Shape
import newick
class class1(Shape):
    def fonk1(self, b1, children):
        super().fonk1(children)
        self.b1 = b1
        self.b2 = children is None
        assert not self.b2 or (b1 is not None), "Leaf must have a label."
    def fonk2(self):
        if self.b2:
            return Shape(None)
        return Shape([child.fonk2() for child in self.children])
    def fonk3(self):
        if self.b2:
            return self.b1
        return tuple(child.fonk3() for child in self.children)
    def fonk4(self):
        if self.b2:
            yield self.b1
        else:
            for child in self.children:
                yield from child.fonk4()
    def fonk5(self):
        return sorted(self.fonk4())
    def fonk6(self):
        b3 = self.fonk5()
        return len(b3) == len(set(b3))
def fonk7(b7):
    return fonk9(newick.loads(b7)[0])
def fonk8(b9):
    return [fonk9(node) for node in newick.loads(b9)]
def fonk9(node):
    if not node.descendants:
        return class1(node.name, None)
    return class1(None, sorted(fonk9(desc) for desc in node.descendants))
def fonk10(fname, b4 = 'utf8', strip_comments=False, **kwargs):
    b5 = newick.read(fname, b4, strip_comments, **kwargs)
    return [fonk9(node) for node in b5]
if b6 = = '__main__':
    b7 = "(A,(B,C));"
    b8 = fonk7(b7)
    print(b8.fonk5())
    print(b8.fonk6())
    b9 = "(A,(B,C)); (D,(E,F));"
    b10 = fonk8(b9)
    for tree in b10:
        print(tree.fonk5())
        print(tree.fonk6())
    b11 = 'b12.newick'
    b12 = fonk10(b11)
    for tree in b12:
        print(tree.fonk5())
        print(tree.fonk6())