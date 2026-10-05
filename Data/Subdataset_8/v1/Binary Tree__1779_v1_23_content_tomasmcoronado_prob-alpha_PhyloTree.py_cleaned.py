from Shape import Shape
import newick
class PhyloTree(Shape):
    def __init__(self, leaf=None, children=None):
        super().__init__(children)
        self.leaf = leaf
        assert not self.is_leaf or (leaf is not None)
    def shape(self):
        if self.is_leaf:
            return Shape(None)
        else:
            return Shape([x.shape() for x in self.children])
    def to_newick_tuple(self):
        if self.is_leaf:
            return self.leaf
        else:
            return tuple(x.to_newick_tuple() for x in self.children)
    def leaves(self):
        if self.is_leaf:
            yield self.leaf
        else:
            for x in self.children:
                for l in x.leaves():
                    yield l
    def labels(self):
        return sorted(list(self.leaves()))
    def is_phylo(self):
        L = self.labels()
        for i in range(1, len(L)):
            if L[i] == L[i-1]:
                return False
        return True
def from_newick(X):
    return newick_node_to_tree(newick.loads(X)[0])
def from_newick_list(X):
    return [newick_node_to_tree(n) for n in newick.loads(X)]
def newick_node_to_tree(N):
    if not bool(N.descendants):
        return PhyloTree(N.name, None)
    return PhyloTree(None, sorted([newick_node_to_tree(x) for x in N.descendants]))
def trees_from_file(fname, encoding='utf8', strip_comments=False, **kw):
    l = newick.read(fname, encoding, strip_comments, **kw)
    return [newick_node_to_tree(n) for n in l]
def main():
    tree_str = "(A, (B, C));"
    phylo_tree = from_newick(tree_str)
    print("Labels:", phylo_tree.labels())
    print("Is phylogenetic:", phylo_tree.is_phylo())
if __name__ == "__main__":
    main()