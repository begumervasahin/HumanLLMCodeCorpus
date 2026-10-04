import struct
import sys
from HUFFMAN.components import huffnode, lists, huffmantree, encodehufftree
def compress_file(input_file, output_file="compressed.huff"):
    inp = read_input_file(input_file)
    if inp is None:
        return
    original_size = len(inp)
    nodes = build_frequency_nodes(inp)
    sorted_nodes = sorted(nodes, key=lambda node: node.freq)
    huffman_tree_root = build_huffman_tree(create_linked_list(sorted_nodes))
    try:
        with open(output_file, 'wb') as comp:
            write_compressed_data(huffman_tree_root, inp, comp)
        print("Compression completed successfully!")
    except Exception as e:
        print(f"An error occurred during compression: {e}")
def read_input_file(input_file):
    try:
        with open(input_file, 'rb') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        return None
def build_frequency_nodes(data):
    nodes = [huffnode(i, 0) for i in range(256)]
    for byte in data:
        nodes[byte].freq += 1
    return [node for node in nodes if node.freq > 0]
def create_linked_list(nodes):
    link = lists(nodes[0])
    for node in nodes[1:]:
        new_list = lists(node)
        new_list.next = link
        link = new_list
    return link
def build_huffman_tree(link):
    while link and link.next:
        a, b = link.top(), link.next.top()
        link = link.next.next
        parent_node = huffnode(257, a.freq + b.freq)
        parent_node.left, parent_node.right = sorted([a, b], key=lambda node: node.freq)
        new_list = lists(parent_node)
        link = link.insert(new_list) if link else new_list
    return link.top() if link else None
def write_compressed_data(tree, data, comp):
    huffman_dict = generate_huffman_dictionary(tree)
    encoded_tree = encode_huff_tree_to_bits(tree)
    write_encoded_tree(comp, encoded_tree)
    encoded_data = encode_input_data(data, huffman_dict)
    write_encoded_data(comp, encoded_data)
def generate_huffman_dictionary(tree):
    huffman_dict = {}
    huffmantree(tree, huffman_dict, "")
    return huffman_dict
def encode_huff_tree_to_bits(tree):
    bit_list = []
    encodehufftree(tree, 16)
    return ''.join(bit_list)
def write_encoded_tree(comp, encoded_tree):
    tree_size = len(encoded_tree)
    comp.write(struct.pack('B', tree_size
    comp.write(struct.pack('B', tree_size % 256))
    write_bits_to_file(comp, encoded_tree)
def encode_input_data(data, huffman_dict):
    encoded_data = ''.join(huffman_dict[byte] for byte in data) + "1"
    return encoded_data.ljust(len(encoded_data) + (8 - len(encoded_data) % 8), '0')
def write_encoded_data(comp, encoded_data):
    write_bits_to_file(comp, encoded_data)
def write_bits_to_file(comp, bit_string):
    while bit_string:
        comp.write(struct.pack('B', int(bit_string[:8], 2)))
        bit_string = bit_string[8:]
if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else "compressed.huff"
    compress_file(input_file, output_file)