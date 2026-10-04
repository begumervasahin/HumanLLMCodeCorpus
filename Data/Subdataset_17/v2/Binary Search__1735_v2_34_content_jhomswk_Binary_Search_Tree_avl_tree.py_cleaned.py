class Node:
    def __init__(self, key, parent=None):
        self.key = key
        self.left = None
        self.right = None
        self.parent = parent
        self.height = 0
class BinarySearchTree:
    def __init__(self):
        self.root = None
    def insert(self, key):
        if not self.root:
            self.root = Node(key)
            return self.root
        current = self.root
        parent = None
        while current:
            parent = current
            if key < current.key:
                current = current.left
            else:
                current = current.right
        new_node = Node(key, parent)
        if key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node
        return new_node
    def delete(self, key):
        node = self._find(key, self.root)
        if node is None:
            return None
        if node.left and node.right:
            successor = self._min_value_node(node.right)
            node.key = successor.key
            node = successor
        child = node.left if node.left else node.right
        if child:
            child.parent = node.parent
        if node.parent:
            if node == node.parent.left:
                node.parent.left = child
            else:
                node.parent.right = child
        else:
            self.root = child
        return node
    def _find(self, key, node):
        while node and node.key != key:
            node = node.left if key < node.key else node.right
        return node
    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current
def height(node):
    return node.height if node else -1
def update_height(node):
    node.height = 1 + max(height(node.left), height(node.right))
class AVLTree(BinarySearchTree):
    def rotate_left(self, node):
        child = node.right
        child.parent = node.parent
        if not node.parent:
            self.root = child
        elif node == node.parent.left:
            node.parent.left = child
        else:
            node.parent.right = child
        node.right = child.left
        if node.right:
            node.right.parent = node
        child.left = node
        node.parent = child
        update_height(node)
        update_height(child)
    def rotate_right(self, node):
        child = node.left
        child.parent = node.parent
        if not node.parent:
            self.root = child
        elif node == node.parent.left:
            node.parent.left = child
        else:
            node.parent.right = child
        node.left = child.right
        if node.left:
            node.left.parent = node
        child.right = node
        node.parent = child
        update_height(node)
        update_height(child)
    def balance(self, node):
        while node:
            update_height(node)
            balance_factor = height(node.left) - height(node.right)
            if balance_factor > 1:
                if height(node.left.left) >= height(node.left.right):
                    self.rotate_right(node)
                else:
                    self.rotate_left(node.left)
                    self.rotate_right(node)
            elif balance_factor < -1:
                if height(node.right.right) >= height(node.right.left):
                    self.rotate_left(node)
                else:
                    self.rotate_right(node.right)
                    self.rotate_left(node)
            node = node.parent
    def insert(self, key):
        node = super().insert(key)
        self.balance(node)
    def delete(self, key):
        node = super().delete(key)
        if node and node.parent:
            self.balance(node.parent)
if __name__ == "__main__":
    avl = AVLTree()
    avl.insert(10)
    avl.insert(20)
    avl.insert(30)
    avl.insert(40)
    avl.insert(50)
    avl.insert(25)
    print("Root after inserts:", avl.root.key)
    avl.delete(40)
    print("Root after deleting 40:", avl.root.key)