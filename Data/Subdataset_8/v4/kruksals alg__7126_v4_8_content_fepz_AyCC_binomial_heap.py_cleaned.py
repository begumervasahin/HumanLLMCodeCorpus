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
            raise LinkError("Other tree has a smaller minimum priority.")
        self.children.append(other_tree)
        other_tree.parent = self
        self.rank += 1
    def decrease(self, newkey):
        node = self
        node.item.key = newkey
        parent = node.parent
        while parent is not None and node.item.key < parent.item.key:
            parent.item, node.item = node.item, parent.item
            parent.item.tree = parent
            node.item.tree = node
            node = parent
            parent = node.parent
        return node
    def __str__(self):
        return f"rank: {self.rank}, key: {self.item.key}, value: {self.item.value}\n" + \
               "".join(child.__str__() for child in self.children)
class BinomialHeap:
    def __init__(self, infinity=float('inf')):
        self.infinity = infinity
        self.trees = []
        self.elements = 0
        self.min_key = self.infinity
        self.min_value = self.infinity
        self.min_tree_rank = -1
    def __capacity(self):
        return 2 ** len(self.trees) - 1
    def __resize(self):
        while self.__capacity() < self.elements:
            self.trees.append(None)
    def __add_tree(self, new_tree):
        self.elements = self.elements + 2 ** new_tree.rank
        self.__resize()
        while self.trees[new_tree.rank] is not None:
            if self.trees[new_tree.rank].item.key < new_tree.item.key:
                new_tree, self.trees[new_tree.rank] = self.trees[new_tree.rank], new_tree
            new_tree.link(self.trees[new_tree.rank])
            self.trees[new_tree.rank] = None
        self.trees[new_tree.rank] = new_tree
        if new_tree.item.key <= self.min_key:
            self.min_key = new_tree.item.key
            self.min_value = new_tree.item.value
            self.min_tree_rank = new_tree.rank
    def insert(self, key, value):
        tree = BinomialTree(key, value)
        self.__add_tree(tree)
        return tree.item
    def extractmin(self):
        if not self:
            raise EmptyBinomialHeapError("Cannot extract minimum from an empty heap.")
        to_remove = self.trees[self.min_tree_rank]
        self.trees[to_remove.rank] = None
        self.elements = self.elements - 2 ** to_remove.rank
        for child in to_remove.children:
            child.parent = None
            self.__add_tree(child)
        self.min_key = self.infinity
        for tree in self.trees:
            if tree is not None and tree.item.key <= self.min_key:
                self.min_key = tree.item.key
                self.min_value = tree.item.value
                self.min_tree_rank = tree.rank
        return to_remove.item
    def decreasekey(self, node, newkey):
        updateref = node.tree.decrease(newkey)
        self.min_key = self.infinity
        for tree in self.trees:
            if tree is not None and tree.item.key <= self.min_key:
                self.min_key = tree.item.key
                self.min_value = tree.item.value
                self.min_tree_rank = tree.rank
        return updateref
    def __str__(self):
        s = f"elements: {self.elements}, min: {str(self.min_key)}, min_tree_rank: {self.min_tree_rank}\n"
        s += "".join("10"[tree is None] for tree in self.trees) + "\n"
        s += "".join(str(tree) for tree in self.trees if tree is not None)
        return s
def test():
    bh1 = BinomialHeap()
    bh1.insert(12, "a")
    bh1.insert(5, "b")
    bh1.insert(21, "c")
    bh1.insert(8, "d")
    iteme = bh1.insert(100, "e")
    print(bh1)
    print("min item:", bh1.min_value)
    print("\n")
    bh1.extractmin()
    print(bh1)
    print("min item:", bh1.min_value)
    bh1.decreasekey(iteme, 1)
    print(bh1)
    bh1.extractmin()
    print(bh1)
if __name__ == '__main__':
    test()