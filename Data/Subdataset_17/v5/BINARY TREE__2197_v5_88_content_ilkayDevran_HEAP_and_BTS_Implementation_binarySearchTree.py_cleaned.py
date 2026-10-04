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
        if node:
            self.inorder_tree_walk(node.left)
            print(node.key, end=" ")
            self.inorder_tree_walk(node.right)
    def tree_search(self, key, node=None):
        if node is None:
            node = self.root
        if not node or node.key == key:
            return node
        if key < node.key:
            return self.tree_search(key, node=node.left)
        return self.tree_search(key, node=node.right)
    def tree_minimum(self, node=None):
        if node is None:
            node = self.root
        while node and node.left:
            node = node.left
        return node
    def tree_maximum(self, node=None):
        if node is None:
            node = self.root
        while node and node.right:
            node = node.right
        return node
    def tree_successor(self, key):
        node = self.tree_search(key)
        if node is None:
            return None
        if node.right:
            return self.tree_minimum(node.right)
        parent_node = node.parent
        while parent_node and node == parent_node.right:
            node = parent_node
            parent_node = parent_node.parent
        if parent_node is None:
            print(f"{key} is the largest key, no successor exists")
        return parent_node
    def tree_predecessor(self, key):
        node = self.tree_search(key)
        if node is None:
            return None
        if node.left:
            return self.tree_maximum(node.left)
        parent_node = node.parent
        while parent_node and node == parent_node.left:
            node = parent_node
            parent_node = parent_node.parent
        if parent_node is None:
            print(f"{key} is the smallest key, no predecessor exists")
        return parent_node
    def tree_insert(self, key, node=None):
        if self.root is None:
            self.root = Node(key)
        else:
            if node is None:
                node = self.root
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
            if parent_node:
                if node == parent_node.left:
                    parent_node.left = None
                else:
                    parent_node.right = None
            else:
                self.root = None
        elif node.left is None:
            if parent_node:
                if node == parent_node.left:
                    parent_node.left = node.right
                else:
                    parent_node.right = node.right
                node.right.parent = parent_node
            else:
                self.root = node.right
                self.root.parent = None
        elif node.right is None:
            if parent_node:
                if node == parent_node.left:
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
            if parent_node:
                if node == parent_node.left:
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
        return 1 + max(self.tree_max_path_length(node.left), self.tree_max_path_length(node.right))
    def tree_min_path_length(self, node):
        if node is None:
            return 0
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
    print()
    print(f"SEARCH for {arr[0]} --> {'Key EXISTS!' if t.tree_search(arr[0]) else 'Key does NOT exist!'}")
    print(f"SEARCH for {arr[5]} --> {'Key EXISTS!' if t.tree_search(arr[5]) else 'Key does NOT exist!'}")
    print(f"SEARCH for {arr[0] * 2} --> {'Key EXISTS!' if t.tree_search(arr[0] * 2) else 'Key does NOT exist!'}")
    print(f"Minimum key in the Tree: {t.tree_minimum().key}")
    print(f"Maximum key in the Tree: {t.tree_maximum().key}")
    print(f"Successor of {arr[4]} is {t.tree_successor(arr[4]).key}")
    print(f"Predecessor of {arr[4]} is {t.tree_predecessor(arr[4]).key}")
    print(f"Delete root {arr[0]}: ", end="")
    t.tree_delete(arr[0])
    t.inorder_tree_walk(t.root)
    print()
    print(f"Height of the Tree: {t.tree_max_path_length(t.root)}")
    print(f"Depth of the Tree: {t.tree_min_path_length(t.root)}")
    print(f"Ratio Depth/Height: {t.tree_ratio_length()}")
    print()
def generate_random_array(length, rng):
    return [random.randint(0, length) for _ in range(rng)]
def main():
    create_bst(generate_random_array(30, 100))
    create_bst(generate_random_array(50, 1000))
    create_bst(generate_random_array(100, 500))
if __name__ == '__main__':
    main()