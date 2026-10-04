import sys
from tree import BST, Node
traversals = ['zigzag', 'preorder', 'postorder', 'inorder', 'levelorder', 'max_width']
vis = []
def max_width(root):
    q = [{'node': root, 'level': 0}]
    cur_level = []
    best = []
    while q:
        cur = q.pop(0)
        if cur_level and cur_level[0]['level'] != cur['level']:
            if len(cur_level) > len(best):
                best = cur_level[:]
            cur_level = []
        cur_level.append(cur)
        if cur['node'].right:
            q.append({'node': cur['node'].right, 'level': cur['level'] + 1})
        if cur['node'].left:
            q.append({'node': cur['node'].left, 'level': cur['level'] + 1})
    if len(cur_level) > len(best):
        best = cur_level[:]
    vis.append(len(best))
    vis.append("at level")
    best and vis.append(best[0]['level'])
def zigzag(root):
    cur_stack = [root]
    next_stack = []
    go_right = True
    while cur_stack:
        cur = cur_stack.pop()
        vis.append(cur.val)
        if go_right:
            if cur.right:
                next_stack.append(cur.right)
            if cur.left:
                next_stack.append(cur.left)
        else:
            if cur.left:
                next_stack.append(cur.left)
            if cur.right:
                next_stack.append(cur.right)
        if not cur_stack:
            go_right = not go_right
            cur_stack = next_stack[:]
            next_stack = []
def levelorder(root):
    q = [root]
    while q:
        cur = q.pop(0)
        if cur.left:
            q.append(cur.left)
        if cur.right:
            q.append(cur.right)
        vis.append(cur.val)
def preorder(root):
    vis.append(root.val)
    if root.left:
        preorder(root.left)
    if root.right:
        preorder(root.right)
def postorder(root):
    if root.left:
        postorder(root.left)
    if root.right:
        postorder(root.right)
    vis.append(root.val)
def inorder(root):
    if root.left:
        inorder(root.left)
    vis.append(root.val)
    if root.right:
        inorder(root.right)
def main():
    global vis
    default_tree = [5, 6, 1, 2, 5, 8, 3, 10, 12, 13, 15]
    default_tree_two = [5, 4, 3, 2, 1, 6, 7, 8, 9, 10]
    tree = BST()
    for node in default_tree:
        tree.insert(node)
    print("{:11s}: {}".format("Traversal", "Sequence"))
    print("-" * 45)
    run = lambda f, root: globals()[f](root)
    for traversal in traversals:
        run(traversal, tree.root)
        print("{:11s}: {}".format(traversal, ', '.join([str(x) for x in vis])))
        vis = []
if __name__ == "__main__":
    main()