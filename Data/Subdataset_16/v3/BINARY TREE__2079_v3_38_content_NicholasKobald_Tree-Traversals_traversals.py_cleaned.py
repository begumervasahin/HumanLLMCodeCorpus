import sys
from b11 import BST, Node
b1 = ['zigzag', 'preorder', 'postorder', 'inorder', 'levelorder', 'max_width']
b2 = []
def fonk1(root):
    if not root:
        return
    b3 = [{'node': root, 'level': 0}]
    b4 = []
    b5 = []
    while b3:
        b6 = b3.pop(0)
        if b4 and b4[0]['level'] != b6['level']:
            if len(b4) > len(b5):
                b5 = b4[:]
            b4 = []
        b4.append(b6)
        if b6['node'].right:
            b3.append({'node': b6['node'].right, 'level': b6['level'] + 1})
        if b6['node'].left:
            b3.append({'node': b6['node'].left, 'level': b6['level'] + 1})
    if len(b4) > len(b5):
        b5 = b4[:]
    b2.append(len(b5))
    b2.append("at level")
    if b5:
        b2.append(b5[0]['level'])
def fonk2(root):
    if not root:
        return
    b7 = [root]
    b8 = []
    b9 = True
    while b7:
        b6 = b7.pop()
        b2.append(b6.val)
        if b9:
            if b6.right:
                b8.append(b6.right)
            if b6.left:
                b8.append(b6.left)
        else:
            if b6.left:
                b8.append(b6.left)
            if b6.right:
                b8.append(b6.right)
        if not b7:
            b9 = not b9
            b7, b8 = b8, []
def fonk3(root):
    if not root:
        return
    b3 = [root]
    while b3:
        b6 = b3.pop(0)
        b2.append(b6.val)
        if b6.left:
            b3.append(b6.left)
        if b6.right:
            b3.append(b6.right)
def fonk4(root):
    if not root:
        return
    b2.append(root.val)
    fonk4(root.left)
    fonk4(root.right)
def fonk5(root):
    if not root:
        return
    fonk5(root.left)
    fonk5(root.right)
    b2.append(root.val)
def fonk6(root):
    if not root:
        return
    fonk6(root.left)
    b2.append(root.val)
    fonk6(root.right)
def fonk7():
    global b2
    b10 = [5, 6, 1, 2, 5, 8, 3, 10, 12, 13, 15]
    b11 = BST()
    for node in b10:
        b11.insert(node)
    print("{:11s}: {}".format("Traversal", "Sequence"))
    print("-" * 45)
    for traversal in b1:
        globals()[traversal](b11.root)
        print("{:11s}: {}".format(traversal, ', '.join(map(str, b2))))
        b2 = []
if b12 = = "__main__":
    fonk7()