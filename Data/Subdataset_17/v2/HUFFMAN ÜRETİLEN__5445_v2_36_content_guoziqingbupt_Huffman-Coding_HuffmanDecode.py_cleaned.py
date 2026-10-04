class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def is_leaf(node):
    return node.left is None and node.right is None
def huffman_decode(encoded_text, root):
    decoded_text = ""
    current_node = root
    for bit in encoded_text:
        current_node = current_node.left if bit == "0" else current_node.right
        if is_leaf(current_node):
            decoded_text += current_node.val
            current_node = root
    return decoded_text
if __name__ == "__main__":
    root = Node()
    root.left = Node()
    root.right = Node('c')
    root.left.left = Node('a')
    root.left.right = Node('b')
    encoded_text = "000110"
    decoded_text = huffman_decode(encoded_text, root)
    print("Decoded text:", decoded_text)
