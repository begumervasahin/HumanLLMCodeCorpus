class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_sibling = None
class Tree:
    def __init__(self):
        self.root = None
    def find(self, target):
        if self.root is not None:
            return self._find_preorder(target, self.root)
        else:
            return None
    def _find_preorder(self, target, node):
        if node is None:
            return None
        if node.value == target:
            return node
        left_result = self._find_preorder(target, node.left_child)
        if left_result:
            return left_result
        right_result = self._find_preorder(target, node.right_sibling)
        if right_result:
            return right_result
        return None
    def insert(self, new_node, parent):
        if self.root is None:
            self.root = new_node
        else:
            current_node = parent.left_child if parent else self.root
            while current_node.right_sibling:
                current_node = current_node.right_sibling
            current_node.right_sibling = new_node
    def delete(self, node, parent=None):
        if node is None:
            return
        if self.root == node:
            if self.root.left_child:
                self.root = None
        else:
            if node == parent.left_child:
                parent.left_child = node.right_sibling
            else:
                current_node = parent.left_child if parent else self.root
                while current_node.right_sibling != node:
                    current_node = current_node.right_sibling
                current_node.right_sibling = node.right_sibling
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