import sys
class HuffmanNode:
    def __init__(self, value, key=''):
        self.key = key
        self.value = value
        self.code = None
        self.left = None
        self.right = None
def fill_codes(node):
    if node.left:
        node.left.code = '0'
        fill_codes(node.left)
    if node.right:
        node.right.code = '1'
        fill_codes(node.right)
def get_letter_codes(code_dict, node, current_code):
    if not node.left and not node.right:
        code_dict[node.key] = '{}{}'.format(node.code, current_code)
        return
    get_letter_codes(code_dict, node.left, current_code + node.left.code)
    get_letter_codes(code_dict, node.right, current_code + node.right.code)
def huffman_encoding(data):
    if data is None:
        return None
    frequencies = {}
    for char in data:
        frequencies[char] = frequencies.get(char, 0) + 1
    if len(frequencies) == 1:
        first_node = HuffmanNode(frequencies[data[0]], data[0])
        root = HuffmanNode(first_node.value)
        root.left = first_node
        first_node.code = '0'
        result = '0' * frequencies[data[0]]
        return result, root
    sorted_frequencies = sorted(frequencies.items(), key=lambda x: x[1])
    nodes = [HuffmanNode(value[1], value[0]) for value in sorted_frequencies]
    nodes.append(HuffmanNode(None))
    while len(nodes) > 2:
        left_node = nodes.pop(0)
        if left_node.value is None:
            nodes.append(left_node)
            continue
        right_node = nodes.pop(0)
        if right_node.value is None:
            nodes.append(left_node)
            nodes.append(right_node)
            continue
        internal_node = HuffmanNode(left_node.value + right_node.value)
        internal_node.left = left_node
        internal_node.right = right_node
        nodes.append(internal_node)
    root = nodes.pop(0)
    if root.value is None:
        root = nodes.pop(0)
    fill_codes(root)
    code_dictionary = {}
    get_letter_codes(code_dictionary, root, '')
    encoded_data = ''.join(code_dictionary[char] for char in data)
    return encoded_data, root
def huffman_decoding(encoded_data, decoding_tree):
    if encoded_data is None or decoding_tree is None:
        return None
    if not decoding_tree.right:
        count = len(encoded_data)
        get_letter = decoding_tree.left.key
        return get_letter * count
    final_value = ''
    temp = {}
    get_letter_codes(temp, decoding_tree, '')
    generated_dict = {code: key for key, code in temp.items()}
    current_code = ''
    for char in encoded_data:
        current_code += char
        if current_code in generated_dict:
            final_value += generated_dict[current_code]
            current_code = ''
    return final_value
def replicate_functionality(input_data):
    print("Original Data Size: {}\n".format(sys.getsizeof(input_data)))
    print("Original Data Content: {}\n".format(input_data))
    encoded_data, tree = huffman_encoding(input_data)
    print("Encoded Data Size: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("Encoded Data Content: {}\n".format(encoded_data))
    decoded_data = huffman_decoding(encoded_data, tree)
    print("Decoded Data Size: {}\n".format(sys.getsizeof(decoded_data)))
    print("Decoded Data Content: {}\n".format(decoded_data))
if __name__ == "__main__":
    replicate_functionality("The bird is the word")
    replicate_functionality("The bird is the word23y rkuwejfkjgfkj vduhdqlihoi fhglkrhtieriyweo iwefhli whiflhevidfghierhg")
    replicate_functionality(None)
    replicate_functionality("aaaaaaaa")