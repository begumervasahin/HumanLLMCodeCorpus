def huffmanDecode(text, root):
    result = ""
    cur = root
    for i in text:
        if not isLeaf(cur) and i == "0":
            cur = cur.left
        elif not isLeaf(cur) and i == "1":
            cur = cur.right
        if isLeaf(cur):
            result += cur.val
            cur = root
    return result
def isLeaf(node):
    return node.left is None and node.right is None