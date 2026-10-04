import binary_search_tree as BST
class AVLTreeNode(BST.TreeNode):
    def __init__(self, key=None, left=None, right=None, height=0):
        super().__init__(key, left, right)
        self.height = height
class AVLTree(BST.BinarySearchTree):
    def left_rotate(self, root):
        temp_node = root
        root = root.right
        temp_node.right = root.left
        root.left = temp_node
        return root
    def right_rotate(self, root):
        temp_node = root
        root = root.left
        temp_node.left = root.right
        root.right = temp_node
        return root
    def left_to_right_rotate(self, root):
        root.left = self.left_rotate(root.left)
        return self.right_rotate(root)
    def right_to_left_rotate(self, root):
        root.right = self.right_rotate(root.right)
        return self.left_rotate(root)
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
            return AVLTreeNode(key)
        if key < root.key:
            root.left = self._avl_insert(root.left, key)
        else:
            root.right = self._avl_insert(root.right, key)
        root.height = 1 + max(self._height(root.left), self._height(root.right))
        balance = self._get_balance(root)
        if balance > 1:
            if key < root.left.key:
                return self.right_rotate(root)
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)
        if balance < -1:
            if key > root.right.key:
                return self.left_rotate(root)
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)
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
                return self.right_rotate(root)
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)
        if balance < -1:
            if self._get_balance(root.right) <= 0:
                return self.left_rotate(root)
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)
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
    test = AVLTree()
    print(f"Tree type: {type(test)}")
    for i in random.sample(range(1, 100), 5):
        test.avl_insert(i)
    print('Inserting values 78, 101, and 14...')
    test.avl_insert(78)
    test.avl_insert(101)
    test.avl_insert(14)
    print('\nPre-order traversal:')
    for val in test.avl_preorder():
        print(val, end=' ')
    print('\n\nIn-order traversal:')
    for val in test.avl_inorder():
        print(val, end=' ')
    print('\n\nPost-order traversal:')
    for val in test.avl_postorder():
        print(val, end=' ')
    print(f'\n\nTree height: {test.height()}')
    print(f'Tree node count: {test.subtree_count()}')
    print(f'Minimum key: {test.find_min().key}')
    print(f'Maximum key: {test.find_max().key}')
    print('\nDeleting values 101 and 14...')
    test.avl_delete(101)
    test.avl_delete(14)
    print('\nPre-order traversal after delete:')
    for val in test.avl_preorder():
        print(val, end=' ')
    print('\n\nIn-order traversal after delete:')
    for val in test.avl_inorder():
        print(val, end=' ')
    print('\n\nPost-order traversal after delete:')
    for val in test.avl_postorder():
        print(val, end=' ')
    print(f'\n\nTree height after delete: {test.height()}')
    print(f'Tree node count after delete: {test.subtree_count()}')
    print(f'Minimum key after delete: {test.find_min().key}')
    print(f'Maximum key after delete: {test.find_max().key}')
if __name__ == '__main__':
    main()