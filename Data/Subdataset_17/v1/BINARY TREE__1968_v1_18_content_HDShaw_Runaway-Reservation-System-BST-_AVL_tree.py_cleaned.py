import binary_search_tree as BST
class AVLtreeNode(BST.tree_node):
    def __init__(self, key=None, left=None, right=None, height=0):
        super().__init__(key, left, right)
        self.height = height
class AVLtree(BST.binary_search_tree):
    def leftRotate(self, root):
        tempnode = root
        root = root.right
        tempnode.right = root.left
        root.left = tempnode
        return root
    def rightRotate(self, root):
        tempnode = root
        root = root.left
        tempnode.left = root.right
        root.right = tempnode
        return root
    def left_to_rightRotate(self, root):
        root.left = self.leftRotate(root.left)
        return self.rightRotate(root)
    def right_to_leftRotate(self, root):
        root.right = self.rightRotate(root.right)
        return self.leftRotate(root)
    def find_heavy_root(self, root):
        while root:
            left_height = self._height(root.left)
            right_height = self._height(root.right)
            if abs(left_height - right_height) > 1:
                return root
            if left_height > right_height:
                root = root.left
            else:
                root = root.right
        return root
    def avl_insert(self, key):
        self.root = self._avl_insert(self.root, key)
    def _avl_insert(self, root, key):
        if not root:
            return AVLtreeNode(key)
        if key < root.key:
            root.left = self._avl_insert(root.left, key)
        else:
            root.right = self._avl_insert(root.right, key)
        root.height = 1 + max(self._height(root.left), self._height(root.right))
        balance = self._get_balance(root)
        if balance > 1:
            if key < root.left.key:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        if balance < -1:
            if key > root.right.key:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        return root
    def avl_delete(self, key):
        self.root = self._avl_delete(self.root, key)
    def _avl_delete(self, root, key):
        if not root:
            return root
        if key < root.key:
            root.left = self._avl_delete(root.left, key)
        elif key > root.key:
            root.right = self._avl_delete(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            temp = self._get_min_value_node(root.right)
            root.key = temp.key
            root.right = self._avl_delete(root.right, temp.key)
        root.height = 1 + max(self._height(root.left), self._height(root.right))
        balance = self._get_balance(root)
        if balance > 1:
            if self._get_balance(root.left) >= 0:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        if balance < -1:
            if self._get_balance(root.right) <= 0:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        return root
    def avl_inorder(self):
        return self.inorder()
    def avl_preorder(self):
        return self.preorder()
    def avl_postorder(self):
        return self.postorder()
    def _height(self, node):
        if not node:
            return -1
        return node.height
    def _get_balance(self, node):
        if not node:
            return 0
        return self._height(node.left) - self._height(node.right)
    def _get_min_value_node(self, node):
        while node.left:
            node = node.left
        return node
def main():
    import random
    test = AVLtree()
    print(type(test))
    for i in random.sample(range(1, 100), 5):
        test.avl_insert(i)
    print('insert: ')
    test.avl_insert(78)
    test.avl_insert(101)
    test.avl_insert(14)
    print('Pre-order traversal:')
    for val in test.avl_preorder():
        print(val, end=' ')
    print('\nIn-order traversal:')
    for val in test.avl_inorder():
        print(val, end=' ')
    print('\nPost-order traversal:')
    for val in test.avl_postorder():
        print(val, end=' ')
    print('\nheight: ', test.height())
    print('count: ', test.subtree_count())
    print('min: ', test.find_min().key)
    print('max: ', test.find_max().key)
    print('delete: ')
    test.avl_delete(101)
    test.avl_delete(14)
    print('Pre-order traversal after delete:')
    for val in test.avl_preorder():
        print(val, end=' ')
    print('\nIn-order traversal after delete:')
    for val in test.avl_inorder():
        print(val, end=' ')
    print('\nPost-order traversal after delete:')
    for val in test.avl_postorder():
        print(val, end=' ')
    print('\nheight: ', test.height())
    print('count: ', test.subtree_count())
    print('min: ', test.find_min().key)
    print('max: ', test.find_max().key)
if __name__ == '__main__':
    main()