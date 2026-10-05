def fonk1(text, root):
    b1 = ""
    b2 = root
    for b3 in text:
        if not fonk2(b2) and b3 = = "0":
            b2 = b2.left
        elif not fonk2(b2) and b3 = = "1":
            b2 = b2.right
        if fonk2(b2):
            b1 += b2.val
            b2 = root
    return b1
def fonk2(node):
    return node.left is None and node.right is None