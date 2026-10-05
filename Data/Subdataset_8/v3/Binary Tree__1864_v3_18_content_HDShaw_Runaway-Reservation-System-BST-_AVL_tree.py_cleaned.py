class AVLTreeNode:
    def __init__(self, key=None, left=None, right=None, height=0):
        self.key = key
        self.left = left
        self.right = right
        self.height = height
class AVLTree:
    def __init__(self):
        self.root = None
    def left_rotate(self, node):
        temp = node
        node = node.right
        temp.right = node.left
        node.left = temp
        return node
    def right_rotate(self, node):
        temp = node
        node = node.left
        temp.left = node.right
        node.right = temp
        return node
    def left_to_right_rotate(self, node):
        temp = node.left
        node.left = temp.right
        temp.right = node
        return temp
    def right_to_left_rotate(self, node):
        temp = node.right
        node.right = temp.left
        temp.left = node
        return temp
    def find_heavy_node(self, node):
        if (not node.left or node.right) and (not node.left.left or node.left.right) and (
                not node.right.right or node.right.left):
            return node
        if node.left.height > node.right.height:
            return self.find_heavy_node(node.left)
        else:
            return self.find_heavy_node(node.right)
    def _height(self, node):
        if node is None:
            return -1
        else:
            return node.height
    def _insert(self, node, key):
        if node is None:
            return AVLTreeNode(key)
        elif key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)
        node.height = 1 + max(self._height(node.left), self._height(node.right))
        return node
    def avl_insert(self, key):
        self.root = self._avl_insert(self.root, key)
    def _avl_insert(self, node, key):
        node = self._insert(node, key)
        left_height = self._height(node.left)
        right_height = self._height(node.right)
        if left_height - right_height > 1:
            heavy_node = self.find_heavy_node(node)
            if not heavy_node.left:
                return self.left_to_right_rotate(heavy_node)
            elif not heavy_node.right:
                return self.right_rotate(heavy_node)
        elif right_height - left_height > 1:
            heavy_node = self.find_heavy_node(node)
            if not heavy_node.left:
                return self.left_rotate(heavy_node)
            elif not heavy_node.right:
                return self.right_to_left_rotate(heavy_node)
        return node
    def insert(self, key):
        self.avl_insert(key)
    def avl_delete(self, key):
        pass
    def inorder_traversal(self):
        self._inorder_traversal(self.root)
        print()
    def _inorder_traversal(self, node):
        if node:
            self._inorder_traversal(node.left)
            print(node.key, end=" ")
            self._inorder_traversal(node.right)
def main():
    import random
    tree = AVLTree()
    print(type(tree))
    for i in random.sample(range(1, 100), 5):
        tree.insert(i)
    print('Insertions:')
    tree.insert(78)
    tree.insert(101)
    tree.insert(14)
    tree.inorder_traversal()
    print('Height:', tree.root.height)
if __name__ == '__main__':
    main()