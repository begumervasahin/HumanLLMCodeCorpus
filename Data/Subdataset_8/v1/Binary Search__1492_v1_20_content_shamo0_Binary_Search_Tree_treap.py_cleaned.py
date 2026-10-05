import random
import sys
class Node:
    def __init__(self, data):
        '''Initialize Node with data.'''
        self.data = data
        self.left = None
        self.right = None
        self.priority = random.random()
    def __str__(self):
        '''Return string representation of data.'''
        return str(self.data)
class TreapSet:
    def __init__(self):
        self.root = None
        self.count = 0
    def left_rot(self, node):
        '''Rotates the subtree to the left.'''
        new_parent = node.right
        tmp = new_parent.left
        new_parent.left = node
        new_parent.left.right = tmp
        return new_parent
    def right_rot(self, node):
        '''Rotates the subtree to the right.'''
        new_parent = node.left
        tmp = new_parent.right
        new_parent.right = node
        new_parent.right.left = tmp
        return new_parent
    def add(self, e):
        '''Inserts element into the tree'''
        self.count += 1
        if self.root is None:
            self.root = Node(e)
        else:
            self.root = self.__add(e, self.root)
    def __add(self, e, ref_node):
        if ref_node is None:
            return Node(e)
        elif e < ref_node.data:
            ref_node.left = self.__add(e, ref_node.left)
            if ref_node.left.priority > ref_node.priority:
                return self.right_rot(ref_node)
        else:
            ref_node.right = self.__add(e, ref_node.right)
            if ref_node.right.priority > ref_node.priority:
                return self.left_rot(ref_node)
        return ref_node
    def __contains__(self, element):
        '''Checks if the element is in the tree'''
        return self.__contains(self.root, element)
    def __contains(self, ref_node, element):
        if ref_node is None:
            return False
        elif ref_node.data == element:
            return True
        if element < ref_node.data:
            return self.__contains(ref_node.left, element)
        elif element > ref_node.data:
            return self.__contains(ref_node.right, element)
        else:
            return False
    def height(self):
        '''Used for determining the height of the tree'''
        return self.__height(self.root)
    def __height(self, node):
        if node is None:
            return 0
        else:
            return 1 + max(self.__height(node.left), self.__height(node.right))
    def __len__(self):
        '''Returns the number of items in tree'''
        return self.count
if __name__ == "__main__":
    treap_set = TreapSet()
    treap_set.add(5)
    treap_set.add(3)
    treap_set.add(7)
    print("Contains 3:", 3 in treap_set)
    print("Contains 6:", 6 in treap_set)
    print("Height of tree:", treap_set.height())
    print("Number of items:", len(treap_set))