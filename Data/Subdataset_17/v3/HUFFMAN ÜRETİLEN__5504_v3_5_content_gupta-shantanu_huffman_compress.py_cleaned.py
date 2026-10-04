import struct
import sys
from HUFFMAN.components import HuffNode, LinkedList, HuffmanTree, encode_huffman_tree
def read_input_file(file_path):
    with open(file_path, 'rb') as file:
        return file.read()
def initialize_huffman_nodes():
    return [HuffNode(byte_value, 0) for byte_value in range(256)]
def calculate_frequencies(data, nodes):
    for byte in data:
        nodes[byte].freq += 1
    nodes.sort(key=lambda node: node.freq)
def build_huffman_tree(nodes):
    linked_list = LinkedList(nodes[0])
    for node in nodes[1:]:
        if node.freq == 0:
            break
        linked_list = LinkedList(node, linked_list)
    while linked_list and linked_list.next:
        left_node = linked_list.pop_top()
        right_node = linked_list.pop_top()
        combined_freq = left_node.freq + right_node.freq
        parent_node = HuffNode(257, combined_freq, left_node, right_node)
        linked_list = linked_list.insert_sorted(LinkedList(parent_node))
    return linked_list.top()
def write_bits_to_file(file, bit_buffer):
    while len(bit_buffer) >= 8:
        byte_value = int(bit_buffer[:8], 2)
        file.write(struct.pack('B', byte_value))
        bit_buffer = bit_buffer[8:]
    return bit_buffer
def write_compressed_file(file, encoded_tree, encoding_dict, data):
    tree_size = len(encoded_tree)
    file.write(struct.pack('BB', tree_size
    bit_buffer = encoded_tree
    bit_buffer = write_bits_to_file(file, bit_buffer)
    for byte in data:
        bit_buffer += encoding_dict[byte]
        bit_buffer = write_bits_to_file(file, bit_buffer)
    bit_buffer += "1"
    bit_buffer += "0" * ((8 - len(bit_buffer) % 8) % 8)
    write_bits_to_file(file, bit_buffer)
def generate_huffman_encoding(tree, file, data):
    encoding_dict = {}
    encode_huffman_tree(tree, encoding_dict, "")
    encoded_tree = ''.join(encoding_dict[byte] for byte in encoding_dict)
    write_compressed_file(file, encoded_tree, encoding_dict, data)
def main():
    if len(sys.argv) < 2:
        print("Usage: python huffman.py <input_file> [output_file]")
        return
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else "compressed.huff"
    try:
        data = read_input_file(input_file)
        nodes = initialize_huffman_nodes()
        calculate_frequencies(data, nodes)
        huffman_tree = build_huffman_tree(nodes)
        with open(output_file, 'wb') as output_file:
            generate_huffman_encoding(huffman_tree, output_file, data)
        print("Compression completed successfully!")
    except Exception as error:
        print(f"An error occurred: {error}")
if __name__ == "__main__":
    main()