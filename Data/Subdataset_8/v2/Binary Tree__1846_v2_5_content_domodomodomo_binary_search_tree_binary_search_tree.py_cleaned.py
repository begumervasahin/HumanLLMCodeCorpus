class BinarySearchTree:
    def __init__(self):
        self.root = None
    def insert(self, value):
        if self.root:
            self.root.insert(value)
        else:
            self.root = BinarySearchNode(value)
    def search(self, value):
        if self.root:
            return self.root.search(value)
        else:
            raise ValueError("Tree is empty")
    def list(self):
        if self.root:
            return self.root.list()
        else:
            return []
    def list_sequentially(self):
        if self.root:
            return self.root.list_sequentially()
        else:
            return []
    def delete_left(self, value):
        if self.root:
            self.root = self.root.delete_left(value)
        else:
            raise ValueError("Tree is empty")
    def delete_right(self, value):
        if self.root:
            self.root = self.root.delete_right(value)
        else:
            raise ValueError("Tree is empty")
    def __iter__(self):
        if self.root:
            return iter(self.root)
        else:
            return iter([])
class BinarySearchNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def insert(self, value):
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinarySearchNode(value)
        elif value >= self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchNode(value)
    def search(self, value):
        if value < self.value:
            if self.left:
                return self.left.search(value)
            else:
                raise ValueError("Value not found")
        elif value > self.value:
            if self.right:
                return self.right.search(value)
            else:
                raise ValueError("Value not found")
        elif value == self.value:
            return self
    def list(self):
        left_list = self.left.list() if self.left else []
        right_list = self.right.list() if self.right else []
        return left_list + [self.value] + right_list
    def list_sequentially(self):
        sorted_list = []
        path = Path(self)
        while True:
            try:
                value = next(path)
                sorted_list.append(value)
            except StopIteration:
                break
        return sorted_list
    def delete_left(self, value):
        if value < self.value:
            if self.left:
                self.left = self.left.delete_left(value)
            else:
                raise ValueError("Value not found")
        elif value > self.value:
            if self.right:
                self.right = self.right.delete_left(value)
            else:
                raise ValueError("Value not found")
        elif value == self.value:
            old_self = self
            if old_self.left:
                self = old_self.left.search_max()
                self.left = old_self.left.delete_max()
                self.right = old_self.right
            else:
                self = old_self.right
            old_self.left = None
            old_self.right = None
        return self
    def delete_right(self, value):
        if value < self.value:
            if self.left:
                self.left = self.left.delete_right(value)
            else:
                raise ValueError("Value not found")
        elif value > self.value:
            if self.right:
                self.right = self.right.delete_right(value)
            else:
                raise ValueError("Value not found")
        elif value == self.value:
            old_self = self
            if old_self.right:
                self = old_self.right.search_min()
                self.right = old_self.right.delete_min()
                self.left = old_self.left
            else:
                self = old_self.left
            old_self.left = None
            old_self.right = None
        return self
    def delete_max(self):
        if self.right:
            self.right = self.right.delete_max()
        else:
            self = self.left
        return self
    def delete_min(self):
        if self.left:
            self.left = self.left.delete_min()
        else:
            self = self.right
        return self
class Path:
    def __init__(self, root):
        pseudo_node = BinarySearchNode(None)
        pseudo_node.right = root
        self._route = [pseudo_node]
    def __next__(self):
        if self._current_node().right:
            self._seek_right_min()
        else:
            self._seek_right_parent()
        return self._current_node().value
    def _seek_right_min(self):
        self._route.append(self._current_node().right)
        while self._current_node().left:
            self._route.append(self._current_node().left)
    def _seek_right_parent(self):
        try:
            while self._route.pop() == self._current_node().right:
                pass
        except IndexError:
            raise StopIteration
    def _current_node(self):
        return self._route[-1]
    def __iter__(self):
        return self
def list_iterator(binary_search_node):
    return iter(binary_search_node.list())
def iterator(binary_search_node):
    return Path(binary_search_node)
def generator(binary_search_node):
    bsn = binary_search_node
    if bsn.left:
        yield from bsn.left
    yield bsn.value
    if bsn.right:
        yield from bsn.right
bst = BinarySearchTree()
values = [5, 3, 7, 1, 4, 6, 8]
for value in values:
    bst.insert(value)
print("Binary Search Tree:")
print(bst.list())
print("Sequential traversal:")
print(bst.list_sequentially())
print("Searching for 3:", bst.search(3).value)
print("Searching for 10:")
try:
    print(bst.search(10).value)
except ValueError as e:
    print(e)
bst.delete_left(5)
print("After deleting 5 from left:")
print(bst.list())
bst.delete_right(7)
print("After deleting 7 from right:")
print(bst.list())