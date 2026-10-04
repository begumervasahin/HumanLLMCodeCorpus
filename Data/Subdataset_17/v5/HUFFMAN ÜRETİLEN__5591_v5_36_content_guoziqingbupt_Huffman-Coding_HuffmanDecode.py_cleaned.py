def huffman_decode(encoded_text, root):
    decoded_text = []
    current_node = root
    for bit in encoded_text:
        current_node = current_node.left if bit == "0" else current_node.right
        if is_leaf(current_node):
            decoded_text.append(current_node.val)
            current_node = root
    return ''.join(decoded_text)
def is_leaf(node):
    return node.left is None and node.right is None