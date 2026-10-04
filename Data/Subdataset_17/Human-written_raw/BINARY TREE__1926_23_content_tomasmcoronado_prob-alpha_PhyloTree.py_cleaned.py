
from Shape import *
import newick
class PhyloTree(Shape):
    def __init__(self, leaf, children):
        super(PhyloTree, self).__init__(children)
        self.leaf = leaf
        assert not self.is_leaf or (leaf is not None)
    def shape(self):
        """
        Returns the `Shape` associated to self. Namely, it "forgets" the labels of the leafs.
        :return: `Shape` instance.
        Returns a tuple representing the simplified Newick code of self.
        :return: tuple instance.
        Yields the (labels of the) leaves of self.
        :return: `PhyloTree` instance.
        Returns a list with the labels that appear in self, sorted in lexicographical order.
        Repetitions may arise if the user enters trees which are not phylogenetic.
        :return: list instance.
        Returns True if self is phylogenetic (namely, if it has no repeated leaves). Returns False otherwise.
        :return: bool instance.
    Create a `PhyloTree` object from a Newick code entered as a string.
    :param X: a string representing a Newick code.
    :return: `PhyloTree` instance.
    Create a list of `PhyloTree` objects from a list of Newick codes entered as a string.
    :param X: a string representing a list of Newick codes.
    :return: [`PhyloTree`] instance.
    Create a `PhyloTree` object from a `Node` object.
    :param N: a Node.
    :return: `PhyloTree` instance.
    Load a list of trees from a Newick formatted file.
    :param fname: file path.
    :param strip_comments: Flag signaling whether to strip comments enclosed in square \
    brackets.
    :param kw: Keyword arguments are passed through to `Node.read`.
    :return: [`PhyloTree`] instance.
    """
    l = newick.read(fname, encoding, strip_comments, **kw)
    return [newick_node_to_tree(n) for n in l]