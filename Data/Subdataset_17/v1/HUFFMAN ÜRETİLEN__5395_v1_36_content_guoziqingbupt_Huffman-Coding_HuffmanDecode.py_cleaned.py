class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def isLeaf(node):
    return node.left is None and node.right is None
def huffmanDecode(text, root):
    result = ""
    cur = root
    for bit in text:
        if not isLeaf(cur):
            if bit == "0":
                cur = cur.left
            elif bit == "1":
                cur = cur.right
        if isLeaf(cur):
            result += cur.val
            cur = root
    return result
if __name__ == "__main__":
    root = Node()
    root.left = Node()
    root.right = Node('c')
    root.left.left = Node('a')
    root.left.right = Node('b')
    encoded_text = "000110"
    decoded_text = huffmanDecode(encoded_text, root)
    print("Decoded text:", decoded_text)
