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
        for i in range(1, len(b2)):
            if b2[i] == b2[i - 1]:
                return False
        return True
def fonk7(newick_str):
    return fonk9(newick.loads(newick_str)[0])
def fonk8(newick_list):
    return [fonk9(n) for n in newick.loads(newick_list)]
def fonk9(node):
    if not bool(node.descendants):
        return class1(node.name, None)
    return class1(None, sorted([fonk9(x) for x in node.descendants]))
def fonk10(file_path, b3 = 'utf8', strip_comments=False, **kwargs):
    b4 = newick.read(file_path, b3, strip_comments, **kwargs)
    return [fonk9(node) for node in b4]
def fonk11():
    b5 = "(A, (B, C));"
    b6 = fonk7(b5)
    print("Labels:", b6.fonk5())
    print("Is phylogenetic:", b6.fonk6())
if b7 = = "__main__":
    fonk11()