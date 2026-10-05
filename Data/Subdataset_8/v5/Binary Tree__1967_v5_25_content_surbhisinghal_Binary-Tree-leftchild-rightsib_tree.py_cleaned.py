class Node:
    def __init__(self, value):
        self.left_child = None
        self.right_sibling = None
        self.value = value
class Tree:
    def __init__(self):
        self.root = None
    def find(self, target):
        if self.root is not None:
            return self.find_preorder(target, self.root)
        else:
            return None
    def find_preorder(self, target, node):
        if target == node.value:
            return node
        if node.left_child:
            found_node = self.find_preorder(target, node.left_child)
            if found_node:
                return found_node
        if node.right_sibling:
            found_node = self.find_preorder(target, node.right_sibling)
            if found_node:
                return found_node
    def insert(self, new_node, parent):
        if self.root is None:
            self.root = new_node
        else:
            if parent.left_child is None:
                parent.left_child = new_node
            else:
                sibling = parent.left_child
                while sibling.right_sibling is not None:
                    sibling = sibling.right_sibling
                sibling.right_sibling = new_node
    def delete(self, node, parent=None):
        if node is None:
            return
        if self.root == node:
            if self.root.left_child:
                self.root = None
        else:
            if node == parent.left_child:
                parent.left_child = parent.left_child.right_sibling
            else:
                sibling = parent.left_child
                while sibling.right_sibling != node:
                    sibling = sibling.right_sibling
                sibling.right_sibling = sibling.right_sibling.right_sibling
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