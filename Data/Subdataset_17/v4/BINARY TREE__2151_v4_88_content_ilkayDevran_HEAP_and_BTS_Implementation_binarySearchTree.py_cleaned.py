from __future__ import division
import random
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
class Tree:
    def __init__(self):
        self.root = None
    def inorder_tree_walk(self, node):
        if node is not None:
            self.inorder_tree_walk(node.left)
            print(node.key, end=" ")
            self.inorder_tree_walk(node.right)
    def tree_search(self, key, node=None):
        if node is None:
            node = self.root
        if node.key == key:
            return node
        elif key < node.key and node.left is not None:
            return self.tree_search(key, node=node.left)
        elif key > node.key and node.right is not None:
            return self.tree_search(key, node=node.right)
        else:
            return None
    def tree_minimum(self, node=None):
        if node is None:
            node = self.root
        while node.left is not None:
            node = node.left
        return node
    def tree_maximum(self, node=None):
        if node is None:
            node = self.root
        while node.right is not None:
            node = node.right
        return node
    def tree_successor(self, key):
        node = self.tree_search(key)
        if node is None:
            return None
        if node.right is not None:
            return self.tree_minimum(node=node.right)
        parent_node = node.parent
        while parent_node is not None and node == parent_node.right:
            node = parent_node
            parent_node = parent_node.parent
        if parent_node is None:
            print(f"{key} is the largest key, no successor exists")
            return node
        else:
            return parent_node
    def tree_predecessor(self, key):
        node = self.tree_search(key)
        if node is None:
            return None
        if node.left is not None:
            return self.tree_maximum(node=node.left)
        parent_node = node.parent
        while parent_node is not None and node == parent_node.left:
            node = parent_node
            parent_node = parent_node.parent
        if parent_node is None:
            print(f"{key} is the smallest key, no predecessor exists")
            return node
        else:
            return parent_node
    def tree_insert(self, key, node=None):
        if node is None:
            node = self.root
        if self.root is None:
            self.root = Node(key)
        else:
            if key <= node.key:
                if node.left is None:
                    node.left = Node(key)
                    node.left.parent = node
                else:
                    self.tree_insert(key, node=node.left)
            else:
                if node.right is None:
                    node.right = Node(key)
                    node.right.parent = node
                else:
                    self.tree_insert(key, node=node.right)
    def tree_delete(self, key):
        node = self.tree_search(key)
        if node is None:
            return
        parent_node = node.parent
        if node.left is None and node.right is None:
            if parent_node is not None:
                if key <= parent_node.key:
                    parent_node.left = None
                else:
                    parent_node.right = None
            else:
                self.root = None
        elif node.left is None:
            if parent_node is not None:
                if key <= parent_node.key:
                    parent_node.left = node.right
                else:
                    parent_node.right = node.right
                node.right.parent = parent_node
            else:
                self.root = node.right
                self.root.parent = None
        elif node.right is None:
            if parent_node is not None:
                if key <= parent_node.key:
                    parent_node.left = node.left
                else:
                    parent_node.right = node.left
                node.left.parent = parent_node
            else:
                self.root = node.left
                self.root.parent = None
        else:
            successor = self.tree_minimum(node.right)
            if successor.parent != node:
                self.tree_delete(successor.key)
                successor.right = node.right
                node.right.parent = successor
            if parent_node is not None:
                if key <= parent_node.key:
                    parent_node.left = successor
                else:
                    parent_node.right = successor
            else:
                self.root = successor
            successor.parent = parent_node
            successor.left = node.left
            node.left.parent = successor
    def tree_max_path_length(self, node):
        if node is None:
            return 0
        else:
            return 1 + max(self.tree_max_path_length(node.left), self.tree_max_path_length(node.right))
    def tree_min_path_length(self, node):
        if node is None:
            return 0
        else:
            return 1 + min(self.tree_min_path_length(node.left), self.tree_min_path_length(node.right))
    def tree_ratio_length(self):
        return self.tree_min_path_length(self.root) / self.tree_max_path_length(self.root)
def create_bst(arr):
    t = Tree()
    for key in arr:
        t.tree_insert(key)
    print("\n--- TREE INFO ---\n")
    print("INORDER WALK: ", end="")
    t.inorder_tree_walk(t.root)
    print("\nSEARCH for " + str(arr[0]) + "\t--> ", end="")
    if t.tree_search(arr[0]) is not None:
        print("Key EXISTS!")
    else:
        print("Key does NOT exist!")
    print("SEARCH for " + str(arr[5]) + "\t--> ", end="")
    if t.tree_search(arr[5]) is not None:
        print("Key EXISTS!")
    else:
        print("Key does NOT exist!")
    print("SEARCH for " + str(arr[0] * 2) + "\t--> ", end="")
    if t.tree_search(arr[0] * 2) is not None:
        print("Key EXISTS!")
    else:
        print("Key does NOT exist!")
    print("Minimum key in the Tree: " + str(t.tree_minimum().key))
    print("Maximum key in the Tree: " + str(t.tree_maximum().key))
    print("Successor of " + str(arr[4]) + " is", t.tree_successor(arr[4]).key)
    print("Predecessor of " + str(arr[4]) + " is", t.tree_predecessor(arr[4]).key)
    print("Delete root " + str(arr[0]) + ": ", end="")
    t.tree_delete(arr[0])
    t.inorder_tree_walk(t.root)
    print("\nHeight of the Tree: " + str(t.tree_max_path_length(t.root)))
    print("Depth of the Tree: " + str(t.tree_min_path_length(t.root)))
    print("Ratio Depth/Height: " + str(t.tree_ratio_length()))
    print("\n")
def generate_random_array(length, rng):
    return [random.randint(0, length) for _ in range(rng)]
def main():
    create_bst(generate_random_array(30, 100))
    create_bst(generate_random_array(50, 1000))
    create_bst(generate_random_array(100, 500))
if __name__ == '__main__':
    main()