class Node:
    def __init__(self, value):
        self.leftchild = None
        self.rightsib = None
        self.value = value
class Tree:
    def __init__(self):
        self.root = None
    def find(self, target):
        if self.root:
            return self._find_preorder(target, self.root)
        return None
    def _find_preorder(self, target, node):
        if target == node.value:
            return node
        if node.leftchild:
            result = self._find_preorder(target, node.leftchild)
            if result:
                return result
        if node.rightsib:
            return self._find_preorder(target, node.rightsib)
        return None
    def insert(self, node, parent):
        if self.root is None:
            self.root = node
        else:
            if parent.leftchild is None:
                parent.leftchild = node
            else:
                sibling = parent.leftchild
                while sibling.rightsib:
                    sibling = sibling.rightsib
                sibling.rightsib = node
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
                sibling = parent.leftchild
                while sibling.rightsib != node:
                    sibling = sibling.rightsib
                sibling.rightsib = sibling.rightsib.rightsib
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
    found_e = tree.find('E')
    if found_e:
        print(found_e.value)
    else:
        print("Node 'E' not found")
if __name__ == "__main__":
    main()