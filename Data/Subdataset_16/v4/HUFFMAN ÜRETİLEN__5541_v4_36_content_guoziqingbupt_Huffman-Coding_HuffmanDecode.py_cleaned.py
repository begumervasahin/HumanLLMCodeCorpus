def fonk1(encoded_text, root):
    b1 = []
    b2 = root
    for b3 in encoded_text:
        if b3 = = "0":
            b2 = b2.left
        elif b3 = = "1":
            b2 = b2.right
        if fonk2(b2):
            b1.append(b2.val)
            b2 = root
    return ''.join(b1)
def fonk2(node):
    return node.left is None and node.right is None