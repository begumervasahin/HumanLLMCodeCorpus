import sys
import struct
class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
class ListNode:
    def __init__(self, node):
        self.node = node
        self.next = None
    def insert(self, new_node):
        if new_node.node.freq < self.node.freq:
            new_node.next = self
            return new_node
        else:
            current = self
            while current.next is not None and current.next.node.freq < new_node.node.freq:
                current = current.next
            new_node.next = current.next
            current.next = new_node
            return self
    def top(self):
        return self.node
def build_huffman_tree(node, dictionary, prefix):
    if node.left is None and node.right is None:
        dictionary[node.char] = prefix
    if node.left is not None:
        build_huffman_tree(node.left, dictionary, prefix + "0")
    if node.right is not None:
        build_huffman_tree(node.right, dictionary, prefix + "1")
def encode_huffman_tree(node, prefix):
    if node.left is None and node.right is None:
        encoded_tree.append('1')
        encoded_tree.append('{0:08b}'.format(prefix + ord(node.char)))
    else:
        encoded_tree.append('0')
        encode_huffman_tree(node.left, prefix + 1)
        encode_huffman_tree(node.right, prefix + 1)
def combine_bits(bits):
    byte = ""
    for bit in bits:
        byte += bit
    return byte
def generate_address(tree, compressed_file):
    code_dictionary = {0: 0}
    build_huffman_tree(tree, code_dictionary, "")
    encode_huffman_tree(tree, 16)
    encoded_tree_string = combine_bits(encoded_tree)
    size = len(encoded_tree_string)
    compressed_file.write(struct.pack('BB', size
    chunk = ""
    for bit in encoded_tree_string:
        chunk += bit
        if len(chunk) > 8:
            compressed_file.write(struct.pack('B', int(chunk[0:8], 2)))
            chunk = chunk[8:]
    data_chunk = ""
    for ch in input_data:
        data_chunk += code_dictionary[ch]
        if len(data_chunk) > 8:
            compressed_file.write(struct.pack('B', int(data_chunk[0:8], 2)))
            data_chunk = data_chunk[8:]
    data_chunk += "1"
    while len(data_chunk) % 8 == 0:
        data_chunk += "0"
    while data_chunk:
        compressed_file.write(struct.pack('B', int("0b" + data_chunk[0:8], 2)))
        data_chunk = data_chunk[8:]
    compressed_file.flush()
try:
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else "compressed.huff"
except IndexError:
    print("Usage: python huffman_compress.py <input_file> [<output_file>]")
    sys.exit(1)
try:
    with open(input_file, 'rb') as file:
        input_data = file.read()
        original_size = len(input_data)
except FileNotFoundError:
    print("Input file not found!")
    sys.exit(1)
frequency_array = [HuffmanNode(i, 0) for i in range(256)]
for ch in input_data:
    frequency_array[ch].freq += 1
frequency_array.sort(key=lambda x: x.freq)
linked_list = ListNode(frequency_array[0])
for a in frequency_array[:0:-1]:
    if a.freq != 0:
        new_node = ListNode(a)
        new_node.next = linked_list
        linked_list = new_node
    else:
        break
tree = None
while True:
    a = linked_list.top()
    linked_list = linked_list.next
    b = linked_list.top()
    linked_list = linked_list.next
    new_node = HuffmanNode(257, a.freq + b.freq)
    new_node.right = a if a.freq > b.freq else b
    new_node.left = b if a.freq > b.freq else a
    new_list_node = ListNode(new_node)
    if linked_list:
        linked_list = linked_list.insert(new_list_node)
    else:
        tree = new_node
        break
with open(output_file, 'wb') as compressed_file:
    encoded_tree = []
    try:
        generate_address(tree, compressed_file)
        print("Compression completed successfully!")
    except Exception as e:
        print("An error occurred:", e)