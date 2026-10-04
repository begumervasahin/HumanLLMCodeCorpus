from queue import PriorityQueue
class Node:
    def __init__(self, data, frequency, left_child=None, right_child=None):
        self.data = data
        self.frequency = frequency
        self.left_child = left_child
        self.right_child = right_child
    def __lt__(self, other):
        return self.frequency < other.frequency
    def __repr__(self):
        return f"Node(data={self.data}, frequency={self.frequency})"
def build_priority_queue(string):
    frequency_dict = {}
    for char in string:
        if char in frequency_dict:
            frequency_dict[char] += 1
        else:
            frequency_dict[char] = 1
    priority_queue = PriorityQueue()
    for char, frequency in frequency_dict.items():
        priority_queue.put(Node(char, frequency))
    return priority_queue
def build_huffman_tree(priority_queue):
    while priority_queue.qsize() > 1:
        left_node = priority_queue.get()
        right_node = priority_queue.get()
        combined_frequency = left_node.frequency + right_node.frequency
        parent_node = Node(None, combined_frequency, left_node, right_node)
        priority_queue.put(parent_node)
    return priority_queue.get()
def build_huffman_table(node, code='', huffman_table=None):
    if huffman_table is None:
        huffman_table = {}
    if node.left_child is None and node.right_child is None:
        huffman_table[node.data] = code
    else:
        if node.left_child is not None:
            build_huffman_table(node.left_child, code + '0', huffman_table)
        if node.right_child is not None:
            build_huffman_table(node.right_child, code + '1', huffman_table)
    return huffman_table
def encode_string(string, huffman_table):
    return ''.join(huffman_table[char] for char in string)
def decode_string(encoded_string, huffman_tree):
    decoded_string = ''
    current_node = huffman_tree
    for bit in encoded_string:
        current_node = current_node.left_child if bit == '0' else current_node.right_child
        if current_node.left_child is None and current_node.right_child is None:
            decoded_string += current_node.data
            current_node = huffman_tree
    return decoded_string
if __name__ == "__main__":
    with open('texteEncode.txt', 'r') as file:
        input_string = file.read()
    priority_queue = build_priority_queue(input_string)
    huffman_tree = build_huffman_tree(priority_queue)
    huffman_table = build_huffman_table(huffman_tree)
    encoded_string = encode_string(input_string, huffman_table)
    with open('texteEncode.txt', 'w') as file:
        file.write(encoded_string)
    decoded_string = decode_string(encoded_string, huffman_tree)
    print(decoded_string)