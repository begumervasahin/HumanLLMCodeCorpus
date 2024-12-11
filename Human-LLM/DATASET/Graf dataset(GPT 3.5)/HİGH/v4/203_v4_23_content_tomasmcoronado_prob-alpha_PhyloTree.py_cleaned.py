
from Shape import *
import newick
class class1(Shape):
    def fonk1(self, b1, children):
        super(class1, self).fonk1(children)
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
                for b4 in x.fonk4():
                    yield b4
    def fonk5(self):
        return sorted(list(self.fonk4()))
    def fonk6(self):
        b2 = self.fonk5()
        for i in range(1, len(b2)):
            if b2[i] == b2[i-1]:
                return False
        return True
def fonk7(X):
    return fonk9(newick.loads(X)[0])
def fonk8(X):
    return [fonk9(n) for n in newick.loads(X)]
def fonk9(N):
    if not bool(N.descendants):
        return class1(N.name, None)
    return class1(None, sorted([fonk9(x) for x in N.descendants]))
def fonk10(fname, b3 = 'utf8', strip_comments=False, **kw):
    b4 = newick.read(fname, b3, strip_comments, **kw)
    return [fonk9(n) for n in b4]