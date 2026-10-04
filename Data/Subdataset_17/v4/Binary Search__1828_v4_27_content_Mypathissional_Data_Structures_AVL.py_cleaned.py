class AVLTree:
    class Node:
        def __init__(self, value, right=None, left=None, height=1):
            self.value = value
            self.right = right
            self.left = left
            self.height = height
    def __init__(self):
        self.__root = None
    def insert(self, value):
        self.__root = self.__insert(self.__root, value)
    def remove(self, value):
        self.__root = self.__remove(self.__root, value)
    def find(self, value):
        return self.__find(self.__root, value)
    def height(self):
        return self.__get_height(self.__root)
    def min(self):
        if not self.is_empty():
            return self.__min(self.__root).value
    def max(self):
        if not self.is_empty():
            return self.__max(self.__root).value
    def is_empty(self):
        return self.__root is None
    def __insert(self, node, value):
        if node is None:
            return AVLTree.Node(value)
        if value < node.value:
            node.left = self.__insert(node.left, value)
        elif value > node.value:
            node.right = self.__insert(node.right, value)
        else:
            return node
        return self.__balance_tree(node)
    def __remove(self, node, value):
        if not node:
            return None
        if value < node.value:
            node.left = self.__remove(node.left, value)
        elif value > node.value:
            node.right = self.__remove(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            min_node = self.__min(node.right)
            node.value = min_node.value
            node.right = self.__remove_min(node.right)
        return self.__balance_tree(node)
    def __balance_tree(self, node):
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
    def __rotate_left(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        self.__fix_height(node)
        self.__fix_height(new_root)
        return new_root
    def __rotate_right(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        self.__fix_height(node)
        self.__fix_height(new_root)
        return new_root
    def __fix_height(self, node):
        node.height = max(self.__get_height(node.left), self.__get_height(node.right)) + 1
    def __balance_factor(self, node):
        return self.__get_height(node.right) - self.__get_height(node.left)
    def __get_height(self, node):
        return node.height if node else 0
    def __min(self, node):
        return node if node.left is None else self.__min(node.left)
    def __max(self, node):
        return node if node.right is None else self.__max(node.right)
    def __remove_min(self, node):
        if node.left is None:
            return node.right
        node.left = self.__remove_min(node.left)
        return self.__balance_tree(node)
    def __find(self, node, value):
        if node is None:
            return None
        if node.value == value:
            return node
        elif value < node.value:
            return self.__find(node.left, value)
        else:
            return self.__find(node.right, value)
    def __str__(self):
        return self.__print_heights(self.__root)
    def __print_heights(self, node):
        if node is None:
            return ''
        result = f'{node.value},{node.height}\n'
        result += self.__print_heights(node.left)
        result += self.__print_heights(node.right)
        return result