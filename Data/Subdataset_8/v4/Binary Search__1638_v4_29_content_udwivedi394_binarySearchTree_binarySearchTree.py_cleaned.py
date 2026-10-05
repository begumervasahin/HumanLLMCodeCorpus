class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BinarySearchTree:
    def __init__(self):
        self.root = None
    def add_node(self, data):
        if self.root is None:
            self.root = Node(data)
            return
        temp = self.root
        while temp:
            prev_node = temp
            if data < temp.data:
                temp = temp.left
            else:
                temp = temp.right
        if data < prev_node.data:
            prev_node.left = Node(data)
        else:
            prev_node.right = Node(data)
    def in_order_traversal(self):
        if self.root is None:
            print("Tree is empty")
            return
        print("\nIn Order Traversal:", end=" ")
        stack = []
        temp = self.root
        while True:
            while temp:
                stack.append(temp)
                temp = temp.left
            while not temp and stack:
                temp = stack.pop()
                print(temp.data, end=" ")
                temp = temp.right
            if not temp and not stack:
                break
        print()
    def level_order_traversal(self):
        if self.root is None:
            print("Tree is empty")
            return
        print("\nLevel Order Traversal:")
        queue = [self.root]
        while queue:
            n = len(queue)
            for _ in range(n):
                temp = queue.pop(0)
                print(temp.data, end=" ")
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
            print()
    def search_data(self, data):
        if self.root is None:
            print("Tree is empty")
            return False
        temp = self.root
        while temp:
            if temp.data == data:
                print("%d found!" % data)
                return True
            elif data < temp.data:
                temp = temp.left
            else:
                temp = temp.right
        print("%d not present" % data)
        return False
    def delete_node(self, data):
        if self.root is None:
            print("Tree is empty")
            return False
        parent = None
        current = self.root
        while current and current.data != data:
            parent = current
            if data < current.data:
                current = current.left
            else:
                current = current.right
        if not current:
            print("Node not found")
            return False
        if not current.left or not current.right:
            if not current.left:
                child = current.right
            else:
                child = current.left
            if not parent:
                self.root = child
            elif current is parent.left:
                parent.left = child
            else:
                parent.right = child
        else:
            successor = current.right
            successor_parent = current
            while successor.left:
                successor_parent = successor
                successor = successor.left
            current.data = successor.data
            if successor is not current.right:
                successor_parent.left = successor.right
            else:
                successor_parent.right = successor.right
        return True
    def kth_node_in_order(self, k):
        if self.root is None:
            print("Tree is empty")
            return
        stack = []
        temp = self.root
        while True:
            while temp:
                stack.append(temp)
                temp = temp.left
            while not temp and stack:
                temp = stack.pop()
                k -= 1
                if k == 0:
                    print(temp.data, end=" ")
                    return
                temp = temp.right
            if not temp and not stack:
                break
    def inorder_successor(self, data):
        if self.root is None:
            print("Tree is empty")
            return
        temp = self.root
        successor = None
        while temp:
            if data == temp.data:
                break
            elif data < temp.data:
                successor = temp
                temp = temp.left
            else:
                temp = temp.right
        if not temp:
            print("Element not found")
            return
        if temp.right:
            temp = temp.right
            while temp.left:
                temp = temp.left
            return temp.data
        return successor.data if successor else None
    def get_root(self):
        return self.root
bst = BinarySearchTree()
bst.add_node(50)
bst.add_node(30)
bst.add_node(20)
bst.add_node(40)
bst.add_node(70)
bst.add_node(60)
bst.add_node(80)
print("Inorder Traversal:")
bst.in_order_traversal()
print("\nLevel Order Traversal:")
bst.level_order_traversal()
bst.delete_node(20)
bst.delete_node(30)
print("\nInorder Traversal after deleting 20 and 30:")
bst.in_order_traversal()
print("\nKth node (2nd) in Inorder Traversal:")
bst.kth_node_in_order(2)
print("\nInorder Successor of 50:")
print(bst.inorder_successor(50))