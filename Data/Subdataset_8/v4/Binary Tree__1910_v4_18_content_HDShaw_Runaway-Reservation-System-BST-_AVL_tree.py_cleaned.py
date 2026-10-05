import binary_search_tree as BST
class AVLTreeNode(BST.TreeNode):
    def __init__(self, key=None, left=None, right=None, height=0):
        super().__init__(key, left, right)
        self.height = height
class AVLTree(BST.BinarySearchTree):
    def left_rotate(self, root):
        temp_node = root
        root = root.right
        root.right = temp_node.right
        root.left = temp_node
        return root
    def right_rotate(self, root):
        temp_node = root
        root = root.left
        root.left = temp_node.left
        root.right = temp_node
        return root
    def left_to_right_rotate(self, root):
        temp = root.left
        root.left = temp.right
        temp.right = root
        return temp
    def right_to_left_rotate(self, root):
        temp = root.right
        root.right = temp.left
        temp.left = root
        return temp
    def find_heavy_root(self, root):
        if (not root.left or root.right) and (not root.left.left or root.left.right) and (not root.right.right or root.right.left):
            return root
        if root.left.height > root.right.height:
            return self.find_heavy_root(root.left)
        else:
            return self.find_heavy_root(root.right)
    def avl_insert(self, key):
        self._avl_insert(self.root, key)
    def _avl_insert(self, root, key):
        left_height = self._height(root.left)
        right_height = self._height(root.right)
        if left_height - right_height > 1:
            rotate_node = self.find_heavy_root(root)
            if not rotate_node.left:
                return self.left_to_right_rotate(rotate_node)
            elif not rotate_node.right:
                return self.right_rotate(rotate_node)
        elif right_height - left_height > 1:
            rotate_node = self.find_heavy_root(root)
            if not rotate_node.left:
                return self.left_rotate(rotate_node)
            elif not rotate_node.right:
                return self.right_to_left_rotate(rotate_node)
        else:
            return root
        return self._insert(root, key)
    def avl_delete(self, key):
        return self.delete(key)
    def avl_inorder(self):
        return self.inorder()
    def avl_preorder(self):
        return self.preorder()
    def avl_postorder(self):
        return self.postorder()
def main():
    import random
    test = AVLTree()
    print(type(test))
    for i in random.sample([j for j in range(1, 100)], 5):
        test.insert(i)
    print('Inserting elements:')
    test.insert(78)
    test.insert(101)
    test.insert(14)
    test.preorder()
    test.inorder()
    test.postorder()
    print('Height:', test.height())
    print('Count:', test.subtree())
    print('Minimum:', test.find_min().key)
    print('Maximum:', test.find_max().key)
    print('Deleting elements:')
    test.delete(101)
    test.delete(12)
    test.preorder()
    test.inorder()
    test.postorder()
    test.find(71)
    test.find(92)
    test.find(78)
    print('Height:', test.height())
    print('Count:', test.subtree())
    print('Minimum:', test.find_min().key)
    print('Maximum:', test.find_max().key)
if __name__ == '__main__':
    main()