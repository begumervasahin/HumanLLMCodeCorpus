from Shape import *
import newick
class class1(Shape):
    def fonk1(self, b1, children):
        super().fonk1(children)
        self.b1 = b1
        assert not self.is_leaf or (b1 is not None), "Leaf nodes must have a label."
    def fonk2(self):
        """
        Return the `Shape` associated with this `class1`, "forgetting" the labels of the leaves.
        :return: `Shape` instance.
        Return a tuple representing the simplified Newick code of this `class1`.
        :return: Tuple instance.
        Yield the labels of the leaves of this `class1`.
        :return: Generator yielding b1 labels.
        Return a list of labels that appear in this `class1`, sorted lexicographically.
        :return: List of labels.
        Check if this `class1` is phylogenetic (i.e., has no repeated leaves).
        :return: `True` if phylogenetic, `False` otherwise.
    Create a `class1` object from a Newick code entered as a string.
    :param newick_str: A string representing a Newick code.
    :return: `class1` instance.
    Create a list of `class1` objects from a string containing multiple Newick codes.
    :param newick_str: A string representing a list of Newick codes.
    :return: List of `class1` instances.
    Create a `class1` object from a `Node` object.
    :param newick_node: A `Node` object from the `newick` module.
    :return: `class1` instance.
    Load a list of trees from a Newick-formatted file.
    :param filename: Path to the file containing Newick codes.
    :param encoding: File encoding (default is 'utf8').
    :param strip_comments: Flag to strip comments enclosed in square brackets (default is `False`).
    :param kwargs: Additional keyword arguments passed to `newick.read`.
    :return: List of `class1` instances.
    """
    b2 = newick.read(filename, encoding, strip_comments, **kwargs)
    return [newick_node_to_tree(tree) for tree in b2]