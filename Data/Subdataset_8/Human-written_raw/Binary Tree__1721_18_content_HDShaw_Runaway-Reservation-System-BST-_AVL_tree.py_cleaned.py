import binary_search_tree as BST
class AVLtreeNode(BST.tree_node):
    def __init__(self,key = None, left = None, right = None,height=0):
        self.key = key
        self.left = left
        self.right = right
        self.height=height
class AVLtree(BST.binary_search_tree):
    def leftRotate(self,root):
        tempnode=root
        root=root.right
        root.right=tempnode.right.right
        root.left=tempnode
        return root
    def rightRotate(self,root):
        tempnode = root
        root = root.left
        root.left = tempnode.left.left
        root.right = tempnode
        return root
    def left_to_rightRotate(self,root):
        temp=root.left
        root.left=temp.right
        root.left.right=temp
        self.rightRotate(root)
    def right_to_leftRotate(self,root):
        temp = root.right
        root.right = temp.left
        root.right.right = temp
        self.leftRotate(root)
    def find_heavy_root(self,root):
        if (not root.left or root.right) and (not root.left.left or
                                                  root.left.right) and (not root.right.right or root.right.lef):
            return root
        if root.left._height>root.right._height:
            self.find_heavy_root(root.left)
        else:
            self.find_heavy_root(root.right)
        return root
    def avl_insert(self,key):
        self._avl_insert(self.root,key)
    def _avl_insert(self,root,key):
        left_height=self._height(root.left)
        right_height=self._height(root.right)
        if left_height-right_height>1:
            rotateNode=self.find_heavy_root(root)
            if not rotateNode.left:
                self.left_to_rightRotate(rotateNode)
            elif not rotateNode.right:
                self.rightRotate(rotateNode)
        elif right_height-left_height>1:
            rotateNode = self.find_heavy_root(root)
            if not rotateNode.left:
                self.leftRotate(rotateNode)
            elif not rotateNode.right:
                self.right_to_leftRotate(rotateNode)
        else:
            return root
        return self._insert(root,key)
    def avl_delete(self,key):
        return self.delete(key)
    def avl_inorder(self):
        return self.inorder()
    def avl_preorder(self):
        return self.preorder()
    def avl_postorder(self):
        return self.postorder()
def main():
    import random
    test = AVLtree()
    print(type(test))
    for i in random.sample([j for j in range(1, 100)], 5):
        test.insert(i)
    print('insert: ')
    test.insert(78)
    test.insert(101)
    test.insert(14)
    test.preorder()
    test.inorder()
    test.postorder()
    print('height: ', test.height())
    print('count: ', test.subtree())
    print('min: ', test.find_min().key)
    print('max: ', test.find_max().key)
    print( 'delete: ')
    test.delete(101)
    test.delete(12)
    test.preorder()
    test.inorder()
    test.postorder()
    test.find(71)
    test.find(92)
    test.find(78)
    print('height: ', test.height())
    print('count: ', test.subtree())
    print('min: ', test.find_min().key)
    print('max: ', test.find_max().key)
if __name__ == '__main__':
    main()