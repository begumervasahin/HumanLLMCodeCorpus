from binary_search_tree import Binary_Search_Tree
def height(node):
    return node.height if node else -1
def update_height(node):
    node.height = 1 + max(height(node.left), height(node.right))
class AVLTree(Binary_Search_Tree):
    def rotate_left(self, node):
        right_child = node.right
        right_child.parent = node.parent
        if node.parent is None:
            self.root = right_child
        else:
            if node is node.parent.left:
                node.parent.left = right_child
            else:
                node.parent.right = right_child
        node.right = right_child.left
        if node.right:
            node.right.parent = node
        right_child.left = node
        node.parent = right_child
        update_height(node)
        update_height(right_child)
    def rotate_right(self, node):
        left_child = node.left
        left_child.parent = node.parent
        if node.parent is None:
            self.root = left_child
        else:
            if node is node.parent.left:
                node.parent.left = left_child
            else:
                node.parent.right = left_child
        node.left = left_child.right
        if node.left:
            node.left.parent = node
        left_child.right = node
        node.parent = left_child
        update_height(node)
        update_height(left_child)
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
        new_node = super(AVLTree, self).insert(key)
        self.balance(new_node)
    def delete(self, key):
        node_to_delete = super(AVLTree, self).delete(key)
        if node_to_delete:
            self.balance(node_to_delete.parent)