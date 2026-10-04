from Shape import *
import newick
class PhyloTree(Shape):
    def __init__(self, leaf, children):
        super().__init__(children)
        self.leaf = leaf
        assert not self.is_leaf or (leaf is not None), "Leaf nodes must have a label."
    def shape(self):
        """
        Return the `Shape` associated with this `PhyloTree`, "forgetting" the labels of the leaves.
        :return: `Shape` instance.
        Return a tuple representing the simplified Newick code of this `PhyloTree`.
        :return: Tuple instance.
        Yield the labels of the leaves of this `PhyloTree`.
        :return: Generator yielding leaf labels.
        Return a list of labels that appear in this `PhyloTree`, sorted lexicographically.
        :return: List of labels.
        Check if this `PhyloTree` is phylogenetic (i.e., has no repeated leaves).
        :return: `True` if phylogenetic, `False` otherwise.
    Create a `PhyloTree` object from a Newick code entered as a string.
    :param newick_str: A string representing a Newick code.
    :return: `PhyloTree` instance.
    Create a list of `PhyloTree` objects from a string containing multiple Newick codes.
    :param newick_str: A string representing a list of Newick codes.
    :return: List of `PhyloTree` instances.
    Create a `PhyloTree` object from a `Node` object.
    :param newick_node: A `Node` object from the `newick` module.
    :return: `PhyloTree` instance.
    Load a list of trees from a Newick-formatted file.
    :param filename: Path to the file containing Newick codes.
    :param encoding: File encoding (default is 'utf8').
    :param strip_comments: Flag to strip comments enclosed in square brackets (default is `False`).
    :param kwargs: Additional keyword arguments passed to `newick.read`.
    :return: List of `PhyloTree` instances.
    """
    newick_trees = newick.read(filename, encoding, strip_comments, **kwargs)
    return [newick_node_to_tree(tree) for tree in newick_trees]