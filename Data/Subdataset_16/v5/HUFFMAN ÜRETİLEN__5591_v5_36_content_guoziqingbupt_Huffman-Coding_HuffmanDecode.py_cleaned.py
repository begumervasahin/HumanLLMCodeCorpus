def fonk1(encoded_text, root):
    b1 = []
    b2 = root
    for bit in encoded_text:
        b2 = b2.left if bit == "0" else b2.right
        if fonk2(b2):
            b1.append(b2.val)
            b2 = root
    return ''.join(b1)
def fonk2(node):
    return node.left is None and node.right is None