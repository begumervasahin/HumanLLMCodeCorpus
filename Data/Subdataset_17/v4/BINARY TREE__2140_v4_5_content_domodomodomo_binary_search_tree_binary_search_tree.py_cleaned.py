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
        else:
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
        else:
            return self
    def search_max(self):
        if self.right:
            return self.right.search_max()
        else:
            return self
    def search_min(self):
        if self.left:
            return self.left.search_min()
        else:
            return self
    def list(self):
        left_sorted_list = self.left.list() if self.left else []
        center = [self.value]
        right_sorted_list = self.right.list() if self.right else []
        return left_sorted_list + center + right_sorted_list
    def list_sequentially(self):
        sorted_list = []
        path = Path(self)
        for value in path:
            sorted_list.append(value)
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
        else:
            if self.left:
                max_left = self.left.search_max()
                self.value = max_left.value
                self.left = self.left.delete_max()
            else:
                return self.right
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
        else:
            if self.right:
                min_right = self.right.search_min()
                self.value = min_right.value
                self.right = self.right.delete_min()
            else:
                return self.left
        return self
    def delete_max(self):
        if self.right:
            self.right = self.right.delete_max()
        else:
            return self.left
        return self
    def delete_min(self):
        if self.left:
            self.left = self.left.delete_min()
        else:
            return self.right
        return self
    def __iter__(self):
        return Path(self)
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
    if binary_search_node.left:
        yield from binary_search_node.left
    yield binary_search_node.value
    if binary_search_node.right:
        yield from binary_search_node.right