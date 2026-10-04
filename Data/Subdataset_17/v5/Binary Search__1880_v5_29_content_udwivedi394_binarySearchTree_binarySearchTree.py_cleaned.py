class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BST:
    def __init__(self):
        self.root = None
    def add_node(self, data):
        if not self.root:
            self.root = Node(data)
            return
        current = self.root
        while True:
            if data < current.data:
                if current.left is None:
                    current.left = Node(data)
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = Node(data)
                    break
                current = current.right
    def in_order(self):
        if not self.root:
            print("Tree is empty")
            return
        print("\nIn Order:", end=" ")
        stack = []
        current = self.root
        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            print(current.data, end=" ")
            current = current.right
        print()
    def level_order(self):
        if not self.root:
            print("Tree is empty")
            return
        print("\nLevel Order:")
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            print(current.data, end=" ")
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        print()
    def search(self, data):
        current = self.root
        while current:
            if current.data == data:
                print(f"{data} found!")
                return True
            current = current.left if data < current.data else current.right
        print(f"{data} not found")
        return False
    def _find_with_parent(self, data):
        current = self.root
        parent = None
        while current and current.data != data:
            parent = current
            current = current.left if data < current.data else current.right
        return parent, current
    def delete_node(self, data):
        parent, node_to_delete = self._find_with_parent(data)
        if node_to_delete is None:
            print(f"Node with data {data} not found!")
            return False
        if node_to_delete.left is None or node_to_delete.right is None:
            child = node_to_delete.left if node_to_delete.left else node_to_delete.right
            if parent is None:
                self.root = child
            elif node_to_delete == parent.left:
                parent.left = child
            else:
                parent.right = child
        else:
            successor_parent = node_to_delete
            successor = node_to_delete.right
            while successor.left:
                successor_parent = successor
                successor = successor.left
            node_to_delete.data = successor.data
            if successor_parent.left == successor:
                successor_parent.left = successor.right
            else:
                successor_parent.right = successor.right
    def search_kth_node(self, k):
        stack = []
        current = self.root
        count = 0
        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            count += 1
            if count == k:
                print(f"{k}-th smallest element is {current.data}")
                return current.data
            current = current.right
        print(f"{k}-th smallest element not found")
        return None
    def in_order_successor(self, data):
        current = self.root
        successor = None
        while current:
            if data < current.data:
                successor = current
                current = current.left
            elif data > current.data:
                current = current.right
            else:
                if current.right:
                    successor = current.right
                    while successor.left:
                        successor = successor.left
                break
        if successor:
            print(f"In-order successor of {data} is {successor.data}")
            return successor.data
        else:
            print(f"No successor found for {data}")
            return None
    def get_root(self):
        return self.root