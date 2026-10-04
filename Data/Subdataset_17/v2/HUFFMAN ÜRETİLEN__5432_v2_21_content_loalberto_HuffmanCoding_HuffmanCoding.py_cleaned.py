import sys
from collections import defaultdict, PriorityQueue
class Node:
    def __init__(self, frequency, key=''):
        self.key = key
        self.frequency = frequency
        self.code = None
        self.left = None
        self.right = None
def assign_codes(node, code=''):
    if node is None:
        return
    if node.left is None and node.right is None:
        node.code = code
        return
    assign_codes(node.left, code + '0')
    assign_codes(node.right, code + '1')
def build_huffman_tree(frequencies):
    nodes = [Node(freq, char) for char, freq in frequencies.items()]
    while len(nodes) > 1:
        nodes.sort(key=lambda node: node.frequency)
        left = nodes.pop(0)
        right = nodes.pop(0)
        merged_node = Node(left.frequency + right.frequency)
        merged_node.left = left
        merged_node.right = right
        nodes.append(merged_node)
    return nodes[0]
def generate_huffman_codes(root):
    code_dict = {}
    assign_codes(root)
    fill_code_dict(root, code_dict)
    return code_dict
def fill_code_dict(node, code_dict):
    if node.left is None and node.right is None:
        code_dict[node.key] = node.code
        return
    fill_code_dict(node.left, code_dict)
    fill_code_dict(node.right, code_dict)
def huffman_encoding(data):
    if not data:
        return None, None
    frequencies = defaultdict(int)
    for char in data:
        frequencies[char] += 1
    if len(frequencies) == 1:
        single_char = next(iter(frequencies))
        encoded_data = '0' * len(data)
        root = Node(frequencies[single_char])
        root.left = Node(frequencies[single_char], single_char)
        return encoded_data, root
    root = build_huffman_tree(frequencies)
    code_dict = generate_huffman_codes(root)
    encoded_data = ''.join(code_dict[char] for char in data)
    return encoded_data, root
def huffman_decoding(encoded_data, root):
    if not encoded_data or not root:
        return None
    decoded_data = []
    current_node = root
    for bit in encoded_data:
        current_node = current_node.left if bit == '0' else current_node.right
        if current_node.left is None and current_node.right is None:
            decoded_data.append(current_node.key)
            current_node = root
    return ''.join(decoded_data)
def test_huffman(data):
    print("Original data size:", sys.getsizeof(data))
    print("Original data:", data)
    encoded_data, tree = huffman_encoding(data)
    if encoded_data:
        print("Encoded data size:", sys.getsizeof(int(encoded_data, base=2)))
        print("Encoded data:", encoded_data)
        decoded_data = huffman_decoding(encoded_data, tree)
        print("Decoded data size:", sys.getsizeof(decoded_data))
        print("Decoded data:", decoded_data)
    else:
        print("Encoding failed. Data is empty or None.")
if __name__ == "__main__":
    test_cases = [
        "The bird is the word",
        "The bird is the word23y rkuwejfkjgfkj vduhdqlihoi fhglkrhtieriyweo iwefhli whiflhevidfghierhg",
        None,
        "aaaaaaaa"
    ]
    for data in test_cases:
        print("\n--- Test case ---")
        test_huffman(data)