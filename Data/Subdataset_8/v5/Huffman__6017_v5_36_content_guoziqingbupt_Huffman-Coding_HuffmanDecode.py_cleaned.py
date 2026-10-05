def huffman_decode(text, root):
    decoded_text = ""
    current_node = root
    for bit in text:
        if not is_internal_node(current_node):
            decoded_text += current_node.val
            current_node = root
        if bit == "0":
            current_node = current_node.left
        elif bit == "1":
            current_node = current_node.right
    if not is_internal_node(current_node):
        decoded_text += current_node.val
    return decoded_text
def is_internal_node(node):
    return node.left is not None or node.right is not None