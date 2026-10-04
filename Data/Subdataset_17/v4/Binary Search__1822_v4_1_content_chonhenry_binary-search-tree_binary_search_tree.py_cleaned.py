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
        while current:
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                print(f"Value {value} found.")
                left_val = current.left.value if current.left else 'None'
                right_val = current.right.value if current.right else 'None'
                print(f"Left child: {left_val}")
                print(f"Right child: {right_val}")
                return current
        print("Value not found.")
        return None
    def remove(self, value):
        parent = None
        current = self.root
        while current:
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
                    del current
                elif current.left is None:
                    if parent is None:
                        self.root = current.right
                    elif parent.left == current:
                        parent.left = current.right
                    else:
                        parent.right = current.right
                    del current
                elif current.right is None:
                    if parent is None:
                        self.root = current.left
                    elif parent.left == current:
                        parent.left = current.left
                    else:
                        parent.right = current.left
                    del current
                else:
                    smallest_parent = current
                    smallest = current.right
                    while smallest.left:
                        smallest_parent = smallest
                        smallest = smallest.left
                    current.value = smallest.value
                    if smallest_parent.left == smallest:
                        smallest_parent.left = smallest.right
                    else:
                        smallest_parent.right = smallest.right
                    del smallest
                return
        print("Value not found in the tree.")
    def breadth_first_search(self):
        if self.root is None:
            return []
        current = self.root
        queue = [current]
        result = []
        while queue:
            current = queue.pop(0)
            result.append(current.value)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return result
    def breadth_first_search_recursive(self, queue, arr):
        if len(queue) == 0:
            return arr
        current = queue.pop(0)
        arr.append(current.value)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
        return self.breadth_first_search_recursive(queue, arr)
    def height(self, node):
        if node is None:
            return 0
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
    values = [50, 28, 78, 12, 40, 66, 90, 9, 18, 37, 43, 57, 69, 81, 93, 3, 10, 15, 21, 30, 38, 42, 46, 54, 60, 67, 72, 80, 84, 92, 96, 13, 29, 55, 56]
    for value in values:
        tree.insert(value)
    tree.remove(15)
    print("Breadth-first search:", tree.breadth_first_search())
    print("Height of the tree:", tree.height(tree.root))
    print("Breadth-first search (recursive):", tree.breadth_first_search_recursive([tree.root], []))
    print("\nIn-order traversal:")
    in_order_traversal(tree.root)
    print("\nPre-order traversal:")
    pre_order_traversal(tree.root)
    print("\nPost-order traversal:")
    post_order_traversal(tree.root)