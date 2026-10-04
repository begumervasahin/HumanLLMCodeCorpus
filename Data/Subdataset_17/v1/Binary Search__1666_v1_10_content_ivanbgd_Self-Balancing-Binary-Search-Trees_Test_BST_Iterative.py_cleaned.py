class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
    def setParent(self, parent):
        self.parent = parent
    def setLeftChild(self, child):
        self.left = child
        if child:
            child.parent = self
    def setRightChild(self, child):
        self.right = child
        if child:
            child.parent = self
    def printNode(self):
        parent_key = self.parent.key if self.parent else None
        print(f"Node {self.key}: Parent {parent_key}, Left Child {self.left.key if self.left else None}, Right Child {self.right.key if self.right else None}")
class BinarySearchTree:
    def __init__(self, root):
        self.root = root
    def insert(self, key):
        new_node = Node(key)
        current = self.root
        while True:
            if key < current.key:
                if current.left is None:
                    current.setLeftChild(new_node)
                    break
                current = current.left
            else:
                if current.right is None:
                    current.setRightChild(new_node)
                    break
                current = current.right
    def find(self, key):
        current = self.root
        while current and current.key != key:
            if key < current.key:
                current = current.left
            else:
                current = current.right
        return current
    def delete(self, node):
        def transplant(node_to_replace, new_node):
            if node_to_replace.parent is None:
                self.root = new_node
            elif node_to_replace == node_to_replace.parent.left:
                node_to_replace.parent.left = new_node
            else:
                node_to_replace.parent.right = new_node
            if new_node:
                new_node.parent = node_to_replace.parent
        if node.left is None:
            transplant(node, node.right)
        elif node.right is None:
            transplant(node, node.left)
        else:
            successor = self.min_value_node(node.right)
            if successor.parent != node:
                transplant(successor, successor.right)
                successor.right = node.right
                successor.right.parent = successor
            transplant(node, successor)
            successor.left = node.left
            successor.left.parent = successor
    def min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    def inOrder(self):
        def _inOrder(node):
            return _inOrder(node.left) + [node.key] + _inOrder(node.right) if node else []
        return _inOrder(self.root)
    def preOrder(self):
        def _preOrder(node):
            return [node.key] + _preOrder(node.left) + _preOrder(node.right) if node else []
        return _preOrder(self.root)
    def postOrder(self):
        def _postOrder(node):
            return _postOrder(node.left) + _postOrder(node.right) + [node.key] if node else []
        return _postOrder(self.root)
    def BFS(self):
        queue = [self.root]
        result = []
        while queue:
            node = queue.pop(0)
            result.append(node.key)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result
    def rotateLeft(self, node):
        y = node.right
        if y:
            node.setRightChild(y.left)
            if node.parent is None:
                self.root = y
            elif node == node.parent.left:
                node.parent.setLeftChild(y)
            else:
                node.parent.setRightChild(y)
            y.setLeftChild(node)
    def rotateRight(self, node):
        y = node.left
        if y:
            node.setLeftChild(y.right)
            if node.parent is None:
                self.root = y
            elif node == node.parent.right:
                node.parent.setRightChild(y)
            else:
                node.parent.setLeftChild(y)
            y.setRightChild(node)
    def getRoot(self):
        return self.root
    def rangeSearch(self, low, high):
        def _rangeSearch(node, low, high):
            if not node:
                return []
            result = []
            if low <= node.key <= high:
                result.append(node.key)
            if low < node.key:
                result += _rangeSearch(node.left, low, high)
            if node.key < high:
                result += _rangeSearch(node.right, low, high)
            return result
        return _rangeSearch(self.root, low, high)
def printTree(bst, verbose=False):
    print()
    print("In order:  ", bst.inOrder())
    print("Pre order: ", bst.preOrder())
    print("BFS:       ", bst.BFS())
    if verbose:
        print("Nodes (in BFS order):")
        nodes = bst.BFS()
        for node_key in nodes:
            bst.find(node_key).printNode()
    print()
def createTree():
    bst = BinarySearchTree(Node(7))
    bst.insert(4)
    bst.insert(1)
    bst.insert(6)
    bst.insert(13)
    bst.insert(15)
    bst.insert(10)
    return bst, bst.getRoot()
def testTree():
    bst, root = createTree()
    print("\nPrint:")
    print("In order:  ", bst.inOrder())
    print("Pre order: ", bst.preOrder())
    print("Post order:", bst.postOrder())
    print("BFS:       ", bst.BFS())
    print("Root:", end=' ')
    root.printNode()
    print("\nFind:")
    for i in [0, 1, 2, 5, 6, 7, 8, 12, 13, 14, 15, 20]:
        found = bst.find(i)
        print(i, found.key if found else None)
    print("\nNext:")
    for i in [0, 1, 2, 4, 5, 6, 7, 8, 10, 12, 14, 15, 16]:
        found = bst.find(i)
        next_node = bst.find(i + 1)
        print(i, next_node.key if next_node else None)
    print("\nPrevious:")
    for i in [0, 1, 2, 4, 5, 6, 7, 8, 10, 12, 14, 15, 16]:
        found = bst.find(i)
        prev_node = bst.find(i - 1)
        print(i, prev_node.key if prev_node else None)
    print("\nRange search:")
    for node in bst.rangeSearch(5, 12):
        print(node, end=' ')
    print()
    if 0:
        print("\nInsert:")
        print("In order:  ", bst.inOrder())
        print("Pre order: ", bst.preOrder())
        print("BFS:       ", bst.BFS())
        n = 3
        bst.insert(n)
        node = bst.find(n)
        node.printNode()
        node.getParent().printNode()
        print("Inserting", n)
        print("In order:  ", bst.inOrder())
        print("Pre order: ", bst.preOrder())
        print("BFS:       ", bst.BFS())
    if 0:
        print("\nDelete:")
        print("In order:  ", bst.inOrder())
        print("Pre order: ", bst.preOrder())
        print("BFS:       ", bst.BFS())
        n = 7
        bst.delete(bst.find(n))
        print("Deleting", n)
        print("In order:  ", bst.inOrder())
        print("Pre order: ", bst.preOrder())
        print("BFS:       ", bst.BFS())
        print("This is the node under which the deleted node, {}, would come: {}.".format(n, bst.find(n)))
        bst.find(n).printNode()
        try:
            bst.find(n).getParent().printNode()
        except:
            print("New root:", end=' ')
            bst.find(root.key).printNode()
        print("Root is:", end=' ')
        bst.getRoot().printNode()
    print("\nRotate right:")
    printTree(bst, True)
    n = 7
    bst.rotateRight(bst.find(n))
    print("Rotating right", n)
    printTree(bst, True)
    bst.find(n).printNode()
    print("\nRotate left:")
    printTree(bst, True)
    n = 1
    bst.rotateLeft(bst.find(n))
    print("Rotating left", n)
    printTree(bst, True)
    bst.find(n).printNode()
def test1():
    bst = BinarySearchTree(Node(3))
    bst.insert(1)
    bst.insert(4)
    bst.insert(5)
    printTree(bst, True)
    bst.delete(bst.find(3))
    printTree(bst, True)
def test2():
    bst, root = createTree()
    printTree(bst, True)
    bst.delete(bst.find(7))
    printTree(bst, True)
testTree()