class Node:
    def __init__(self, word):
        self.word = word
        self.left = None
        self.right = None
        self.count = 1
class BSTree:
    def __init__(self, root=None):
        self.root = root
    def add(self, word):
        if not self.root:
            self.root = Node(word)
        else:
            self._add(self.root, word)
    def find(self, word):
        return self._find(self.root, word)
    def size(self):
        return self._size(self.root)
    def height(self):
        return self._height(self.root)
    def in_order_print(self):
        self._in_order_print(self.root)
    def _add(self, root, word):
        if root.word == word:
            root.count += 1
        elif root.word > word:
            if root.left is None:
                root.left = Node(word)
            else:
                self._add(root.left, word)
        else:
            if root.right is None:
                root.right = Node(word)
            else:
                self._add(root.right, word)
    def _find(self, root, word):
        if root is None:
            return 0
        if root.word == word:
            return root.count
        elif root.word > word:
            return self._find(root.left, word)
        else:
            return self._find(root.right, word)
    def _size(self, root):
        if root is None:
            return 0
        return 1 + self._size(root.left) + self._size(root.right)
    def _height(self, root):
        if root is None:
            return 0
        left_height = self._height(root.left)
        right_height = self._height(root.right)
        return 1 + max(left_height, right_height)
    def _in_order_print(self, root):
        if root is None:
            return
        self._in_order_print(root.left)
        print(f'{root.word}: {root.count}')
        self._in_order_print(root.right)
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