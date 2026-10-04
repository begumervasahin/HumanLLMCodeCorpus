from queue import PriorityQueue
class Node:
    def __init__(self, data, frequency, left=None, right=None):
        self.data = data
        self.frequency = frequency
        self.left = left
        self.right = right
    def __lt__(self, other):
        return self.frequency < other.frequency
    def __repr__(self):
        return f"Node(data={self.data}, frequency={self.frequency})"
def calculate_frequencies(text):
    frequency_dict = {}
    for char in text:
        frequency_dict[char] = frequency_dict.get(char, 0) + 1
    return frequency_dict
def build_priority_queue(frequency_dict):
    priority_queue = PriorityQueue()
    for char, freq in frequency_dict.items():
        priority_queue.put(Node(char, freq))
    return priority_queue
def build_huffman_tree(priority_queue):
    while priority_queue.qsize() > 1:
        left = priority_queue.get()
        right = priority_queue.get()
        merged_node = Node(None, left.frequency + right.frequency, left, right)
        priority_queue.put(merged_node)
    return priority_queue.get()
def build_huffman_table(node, code='', huffman_table=None):
    if huffman_table is None:
        huffman_table = {}
    if node.left is None and node.right is None:
        huffman_table[node.data] = code
    else:
        if node.left:
            build_huffman_table(node.left, code + '0', huffman_table)
        if node.right:
            build_huffman_table(node.right, code + '1', huffman_table)
    return huffman_table
def encode_text(text, huffman_table):
    return ''.join(huffman_table[char] for char in text)
def decode_text(encoded_text, huffman_tree):
    decoded_text = []
    current_node = huffman_tree
    for bit in encoded_text:
        current_node = current_node.left if bit == '0' else current_node.right
        if current_node.left is None and current_node.right is None:
            decoded_text.append(current_node.data)
            current_node = huffman_tree
    return ''.join(decoded_text)
def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()
def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)
def main():
    input_file_path = 'texteEncode.txt'
    input_text = read_file(input_file_path)
    frequency_dict = calculate_frequencies(input_text)
    priority_queue = build_priority_queue(frequency_dict)
    huffman_tree = build_huffman_tree(priority_queue)
    huffman_table = build_huffman_table(huffman_tree)
    encoded_text = encode_text(input_text, huffman_table)
    write_file(input_file_path, encoded_text)
    decoded_text = decode_text(encoded_text, huffman_tree)
    print(decoded_text)
if __name__ == "__main__":
    main()