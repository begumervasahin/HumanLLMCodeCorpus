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
        else:
            return None
    def _find_preorder(self, target, node):
        x = y = None
        if target == node.value:
            return node
        if node.leftchild:
            x = self._find_preorder(target, node.leftchild)
        if node.rightsib:
            y = self._find_preorder(target, node.rightsib)
        if x is not None:
            return x
        elif y is not None:
            return y
    def insert(self, new_node, parent):
        if self.root is None:
            self.root = new_node
        else:
            if parent.leftchild is None:
                parent.leftchild = new_node
            else:
                parent = parent.leftchild
                while parent.rightsib is not None:
                    parent = parent.rightsib
                parent.rightsib = new_node
    def delete(self, node, parent=None):
        if node is None:
            return
        if self.root == node:
            if self.root.leftchild:
                self.root = None
        else:
            if node == parent.leftchild:
                parent.leftchild = parent.leftchild.rightsib
            else:
                parent = parent.leftchild
                while parent.rightsib != node:
                    parent = parent.rightsib
                parent.rightsib = parent.rightsib.rightsib
def main():
    tree = Tree()
    n1 = Node('A')
    tree.insert(n1, None)
    n2 = Node('B')
    tree.insert(n2, n1)
    n3 = Node('C')
    n4 = Node('D')
    tree.insert(n4, n2)
    tree.insert(n3, n2)
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