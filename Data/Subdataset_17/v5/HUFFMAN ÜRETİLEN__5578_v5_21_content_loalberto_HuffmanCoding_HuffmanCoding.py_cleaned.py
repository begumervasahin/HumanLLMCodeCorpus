import sys
class Node:
    def __init__(self, val, key=''):
        self.key = key
        self.val = val
        self.code = None
        self.left = None
        self.right = None
def fill_codes(node):
    if not node.left and not node.right:
        return
    if node.left:
        node.left.code = '0'
        fill_codes(node.left)
    if node.right:
        node.right.code = '1'
        fill_codes(node.right)
def get_letter_codes(code_dict, node, current_code):
    if not node.left and not node.right:
        code_dict[node.key] = current_code
        return
    if node.left:
        get_letter_codes(code_dict, node.left, current_code + node.left.code)
    if node.right:
        get_letter_codes(code_dict, node.right, current_code + node.right.code)
def huffman_encoding(data):
    if not data:
        return None, None
    frequency = {}
    for char in data:
        frequency[char] = frequency.get(char, 0) + 1
    if len(frequency) == 1:
        single_char = list(frequency.keys())[0]
        root = Node(frequency[single_char])
        root.left = Node(frequency[single_char], single_char)
        root.left.code = '0'
        return '0' * len(data), root
    nodes = [Node(val, key) for key, val in sorted(frequency.items(), key=lambda x: x[1])]
    while len(nodes) > 1:
        left_node = nodes.pop(0)
        right_node = nodes.pop(0)
        internal_node = Node(left_node.val + right_node.val)
        internal_node.left = left_node
        internal_node.right = right_node
        nodes.append(internal_node)
        nodes.sort(key=lambda x: x.val)
    root = nodes[0]
    fill_codes(root)
    code_dict = {}
    get_letter_codes(code_dict, root, '')
    encoded_data = ''.join(code_dict[char] for char in data)
    return encoded_data, root
def huffman_decoding(encoded_data, tree):
    if not encoded_data or not tree:
        return None
    if tree.left is None and tree.right is None:
        return tree.left.key * len(encoded_data)
    decoded_data = ''
    current_node = tree
    for bit in encoded_data:
        current_node = current_node.left if bit == '0' else current_node.right
        if current_node.left is None and current_node.right is None:
            decoded_data += current_node.key
            current_node = tree
    return decoded_data
def main():
    test_sentences = [
        "The bird is the word",
        "The bird is the word23y rkuwejfkjgfkj vduhdqlihoi fhglkrhtieriyweo iwefhli whiflhevidfghierhg",
        None,
        "aaaaaaaa"
    ]
    for sentence in test_sentences:
        print(f"\nOriginal sentence: {sentence}")
        if sentence is not None:
            print(f"Size of original data: {sys.getsizeof(sentence)} bytes")
        try:
            encoded_data, tree = huffman_encoding(sentence)
            if encoded_data:
                print(f"Encoded data: {encoded_data}")
                print(f"Size of encoded data: {sys.getsizeof(int(encoded_data, base=2))} bytes")
            decoded_data = huffman_decoding(encoded_data, tree)
            if decoded_data:
                print(f"Decoded data: {decoded_data}")
                print(f"Size of decoded data: {sys.getsizeof(decoded_data)} bytes")
        except (TypeError, ValueError) as e:
            print(f"Error processing the sentence: {e}")
if __name__ == "__main__":
    main()