class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class BinarySearchTree:
    def __init__(self):
        self.root = None
    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            while True:
                if value < current.value:
                    if current.left is None:
                        current.left = new_node
                        break
                    current = current.left
                elif value > current.value:
                    if current.right is None:
                        current.right = new_node
                        break
                    current = current.right
                else:
                    break
    def lookup(self, value):
        current = self.root
        while current is not None:
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                print(f'Value {value} found:')
                print(f'Left child: {current.left.value if current.left else "None"}')
                print(f'Right child: {current.right.value if current.right else "None"}')
                return
        print('Value not found')
    def remove(self, value):
        parent = None
        current = self.root
        while current is not None:
            if value < current.value:
                parent = current
                current = current.left
            elif value > current.value:
                parent = current
                current = current.right
            else:
                if current.left is None and current.right is None:
                    if parent is None:
                        self.root = None
                    elif parent.left == current:
                        parent.left = None
                    else:
                        parent.right = None
                elif current.left is None:
                    if parent is None:
                        self.root = current.right
                    elif parent.left == current:
                        parent.left = current.right
                    else:
                        parent.right = current.right
                elif current.right is None:
                    if parent is None:
                        self.root = current.left
                    elif parent.left == current:
                        parent.left = current.left
                    else:
                        parent.right = current.left
                else:
                    successor = self._find_minimum(current.right)
                    successor_value = successor.value
                    self.remove(successor_value)
                    current.value = successor_value
                return
        print("Value not found")
    def _find_minimum(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    def breadth_first_search(self):
        current = self.root
        result = []
        queue = []
        if current:
            queue.append(current)
        while queue:
            current = queue.pop(0)
            result.append(current.value)
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)
        return result
    def breadth_first_search_recursive(self, queue, result):
        if not queue:
            return result
        current = queue.pop(0)
        result.append(current.value)
        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)
        return self.breadth_first_search_recursive(queue, result)
    def height(self, node):
        if node is None:
            return 0
        else:
            return 1 + max(self.height(node.left), self.height(node.right))
def in_order_traversal(root):
    if root:
        in_order_traversal(root.left)
        print(root.value)
        in_order_traversal(root.right)
def pre_order_traversal(root):
    if root:
        print(root.value)
        pre_order_traversal(root.left)
        pre_order_traversal(root.right)
def post_order_traversal(root):
    if root:
        post_order_traversal(root.left)
        post_order_traversal(root.right)
        print(root.value)
if __name__ == "__main__":
    tree = BinarySearchTree()
    elements = [
        50, 28, 78, 12, 40, 66, 90, 9, 18, 37, 43, 57, 69, 81, 93, 3, 10, 15, 21,
        30, 38, 42, 46, 54, 60, 67, 72, 80, 84, 92, 96, 13, 29, 55, 56
    ]
    for el in elements:
        tree.insert(el)
    tree.remove(15)
    print("Breadth-First Search:", tree.breadth_first_search())
    print('Height of the tree:', tree.height(tree.root))
    print("Breadth-First Search (Recursive):", tree.breadth_first_search_recursive([tree.root], []))
    print('In-Order Traversal:')
    in_order_traversal(tree.root)
    print('Pre-Order Traversal:')
    pre_order_traversal(tree.root)
    print('Post-Order Traversal:')
    post_order_traversal(tree.root)