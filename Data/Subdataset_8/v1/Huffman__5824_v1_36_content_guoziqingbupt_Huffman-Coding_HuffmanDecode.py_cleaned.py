class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
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
root = TreeNode('*')
root.left = TreeNode('A')
root.right = TreeNode('*')
root.right.left = TreeNode('B')
root.right.right = TreeNode('*')
root.right.right.left = TreeNode('C')
root.right.right.right = TreeNode('D')
encoded_text = "010101001010101001011110"
decoded_text = huffmanDecode(encoded_text, root)
print("Decoded text:", decoded_text)