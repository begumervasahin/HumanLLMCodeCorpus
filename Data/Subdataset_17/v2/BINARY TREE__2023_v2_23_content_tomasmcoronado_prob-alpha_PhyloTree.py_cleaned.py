from Shape import Shape
import newick
class PhyloTree(Shape):
    def __init__(self, leaf, children):
        super().__init__(children)
        self.leaf = leaf
        self.is_leaf = children is None
        assert not self.is_leaf or (leaf is not None), "Leaf must have a label."
    def shape(self):
        if self.is_leaf:
            return Shape(None)
        return Shape([child.shape() for child in self.children])
    def to_newick_tuple(self):
        if self.is_leaf:
            return self.leaf
        return tuple(child.to_newick_tuple() for child in self.children)
    def leaves(self):
        if self.is_leaf:
            yield self.leaf
        else:
            for child in self.children:
                yield from child.leaves()
    def labels(self):
        return sorted(self.leaves())
    def is_phylo(self):
        labels = self.labels()
        return len(labels) == len(set(labels))
def from_newick(newick_str):
    return newick_node_to_tree(newick.loads(newick_str)[0])
def from_newick_list(newick_list_str):
    return [newick_node_to_tree(node) for node in newick.loads(newick_list_str)]
def newick_node_to_tree(node):
    if not node.descendants:
        return PhyloTree(node.name, None)
    return PhyloTree(None, sorted(newick_node_to_tree(desc) for desc in node.descendants))
def trees_from_file(fname, encoding='utf8', strip_comments=False, **kwargs):
    nodes = newick.read(fname, encoding, strip_comments, **kwargs)
    return [newick_node_to_tree(node) for node in nodes]
if __name__ == '__main__':
    newick_str = "(A,(B,C));"
    phylo_tree = from_newick(newick_str)
    print(phylo_tree.labels())
    print(phylo_tree.is_phylo())
    newick_list_str = "(A,(B,C)); (D,(E,F));"
    phylo_trees = from_newick_list(newick_list_str)
    for tree in phylo_trees:
        print(tree.labels())
        print(tree.is_phylo())
    filename = 'trees.newick'
    trees = trees_from_file(filename)
    for tree in trees:
        print(tree.labels())
        print(tree.is_phylo())