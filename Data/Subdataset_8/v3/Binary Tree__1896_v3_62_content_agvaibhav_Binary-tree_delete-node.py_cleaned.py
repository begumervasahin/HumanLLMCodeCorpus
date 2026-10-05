class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def print_level_order(root):
    if root is None:
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
    if root is None:
        return
    inorder_traversal(root.left)
    print(root.data, end=' ')
    inorder_traversal(root.right)
def delete_deepest(root, last):
    if root is None:
        return
    rq = [root]
    while rq:
        node = rq.pop(0)
        if node == last:
            node = None
            return
        if node.right:
            if node.right == last:
                node.right = None
                return
            else:
                rq.append(node.right)
        if node.left:
            if node.left == last:
                node.left = None
                return
            else:
                rq.append(node.left)
def delete_node(root, dele):
    if root is None:
        return
    q = [root]
    key_node = None
    while q:
        node = q.pop(0)
        if node.data == dele:
            key_node = node
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    last = node
    delete_deepest(root, last)
    if key_node:
        key_node.data = last.data
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
    key = 11
    delete_node(root, key)
    print()
    print("The tree after the deletion:")
    inorder_traversal(root)
    print()
    print_level_order(root)