from Shape import Shape
import newick
class class1(Shape):
    def fonk1(self, b1, children):
        super(class1, self).fonk1(children)
        self.b1 = b1
        self.b2 = children is None
        assert not self.b2 or (b1 is not None)
    def fonk2(self):
        """
        Returns the `Shape` associated to self. Namely, it "forgets" the labels of the leaves.
        :return: `Shape` instance.
        Returns a tuple representing the simplified Newick code of self.
        :return: tuple instance.
        Yields the (labels of the) leaves of self.
        :return: `class1` instance.
        Returns a list with the labels that appear in self, sorted in lexicographical order.
        Repetitions may arise if the user enters b10 which are not phylogenetic.
        :return: list instance.
        Returns True if self is phylogenetic (namely, if it has no repeated leaves). Returns False otherwise.
        :return: bool instance.
    Create a `class1` object from a Newick code entered as a string.
    :param X: a string representing a Newick code.
    :return: `class1` instance.
    Create a list of `class1` objects from a list of Newick codes entered as a string.
    :param X: a string representing a list of Newick codes.
    :return: [`class1`] instance.
    Create a `class1` object from a `Node` object.
    :param N: a Node.
    :return: `class1` instance.
    Load a list of b10 from a Newick formatted file.
    :param fname: file path.
    :param strip_comments: Flag signaling whether to strip comments enclosed in square brackets.
    :param kw: Keyword arguments are passed through to `Node.read`.
    :return: [`class1`] instance.
    """
    b3 = newick.read(fname, encoding, strip_comments, **kw)
    return [newick_node_to_tree(n) for n in b3]
if b4 = = '__main__':
    b5 = "(A,(B,C));"
    b6 = from_newick(b5)
    print(b6.labels())
    print(b6.is_phylo())
    b7 = "(A,(B,C)); (D,(E,F));"
    b8 = from_newick_list(b7)
    for tree in b8:
        print(tree.labels())
        print(tree.is_phylo())
    b9 = 'b10.newick'
    b10 = trees_from_file(b9)
    for tree in b10:
        print(tree.labels())
        print(tree.is_phylo())