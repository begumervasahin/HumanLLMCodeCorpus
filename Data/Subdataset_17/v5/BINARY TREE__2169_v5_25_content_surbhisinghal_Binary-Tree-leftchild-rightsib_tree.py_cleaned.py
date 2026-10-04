class Node:
    def __init__(self, value):
        self.leftchild = None
        self.rightsib = None
        self.value = value
class Tree:
    def __init__(self):
        self.root = None
    def find(self, target):
        if self.root is not None:
            return self._find_preorder(target, self.root)
        return None
    def _find_preorder(self, target, node):
        if node.value == target:
            return node
        left_result = self._find_preorder(target, node.leftchild) if node.leftchild else None
        right_result = self._find_preorder(target, node.rightsib) if node.rightsib else None
        return left_result if left_result is not None else right_result
    def insert(self, node, parent):
        if self.root is None:
            self.root = node
        else:
            if parent.leftchild is None:
                parent.leftchild = node
            else:
                current = parent.leftchild
                while current.rightsib:
                    current = current.rightsib
                current.rightsib = node
    def delete(self, node, parent=None):
        if node is None:
            return
        if self.root == node:
            self.root = None if self.root.leftchild is None else self.root
            return
        if parent.leftchild == node:
            parent.leftchild = node.rightsib
        else:
            current = parent.leftchild
            while current.rightsib != node:
                current = current.rightsib
            current.rightsib = node.rightsib
def main():
    tree = Tree()
    n1 = Node('A')
    tree.insert(n1, None)
    n2 = Node('B')
    tree.insert(n2, n1)
    n3 = Node('C')
    n4 = Node('D')
    tree.insert(n3, n2)
    tree.insert(n4, n2)
    n5 = Node('E')
    n6 = Node('F')
    n7 = Node('G')
    tree.insert(n5, n1)
    tree.insert(n6, n1)
    tree.insert(n7, n1)
    print(tree.find('F').value)
    print(tree.find('G').value)
    tree.delete(n7, n1)
    print(tree.find('E').value)
if __name__ == "__main__":
    main()