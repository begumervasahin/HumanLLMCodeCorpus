class Node:
    def __init__(self, key, value=None, left=None, right=None, parent=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0
    def insert(self, key, value=None):
        if self.root:
            self._insert(key, value, self.root)
        else:
            self.root = Node(key, value)
        self.size += 1
    def _insert(self, key, value, current_node):
        if key < current_node.key:
            if current_node.left:
                self._insert(key, value, current_node.left)
            else:
                current_node.left = Node(key, value, parent=current_node)
        else:
            if current_node.right:
                self._insert(key, value, current_node.right)
            else:
                current_node.right = Node(key, value, parent=current_node)
    def get(self, key):
        if self.root:
            result = self._get(key, self.root)
            if result:
                return result.value
        return None
    def _get(self, key, current_node):
        while current_node:
            if key == current_node.key:
                return current_node
            elif key < current_node.key:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return None
    def delete(self, key):
        if self.size > 1:
            node_to_delete = self._get(key, self.root)
            if node_to_delete:
                self._remove(node_to_delete)
                self.size -= 1
            else:
                raise KeyError('Key not found in the tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError('Key not found in the tree')
    def _remove(self, node):
        if node.left is None and node.right is None:
            if node.parent:
                if node == node.parent.left:
                    node.parent.left = None
                else:
                    node.parent.right = None
        elif node.left and node.right:
            successor = node.right
            while successor.left:
                successor = successor.left
            node.key = successor.key
            node.value = successor.value
            self._remove(successor)
        else:
            if node.left:
                child = node.left
            else:
                child = node.right
            if node.parent:
                if node == node.parent.left:
                    node.parent.left = child
                else:
                    node.parent.right = child
                child.parent = node.parent
            else:
                self.root = child
                child.parent = None
def main():
    tree = BinaryTree()
    tree.insert(5, 'five')
    tree.insert(3, 'three')
    tree.insert(7, 'seven')
    tree.insert(2, 'two')
    tree.insert(4, 'four')
    print("Tree size:", len(tree))
    print("Value for key 3:", tree.get(3))
    tree.delete(3)
    print("Tree size after deleting key 3:", len(tree))
    print("Value for key 3 after deletion:", tree.get(3))
if __name__ == "__main__":
    main()