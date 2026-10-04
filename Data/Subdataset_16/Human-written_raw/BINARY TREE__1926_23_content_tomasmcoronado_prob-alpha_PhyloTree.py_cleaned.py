
from Shape import *
import newick
class class1(Shape):
    def fonk1(self, b1, children):
        super(class1, self).fonk1(children)
        self.b1 = b1
        assert not self.is_leaf or (b1 is not None)
    def fonk2(self):
        """
        Returns the `Shape` associated to self. Namely, it "forgets" the labels of the leafs.
        :return: `Shape` instance.
        Returns a tuple representing the simplified Newick code of self.
        :return: tuple instance.
        Yields the (labels of the) leaves of self.
        :return: `class1` instance.
        Returns a list with the labels that appear in self, sorted in lexicographical order.
        Repetitions may arise if the user enters trees which are not phylogenetic.
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
    Load a list of trees from a Newick formatted file.
    :param fname: file path.
    :param strip_comments: Flag signaling whether to strip comments enclosed in square \
    brackets.
    :param kw: Keyword arguments are passed through to `Node.read`.
    :return: [`class1`] instance.
    """
    b2 = newick.read(fname, encoding, strip_comments, **kw)
    return [newick_node_to_tree(n) for n in b2]