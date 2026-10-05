import sys
from tree import BST, Node
TRAVERSALS = ['zigzag', 'preorder', 'postorder', 'inorder', 'levelorder', 'max_width']
VISITED_NODES = []
def max_width(root):
    queue = [{'node': root, 'level': 0}]
    current_level = []
    best = []
    while queue:
        current = queue.pop(0)
        if current_level and current_level[0]['level'] != current['level']:
            if len(current_level) > len(best):
                best = current_level[:]
            current_level = []
        current_level.append(current)
        if current['node'].right:
            queue.append({'node': current['node'].right, 'level': current['level'] + 1})
        if current['node'].left:
            queue.append({'node': current['node'].left, 'level': current['level'] + 1})
    VISITED_NODES.append(len(best))
    VISITED_NODES.append("at level")
    best and VISITED_NODES.append(best[0]['level'])
def zigzag(root):
    current_stack = [root]
    next_stack = []
    go_right = True
    while current_stack:
        current = current_stack.pop()
        VISITED_NODES.append(current.val)
        if go_right:
            if current.right:
                next_stack.append(current.right)
            if current.left:
                next_stack.append(current.left)
        else:
            if current.left:
                next_stack.append(current.left)
            if current.right:
                next_stack.append(current.right)
        if not current_stack:
            go_right = not go_right
            current_stack = next_stack[:]
            next_stack = []
def levelorder(root):
    queue = [root]
    while queue:
        current = queue.pop(0)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
        VISITED_NODES.append(current.val)
def preorder(root):
    VISITED_NODES.append(root.val)
    if root.left:
        preorder(root.left)
    if root.right:
        preorder(root.right)
def postorder(root):
    if root.left:
        postorder(root.left)
    if root.right:
        postorder(root.right)
    VISITED_NODES.append(root.val)
def inorder(root):
    if root.left:
        inorder(root.left)
    VISITED_NODES.append(root.val)
    if root.right:
        inorder(root.right)
def main():
    global VISITED_NODES
    default_tree = [5, 6, 1, 2, 5, 8, 3, 10, 12, 13, 15]
    tree = BST()
    [tree.insert(node) for node in default_tree]
    print("{:11s}: {}".format("Traversal", "Sequence"))
    print("-" * 45)
    for traversal in TRAVERSALS:
        globals()[traversal](tree.root)
        print("{:11s}: {}".format(traversal, ', '.join([str(x) for x in VISITED_NODES])))
        VISITED_NODES = []
if __name__ == "__main__":
    main()