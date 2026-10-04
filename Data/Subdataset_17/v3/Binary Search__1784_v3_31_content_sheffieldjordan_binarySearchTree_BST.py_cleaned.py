class Node:
    def __init__(self, word):
        self.word = word
        self.left = None
        self.right = None
        self.count = 1
class BSTree:
    def __init__(self):
        self.root = None
    def add(self, word):
        if self.root is None:
            self.root = Node(word)
        else:
            self._add_recursive(self.root, word)
    def find(self, word):
        return self._find_recursive(self.root, word)
    def size(self):
        return self._calculate_size(self.root)
    def height(self):
        return self._calculate_height(self.root)
    def in_order_print(self):
        self._print_in_order(self.root)
    def _add_recursive(self, node, word):
        if node.word == word:
            node.count += 1
        elif word < node.word:
            if node.left is None:
                node.left = Node(word)
            else:
                self._add_recursive(node.left, word)
        else:
            if node.right is None:
                node.right = Node(word)
            else:
                self._add_recursive(node.right, word)
    def _find_recursive(self, node, word):
        if node is None:
            return 0
        if node.word == word:
            return node.count
        elif word < node.word:
            return self._find_recursive(node.left, word)
        else:
            return self._find_recursive(node.right, word)
    def _calculate_size(self, node):
        if node is None:
            return 0
        return 1 + self._calculate_size(node.left) + self._calculate_size(node.right)
    def _calculate_height(self, node):
        if node is None:
            return 0
        left_height = self._calculate_height(node.left)
        right_height = self._calculate_height(node.right)
        return 1 + max(left_height, right_height)
    def _print_in_order(self, node):
        if node is None:
            return
        self._print_in_order(node.left)
        print(f'{node.word}: {node.count}')
        self._print_in_order(node.right)
if __name__ == "__main__":
    bst = BSTree()
    words = ["apple", "banana", "apple", "orange", "banana", "apple", "orange", "orange"]
    for word in words:
        bst.add(word)
    print("In-order traversal of the BST:")
    bst.in_order_print()
    print("\nSize of the BST:", bst.size())
    print("Height of the BST:", bst.height())
    word_to_find = "apple"
    print(f"\nOccurrences of '{word_to_find}':", bst.find(word_to_find))