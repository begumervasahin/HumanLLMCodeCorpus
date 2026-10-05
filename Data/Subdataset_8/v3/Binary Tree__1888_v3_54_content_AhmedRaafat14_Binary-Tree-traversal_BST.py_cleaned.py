from queue import Queue
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def display_tree(root, full_depth):
    if root is None:
        return
    if full_depth == 0:
        print(root.data, end=' ')
    display_tree(root.left, full_depth - 1)
    display_tree(root.right, full_depth - 1)
def display_level_order(root):
    if root is None:
        return
    queue = Queue()
    queue.put(root)
    while not queue.empty():
        nodes_at_current_level = queue.qsize()
        while nodes_at_current_level > 0:
            node = queue.get()
            print(node.data, end=' ')
            if node.left:
                queue.put(node.left)
            if node.right:
                queue.put(node.right)
            nodes_at_current_level -= 1
        print("")
root = TreeNode(1)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(2)
root.left.right = TreeNode(8)
root.right.left = TreeNode(3)
root.right.right = TreeNode(7)
root.left.left.left = TreeNode(0)
root.left.left.right = TreeNode(1)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(9)
root.right.right.left = TreeNode(1)
root.right.right.right = TreeNode(10)
display_level_order(root)