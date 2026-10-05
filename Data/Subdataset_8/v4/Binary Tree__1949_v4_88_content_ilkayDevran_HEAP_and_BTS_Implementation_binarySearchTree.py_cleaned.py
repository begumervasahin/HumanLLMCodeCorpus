class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
class Tree:
    def __init__(self):
        self.root = None
    def Inorder_Tree_Walk(self, node):
        if node is not None:
            self.Inorder_Tree_Walk(node.left)
            print(node.key, end=' ')
            self.Inorder_Tree_Walk(node.right)
    def Tree_search(self, key, node=None):
        if node is None:
            node = self.root
        if self.root.key == key:
            return self.root
        else:
            if node.key == key:
                return node
            elif key < node.key and node.left is not None:
                return self.Tree_search(key, node=node.left)
            elif key > node.key and node.right is not None:
                return self.Tree_search(key, node=node.right)
            else:
                return None
    def Tree_Minimum(self, node=None):
        if node is None:
            node = self.root
        while node.left is not None:
            node = node.left
        return node
    def Tree_Maximum(self, node=None):
        if node is None:
            node = self.root
        while node.right is not None:
            node = node.right
        return node
    def Tree_Successor(self, key, node=None):
        if node is None:
            node = self.Tree_search(key)
            current = node
        if node.right is not None:
            return self.Tree_Minimum(node=node.right)
        parent_node = node.parent
        while parent_node is not None and node is parent_node.right:
            node = parent_node
            parent_node = parent_node.parent
        if parent_node is None:
            print(str(key) + ' is the largest key; no successor exists')
            return current
        else:
            return parent_node
    def Tree_Predecessor(self, key, node=None):
        if node is None:
            node = self.Tree_search(key)
            current = node
        if node.left is not None:
            return self.Tree_Maximum(node=node.left)
        parent_node = node.parent
        while parent_node is not None and node is parent_node.left:
            node = parent_node
            parent_node = parent_node.parent
        if parent_node is None:
            print(str(key) + ' is the largest key; no predecessor exists')
            return current
        else:
            return parent_node
    def Tree_Insert(self, key, node=None):
        if node is None:
            node = self.root
        if self.root is None:
            self.root = Node(key)
        else:
            if key <= node.key:
                if node.left is None:
                    node.left = Node(key)
                    node.left.parent = node
                    return
                else:
                    return self.Tree_Insert(key, node=node.left)
            else:
                if node.right is None:
                    node.right = Node(key)
                    node.right.parent = node
                    return
                else:
                    return self.Tree_Insert(key, node=node.right)
    def Tree_Delete(self, key, node=None):
        if node is None:
            node = self.Tree_search(key)
        if self.root.key == node.key:
            parent_node = self.root
        else:
            parent_node = node.parent
        if node.left is None and node.right is None:
            if key <= parent_node.key:
                parent_node.left = None
            else:
                parent_node.right = None
            return
        if node.left is not None and node.right is None:
            if node.left.key < parent_node.key:
                parent_node.left = node.left
            else:
                parent_node.right = node.left
            return
        if node.right is not None and node.left is None:
            if node.key <= parent_node.key:
                parent_node.left = node.right
            else:
                parent_node.right = node.right
            return
        if node.left is not None and node.right is not None:
            min_value = self.Tree_Minimum(node)
            node.key = min_value.key
            min_value.parent.left = None
            return
    def Tree_max_path_length(self, node):
        if node is None:
            return 0
        else:
            return 1 + max(self.Tree_max_path_length(node.left), self.Tree_max_path_length(node.right))
    def Tree_min_path_length(self, node):
        if node is None:
            return 0
        else:
            return 1 + min(self.Tree_min_path_length(node.left), self.Tree_min_path_length(node.right))
    def Tree_ratio_length(self):
        return self.Tree_min_path_length(self.root) / self.Tree_max_path_length(self.root)
def CREATE_BST(lst):
    t = Tree()
    for i in range(len(lst)):
        t.Tree_Insert(lst[i])
    print("\n---TREE INFO---\n")
    print("INORDER WALK: ", end='')
    t.Inorder_Tree_Walk(t.root)
    print("\nSEARCH for", str(lst[0]), "-->", end=' ')
    if t.Tree_search(lst[0]) is not None:
        print("Key EXISTS!")
    else:
        print("Key does NOT exist!")
    print("SEARCH for", str(lst[5]), "-->", end=' ')
    if t.Tree_search(lst[5]) is not None:
        print("Key EXISTS!")
    else:
        print("Key does NOT exist!")
    print("SEARCH for", str(lst[0] * 2), "-->", end=' ')
    if t.Tree_search(lst[0] * 2) is not None:
        print("Key EXISTS!")
    else:
        print("Key does NOT exist!")
    print("Minimum key in the Tree:", t.Tree_Minimum().key)
    print("Maximum key in the Tree:", t.Tree_Maximum().key)
    print("Successor of", str(lst[4]), "is", t.Tree_Successor(lst[4]).key)
    print("Predecessor of", str(lst[4]), "is", t.Tree_Predecessor(lst[4]).key)
    print("Delete root", str(lst[0]) + ":", end=' ')
    t.Tree_Delete(lst[0])
    t.Inorder_Tree_Walk(t.root)
    print("\nHeight of the Tree:", t.Tree_max_path_length(t.root))
    print("Depth of the Tree:", t.Tree_min_path_length(t.root))
    print("Ratio Depth/Height:", t.Tree_ratio_length(), "\n")
def generateRandomArray(length, rng):
    from random import randint
    lst = [randint(0, length) for _ in range(rng)]
    return lst
def main():
    CREATE_BST(generateRandomArray(30, 100))
    CREATE_BST(generateRandomArray(50, 1000))
    CREATE_BST(generateRandomArray(100, 500))
if __name__ == '__main__':
    main()