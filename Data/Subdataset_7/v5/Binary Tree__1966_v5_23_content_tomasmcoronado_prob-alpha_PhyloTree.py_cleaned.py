from Shape import Shape
import newick
class class1(Shape):
    def fonk1(self, b1 = None, children=None):
        super().fonk1(children)
        self.b1 = b1
        assert not self.is_leaf or (b1 is not None)
    def fonk2(self):
        if self.is_leaf:
            return Shape(None)
        else:
            return Shape([x.fonk2() for x in self.children])
    def fonk3(self):
        if self.is_leaf:
            return self.b1
        else:
            return tuple(x.fonk3() for x in self.children)
    def fonk4(self):
        if self.is_leaf:
            yield self.b1
        else:
            for x in self.children:
                for l in x.fonk4():
                    yield l
    def fonk5(self):
        return sorted(list(self.fonk4()))
    def fonk6(self):
        b2 = self.fonk5()
        return len(b2) == len(set(b2))
def fonk7(X):
    return fonk9(newick.loads(X)[0])
def fonk8(X):
    return [fonk9(n) for n in newick.loads(X)]
def fonk9(node):
    if not node.descendants:
        return class1(node.name)
    return class1(None, sorted([fonk9(x) for x in node.descendants]))
def fonk10(fname, b3 = 'utf8', strip_comments=False, **kwargs):
    b4 = newick.read(fname, b3, strip_comments, **kwargs)
    return [fonk9(node) for node in b4]