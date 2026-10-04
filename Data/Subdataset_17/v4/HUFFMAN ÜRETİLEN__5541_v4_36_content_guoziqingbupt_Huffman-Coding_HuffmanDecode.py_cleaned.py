def huffman_decode(encoded_text, root):
    decoded_text = []
    current_node = root
    for bit in encoded_text:
        if bit == "0":
            current_node = current_node.left
        elif bit == "1":
            current_node = current_node.right
        if is_leaf(current_node):
            decoded_text.append(current_node.val)
            current_node = root
    return ''.join(decoded_text)
def is_leaf(node):
    return node.left is None and node.right is None