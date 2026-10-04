import struct
import sys
from HUFFMAN.components import huffnode, lists, huffmantree, encodehufftree
def read_input_file(input_file):
    with open(input_file, 'rb') as file:
        return file.read()
def initialize_huffman_nodes():
    return [huffnode(i, 0) for i in range(256)]
def calculate_frequencies(data, arr):
    for ch in data:
        arr[ch].freq += 1
    arr.sort(key=lambda x: x.freq)
def build_huffman_tree(arr):
    link = lists(arr[0])
    for a in arr[:0:-1]:
        if a.freq != 0:
            new_node = lists(a)
            new_node.next = link
            link = new_node
        else:
            break
    while True:
        a = link.top()
        link = link.next
        b = link.top()
        link = link.next
        combined_freq = a.freq + b.freq
        new_node = huffnode(257, combined_freq)
        if a.freq > b.freq:
            new_node.right, new_node.left = a, b
        else:
            new_node.left, new_node.right = a, b
        if link is not None:
            link = link.insert(lists(new_node))
        else:
            return new_node
def write_compressed_file(comp, coded_tree, dictionary, data):
    size = len(coded_tree)
    comp.write(struct.pack('B', size
    comp.write(struct.pack('B', size % 256))
    chunk = ""
    for ch in coded_tree:
        chunk += ch
        if len(chunk) >= 8:
            comp.write(struct.pack('B', int(chunk[:8], 2)))
            chunk = chunk[8:]
    for ch in data:
        chunk += dictionary[ch]
        while len(chunk) >= 8:
            comp.write(struct.pack('B', int(chunk[:8], 2)))
            chunk = chunk[8:]
    chunk += "1"
    chunk += "0" * ((8 - len(chunk) % 8) % 8)
    while chunk:
        comp.write(struct.pack('B', int(chunk[:8], 2)))
        chunk = chunk[8:]
def generate_address(tree, comp, data):
    dictionary = {}
    huffmantree(tree, dictionary, "")
    coded_tree = ''.join(pt)
    write_compressed_file(comp, coded_tree, dictionary, data)
def main():
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else "compressed.huff"
    data = read_input_file(input_file)
    arr = initialize_huffman_nodes()
    calculate_frequencies(data, arr)
    tree = build_huffman_tree(arr)
    with open(output_file, 'wb') as comp:
        generate_address(tree, comp, data)
    print("Job completed!")
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")