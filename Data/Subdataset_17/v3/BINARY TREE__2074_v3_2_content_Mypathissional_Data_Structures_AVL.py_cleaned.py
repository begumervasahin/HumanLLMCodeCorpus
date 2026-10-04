class AVL:
    class Node:
        def __init__(self, value, right=None, left=None, height=1):
            self.value = value
            self.right = right
            self.left = left
            self.height = height
    def __init__(self):
        self.__root = None
    def insert(self, val):
        self.__root = self.__insert(self.__root, val)
    def remove(self, val):
        self.__root = self.__remove(self.__root, val)
    def find(self, val):
        return self.__find(self.__root, val)
    def __str__(self):
        return self.__print_tree(self.__root)
    def height(self):
        return self.__get_height(self.__root)
    def min(self):
        return self.__min(self.__root).value if not self.is_empty() else None
    def max(self):
        return self.__max(self.__root).value if not self.is_empty() else None
    def is_empty(self):
        return self.__root is None
    def __insert(self, node, val):
        if node is None:
            return AVL.Node(val)
        if val < node.value:
            node.left = self.__insert(node.left, val)
        elif val > node.value:
            node.right = self.__insert(node.right, val)
        return self.__balance(node)
    def __remove(self, node, val):
        if node is None:
            return None
        if val < node.value:
            node.left = self.__remove(node.left, val)
        elif val > node.value:
            node.right = self.__remove(node.right, val)
        else:
            if node.left is None or node.right is None:
                node = node.left if node.left else node.right
            else:
                min_node = self.__min(node.right)
                node.value = min_node.value
                node.right = self.__remove_min(node.right)
        return self.__balance(node)
    def __find(self, node, val):
        if node is None:
            return False
        if node.value == val:
            return node
        elif val < node.value:
            return self.__find(node.left, val)
        else:
            return self.__find(node.right, val)
    def __min(self, node):
        return node if node.left is None else self.__min(node.left)
    def __max(self, node):
        return node if node.right is None else self.__max(node.right)
    def __remove_min(self, node):
        if node.left is None:
            return node.right
        node.left = self.__remove_min(node.left)
        return self.__balance(node)
    def __get_height(self, node):
        return 0 if node is None else node.height
    def __fix_height(self, node):
        node.height = max(self.__get_height(node.left), self.__get_height(node.right)) + 1
    def __balance_factor(self, node):
        return self.__get_height(node.right) - self.__get_height(node.left)
    def __rotate_right(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        self.__fix_height(node)
        self.__fix_height(new_root)
        return new_root
    def __rotate_left(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        self.__fix_height(node)
        self.__fix_height(new_root)
        return new_root
    def __balance(self, node):
        self.__fix_height(node)
        if self.__balance_factor(node) == 2:
            if self.__balance_factor(node.right) < 0:
                node.right = self.__rotate_right(node.right)
            return self.__rotate_left(node)
        if self.__balance_factor(node) == -2:
            if self.__balance_factor(node.left) > 0:
                node.left = self.__rotate_left(node.left)
            return self.__rotate_right(node)
        return node
    def __print_tree(self, node):
        if node is None:
            return ''
        return f'{node.value},{node.height}\n' + self.__print_tree(node.left) + self.__print_tree(node.right)
if __name__ == '__main__':
    avl = AVL()
    avl.insert(10)
    avl.insert(20)
    avl.insert(5)
    avl.insert(6)
    avl.insert(15)
    print("AVL Tree:")
    print(avl)
    print("Find 10:", avl.find(10))
    print("Find 25:", avl.find(25))
    print("Min value:", avl.min())
    print("Max value:", avl.max())
    avl.remove(10)
    print("AVL Tree after removing 10:")
    print(avl)
    print("Tree height:", avl.height())