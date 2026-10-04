class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def print_level_order(root):
    if not root:
        return
    queue = [root]
    while queue:
        node = queue.pop(0)
        print(node.data, end=' ')
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
def inorder_traversal(root):
    if not root:
        return
    inorder_traversal(root.left)
    print(root.data, end=' ')
    inorder_traversal(root.right)
def delete_deepest(root, d_node):
    if not root:
        return
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node == d_node:
            node = None
            return
        if node.right:
            if node.right == d_node:
                node.right = None
                return
            else:
                queue.append(node.right)
        if node.left:
            if node.left == d_node:
                node.left = None
                return
            else:
                queue.append(node.left)
def delete_node(root, key):
    if not root:
        return None
    if root.left is None and root.right is None:
        if root.data == key:
            return None
        else:
            return root
    key_node = None
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node.data == key:
            key_node = node
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    if key_node:
        x = node.data
        delete_deepest(root, node)
        key_node.data = x
    return root
if __name__ == '__main__':
    root = Node(10)
    root.left = Node(11)
    root.left.left = Node(7)
    root.left.right = Node(12)
    root.right = Node(9)
    root.right.left = Node(15)
    root.right.right = Node(8)
    print("The tree before the deletion:")
    inorder_traversal(root)
    print()
    print_level_order(root)
    print()
    key = 11
    root = delete_node(root, key)
    print("The tree after the deletion:")
    inorder_traversal(root)
    print()
    print_level_order(root)
    print()