import sys
class Node:
    def __init__(self, val, key=''):
        self.key = key
        self.val = val
        self.code = None
        self.left = None
        self.right = None
def fill_codes(node):
    if node.left is None and node.right is None:
        return
    if node.left is not None:
        node.left.code = '0'
        fill_codes(node.left)
    if node.right is not None:
        node.right.code = '1'
        fill_codes(node.right)
def get_letter_codes(di, node, val):
    if node.left is None and node.right is None:
        di[node.key] = '{}{}'.format(node.code, val)
        return
    get_letter_codes(di, node.left, val + node.left.code)
    get_letter_codes(di, node.right, val + node.right.code)
def build_huffman_tree(data):
    if data is None:
        return None
    val = {}
    for char in data:
        val[char] = val.get(char, 0) + 1
    if len(val) == 1:
        first_node = Node(val[data[0]], data[0])
        root = Node(first_node.val)
        root.left = first_node
        first_node.code = '0'
        result = '0' * val[data[0]]
        return result, root
    sorted_values = sorted(val.items(), key=lambda x: x[1])
    nodes = [Node(value[1], value[0]) for value in sorted_values]
    nodes.append(Node(None))
    while len(nodes) > 2:
        left_node = nodes.pop(0)
        if left_node.val is None:
            nodes.append(left_node)
            continue
        right_node = nodes.pop(0)
        if right_node.val is None:
            nodes.append(left_node)
            nodes.append(right_node)
            continue
        internal_node = Node(left_node.val + right_node.val)
        internal_node.left = left_node
        internal_node.right = right_node
        nodes.append(internal_node)
    root = nodes.pop(0)
    if root.val is None:
        root = nodes.pop(0)
    fill_codes(root)
    return root
def huffman_encoding(data):
    tree = build_huffman_tree(data)
    if tree is None:
        return None
    di = {}
    get_letter_codes(di, tree, '')
    encoded_data = ''.join(di[char] for char in data)
    return encoded_data, tree
def huffman_decoding(data, dec_tree):
    if data is None or dec_tree is None:
        return None
    if dec_tree.right is None:
        count = len(data)
        get_letter = dec_tree.left.key
        return get_letter * count
    final_value = ''
    temp = {}
    get_letter_codes(temp, dec_tree, '')
    generated_dict = {temp[key]: key for key in temp}
    v = ''
    for char in data:
        v += char
        if v in generated_dict:
            final_value += generated_dict[v]
            v = ''
    return final_value
if __name__ == "__main__":
    a_great_sentence = "The bird is the word"
    print("Original Data: {}\n".format(a_great_sentence))
    encoded_data, tree = huffman_encoding(a_great_sentence)
    print("Encoded Data: {}\n".format(encoded_data))
    decoded_data = huffman_decoding(encoded_data, tree)
    print("Decoded Data: {}\n".format(decoded_data))
    print("\nAdditional Test Cases:")
    test_cases = [
        "The bird is the word23y rkuwejfkjgfkj vduhdqlihoi fhglkrhtieriyweo iwefhli whiflhevidfghierhg",
        None,
        "aaaaaaaa"
    ]
    for test_case in test_cases:
        print("Original Data: {}\n".format(test_case))
        try:
            encoded_data, tree = huffman_encoding(test_case)
            print("Encoded Data: {}\n".format(encoded_data))
            decoded_data = huffman_decoding(encoded_data, tree)
            print("Decoded Data: {}\n".format(decoded_data))
        except (TypeError, ValueError):
            print('Error')