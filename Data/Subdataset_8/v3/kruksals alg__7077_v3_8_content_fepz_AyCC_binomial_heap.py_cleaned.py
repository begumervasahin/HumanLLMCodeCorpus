class LinkError(Exception):
    pass
class EmptyBinomialHeapError(Exception):
    pass
class TreeItem:
    def __init__(self, key, value, tree):
        self.key = key
        self.value = value
        self.tree = tree
class BinomialTree:
    def __init__(self, key, value):
        self.rank = 0
        self.item = TreeItem(key, value, self)
        self.children = []
        self.parent = None
    def link(self, other_tree):
        if self.rank != other_tree.rank:
            raise LinkError("Cannot link trees with different ranks.")
        if self.item.key > other_tree.item.key:
            raise LinkError("Cannot link tree with lower priority as child.")
        self.children.append(other_tree)
        other_tree.parent = self
        self.rank += 1
    def decrease_key(self, new_key):
        node = self
        node.item.key = new_key
        parent = node.parent
        while parent is not None and node.item.key < parent.item.key:
            parent.item, node.item = node.item, parent.item
            parent.item.tree = parent
            node.item.tree = node
            node = parent
            parent = node.parent
        return node
    def __str__(self, indent=0):
        return (" " * indent +
                f"rank: {self.rank} key: {self.item.key} value: {self.item.value}" +
                "\n" + "".join(child.__str__(indent+2) for child in self.children))
class BinomialHeap:
    def __init__(self, infinity=float('inf')):
        self.infinity = infinity
        self.trees = []
        self.elements = 0
        self.min_key = self.infinity
        self.min_value = None
        self.min_tree_rank = -1
    def __capacity(self):
        return 2 ** len(self.trees) - 1
    def __resize(self):
        while self.__capacity() < self.elements:
            self.trees.append(None)
    def __add_tree(self, new_tree):
        self.elements += 2 ** new_tree.rank
        self.__resize()
        while self.trees[new_tree.rank] is not None:
            if self.trees[new_tree.rank].item.key < new_tree.item.key:
                new_tree, self.trees[new_tree.rank] = self.trees[new_tree.rank], new_tree
            r = new_tree.rank
            new_tree.link(self.trees[r])
            self.trees[r] = None
        self.trees[new_tree.rank] = new_tree
        if new_tree.item.key <= self.min_key:
            self.min_key = new_tree.item.key
            self.min_value = new_tree.item.value
            self.min_tree_rank = new_tree.rank
    def insert(self, key, value):
        tree = BinomialTree(key, value)
        self.__add_tree(tree)
        return tree.item
    def extract_min(self):
        if not self:
            raise EmptyBinomialHeapError("Heap is empty.")
        to_remove = self.trees[self.min_tree_rank]
        self.trees[to_remove.rank] = None
        self.elements -= 2 ** to_remove.rank
        for child in to_remove.children:
            child.parent = None
            self.__add_tree(child)
        self.min_key = self.infinity
        for tree in self.trees:
            if tree is not None:
                if tree.item.key <= self.min_key:
                    self.min_key = tree.item.key
                    self.min_value = tree.item.value
                    self.min_tree_rank = tree.rank
        return to_remove.item
    def decrease_key(self, node, new_key):
        update_ref = node.tree.decrease_key(new_key)
        self.min_key = self.infinity
        for tree in self.trees:
            if tree is not None:
                if tree.item.key <= self.min_key:
                    self.min_key = tree.item.key
                    self.min_value = tree.item.value
                    self.min_tree_rank = tree.rank
        return update_ref
    def __str__(self):
        s = f"elements: {self.elements} min: {str(self.min_key)}\n"
        s += f"min_tree_rank: {self.min_tree_rank}\n"
        s += "".join("10"[tree is None] for tree in self.trees) + "\n"
        s += "".join(str(tree) for tree in self.trees if tree is not None)
        return s
def test():
    bh1 = BinomialHeap()
    bh1.insert(12, "a")
    bh1.insert(5, "b")
    bh1.insert(21, "c")
    bh1.insert(8, "d")
    item_e = bh1.insert(100, "e")
    print(bh1)
    print("min item: ", bh1.min_value)
    print("\n")
    bh1.extract_min()
    print(bh1)
    print("min item: ", bh1.min_value)
    bh1.decrease_key(item_e, 1)
    print(bh1)
    bh1.extract_min()
    print(bh1)
if __name__ == '__main__':
    test()