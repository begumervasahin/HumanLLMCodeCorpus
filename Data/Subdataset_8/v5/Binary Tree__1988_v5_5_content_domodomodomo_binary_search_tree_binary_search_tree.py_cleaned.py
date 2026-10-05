class BinarySearchTree:
    def __init__(self):
        self.root = None
    def insert(self, value):
        if self.root:
            self._insert(value, self.root)
        else:
            self.root = BinarySearchNode(value)
    def _insert(self, value, node):
        if value < node.value:
            if node.left:
                self._insert(value, node.left)
            else:
                node.left = BinarySearchNode(value)
        elif value >= node.value:
            if node.right:
                self._insert(value, node.right)
            else:
                node.right = BinarySearchNode(value)
    def search(self, value):
        if self.root:
            return self._search(value, self.root)
        else:
            raise ValueError("Tree is empty")
    def _search(self, value, node):
        if not node:
            raise ValueError("Value not found")
        if value == node.value:
            return node
        elif value < node.value:
            return self._search(value, node.left)
        else:
            return self._search(value, node.right)
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
            self.root = self.root.delete(value, side='left')
        else:
            raise ValueError("Tree is empty")
    def delete_right(self, value):
        if self.root:
            self.root = self.root.delete(value, side='right')
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
    def list(self):
        left_sorted_list = self.left.list() if self.left else []
        right_sorted_list = self.right.list() if self.right else []
        return left_sorted_list + [self.value] + right_sorted_list
    def list_sequentially(self):
        sorted_list = []
        path = Path(self)
        while True:
            try:
                value = next(path)
            except StopIteration:
                break
            else:
                sorted_list.append(value)
        return sorted_list
    def delete(self, value, side):
        if value < self.value:
            if self.left:
                self.left = self.left.delete(value, side)
            else:
                raise ValueError(f"Value {value} not found")
        elif value > self.value:
            if self.right:
                self.right = self.right.delete(value, side)
            else:
                raise ValueError(f"Value {value} not found")
        elif value == self.value:
            if side == 'left':
                return self._delete_left()
            elif side == 'right':
                return self._delete_right()
    def _delete_left(self):
        if self.left:
            max_node = self.left._find_max()
            max_value = max_node.value
            self.left = self.left.delete(max_value, side='left')
            self.value = max_value
            return self
        else:
            return self.right
    def _delete_right(self):
        if self.right:
            min_node = self.right._find_min()
            min_value = min_node.value
            self.right = self.right.delete(min_value, side='right')
            self.value = min_value
            return self
        else:
            return self.left
    def _find_max(self):
        if self.right:
            return self.right._find_max()
        else:
            return self
    def _find_min(self):
        if self.left:
            return self.left._find_min()
        else:
            return self
    def __iter__(self):
        return Path(self)
class Path:
    def __init__(self, root):
        self.route = []
        self._traverse_left(root)
    def _traverse_left(self, node):
        while node:
            self.route.append(node)
            node = node.left
    def __next__(self):
        if not self.route:
            raise StopIteration
        current_node = self.route.pop()
        if current_node.right:
            self._traverse_left(current_node.right)
        return current_node.value
    def __iter__(self):
        return self
if __name__ == '__main__':
    pass