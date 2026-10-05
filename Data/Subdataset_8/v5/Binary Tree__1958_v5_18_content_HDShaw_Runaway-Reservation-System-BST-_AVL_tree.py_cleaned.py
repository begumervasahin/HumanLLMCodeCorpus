import random
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
        left_height = root.left.height if root.left else 0
        right_height = root.right.height if root.right else 0
        if abs(left_height - right_height) > 1:
            return root
        elif left_height > right_height:
            return self.find_heavy_root(root.left)
        else:
            return self.find_heavy_root(root.right)
    def _avl_insert(self, root, key):
        if not root:
            return AVLTreeNode(key)
        if key < root.key:
            root.left = self._avl_insert(root.left, key)
        else:
            root.right = self._avl_insert(root.right, key)
        root.height = max(self._height(root.left), self._height(root.right)) + 1
        balance = self._balance_factor(root)
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
    def avl_insert(self, key):
        self.root = self._avl_insert(self.root, key)
    def avl_delete(self, key):
        self.root = self.delete(self.root, key)
def main():
    test = AVLTree()
    print(type(test))
    elements_to_insert = random.sample(range(1, 100), 5)
    for element in elements_to_insert:
        test.avl_insert(element)
    print('Inserting elements:')
    test.avl_insert(78)
    test.avl_insert(101)
    test.avl_insert(14)
    print('Preorder:')
    test.avl_preorder()
    print('Inorder:')
    test.avl_inorder()
    print('Postorder:')
    test.avl_postorder()
    print('Height:', test.height())
    print('Count:', test.subtree())
    print('Minimum:', test.find_min().key)
    print('Maximum:', test.find_max().key)
    print('Deleting elements:')
    test.avl_delete(101)
    test.avl_delete(12)
    print('Preorder:')
    test.avl_preorder()
    print('Inorder:')
    test.avl_inorder()
    print('Postorder:')
    test.avl_postorder()
    test.find(71)
    test.find(92)
    test.find(78)
    print('Height:', test.height())
    print('Count:', test.subtree())
    print('Minimum:', test.find_min().key)
    print('Maximum:', test.find_max().key)
if __name__ == '__main__':
    main()