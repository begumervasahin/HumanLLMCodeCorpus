class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def huffman_decode(text, root):
    result = ""
    current_node = root
    for bit in text:
        if not is_leaf(current_node) and bit == "0":
            current_node = current_node.left
        elif not is_leaf(current_node) and bit == "1":
            current_node = current_node.right
        if is_leaf(current_node):
            result += current_node.val
            current_node = root
    return result
def is_leaf(node):
    return node.left is None and node.right is None
root = TreeNode('*')
root.left = TreeNode('A')
root.right = TreeNode('*')
root.right.left = TreeNode('B')
root.right.right = TreeNode('*')
root.right.right.left = TreeNode('C')
root.right.right.right = TreeNode('D')
encoded_text = "010101001010101001011110"
decoded_text = huffman_decode(encoded_text, root)
print("Decoded text:", decoded_text)