import struct
import sys
from HUFFMAN.components import huffnode, lists, huffmantree, encodehufftree
def compress_file(input_file, output_file="compressed.huff"):
    try:
        with open(input_file, 'rb') as file:
            inp = file.read()
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        return
    original_size = len(inp)
    nodes = [huffnode(i, 0) for i in range(256)]
    for byte in inp:
        nodes[byte].freq += 1
    nodes = [node for node in nodes if node.freq > 0]
    nodes.sort(key=lambda node: node.freq)
    link = lists(nodes[0])
    for node in nodes[1:]:
        new_list = lists(node)
        new_list.next = link
        link = new_list
    tree = build_huffman_tree(link)
    try:
        with open(output_file, 'wb') as comp:
            generate_huffman_encoding(tree, inp, comp)
        print("Compression completed successfully!")
    except Exception as e:
        print(f"An error occurred during compression: {e}")
def build_huffman_tree(link):
    while link and link.next:
        a = link.top()
        link = link.next
        b = link.top()
        link = link.next
        parent_node = huffnode(257, a.freq + b.freq)
        parent_node.left, parent_node.right = (b, a) if a.freq > b.freq else (a, b)
        new_list = lists(parent_node)
        link = link.insert(new_list) if link else new_list
    return link.top() if link else None
def generate_huffman_encoding(tree, inp, comp):
    dictionary = {}
    huffmantree(tree, dictionary, "")
    encoded_tree = encode_huff_tree_to_bits(tree)
    write_encoded_tree(comp, encoded_tree)
    encoded_data = encode_input_data(inp, dictionary)
    write_encoded_data(comp, encoded_data)
def encode_huff_tree_to_bits(tree):
    pt = []
    encodehufftree(tree, 16)
    return ''.join(pt)
def write_encoded_tree(comp, encoded_tree):
    tree_size = len(encoded_tree)
    comp.write(struct.pack('B', tree_size
    comp.write(struct.pack('B', tree_size % 256))
    chunk = ""
    for bit in encoded_tree:
        chunk += bit
        if len(chunk) >= 8:
            comp.write(struct.pack('B', int(chunk[:8], 2)))
            chunk = chunk[8:]
def encode_input_data(inp, dictionary):
    encoded_data = ""
    for byte in inp:
        encoded_data += dictionary[byte]
    encoded_data += "1"
    while len(encoded_data) % 8 != 0:
        encoded_data += "0"
    return encoded_data
def write_encoded_data(comp, encoded_data):
    while encoded_data:
        comp.write(struct.pack('B', int(encoded_data[:8], 2)))
        encoded_data = encoded_data[8:]
if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else "compressed.huff"
    compress_file(input_file, output_file)