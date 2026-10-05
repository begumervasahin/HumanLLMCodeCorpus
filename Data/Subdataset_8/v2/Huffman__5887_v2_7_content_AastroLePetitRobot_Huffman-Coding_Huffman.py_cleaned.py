from queue import PriorityQueue
class Node:
    def __init__(self, data, frequency, leftChild=None, rightChild=None):
        self.data = data
        self.frequency = frequency
        self.leftChild = leftChild
        self.rightChild = rightChild
    def __lt__(self, other):
        return self.frequency < other.frequency
    def __repr__(self):
        return "Node: value ({}) with frequency ({})\n".format(self.data, self.frequency)
def initialize_priority_queue(string):
    queue = PriorityQueue()
    characters = set(string)
    for char in characters:
        queue.put(Node(char, string.count(char)))
    return queue
def build_huffman_tree(queue):
    while queue.qsize() > 1:
        left_node = queue.get()
        right_node = queue.get()
        frequency = left_node.frequency + right_node.frequency
        new_node = Node(None, frequency, left_node, right_node)
        queue.put(new_node)
    return queue.get()
def build_huffman_table(node, code, huffman_table):
    if node.leftChild is None and node.rightChild is None:
        huffman_table[node.data] = code
    if node.leftChild is not None:
        build_huffman_table(node.leftChild, code + "0", huffman_table)
    if node.rightChild is not None:
        build_huffman_table(node.rightChild, code + "1", huffman_table)
def encode_string(string, huffman_table):
    encoded_string = ""
    for char in string:
        encoded_string += huffman_table[char]
    return encoded_string
def decode_string(encoded_string, node):
    decoded_string = ""
    current_node = node
    for bit in encoded_string:
        if bit == "0":
            current_node = current_node.leftChild
        elif bit == "1":
            current_node = current_node.rightChild
        if current_node.data is not None:
            decoded_string += current_node.data
            current_node = node
    return decoded_string
with open('texteEncode.txt', 'r') as f:
    input_string = f.read()
priority_queue = initialize_priority_queue(input_string)
huffman_tree = build_huffman_tree(priority_queue)
print(huffman_tree)
huffman_table = {}
build_huffman_table(huffman_tree, "", huffman_table)
print(huffman_table)
encoded_string = encode_string(input_string, huffman_table)
print(encoded_string)
with open('texteEncode.txt', 'w') as f:
    f.write(encoded_string)
decoded_string = decode_string(encoded_string, huffman_tree)
print(decoded_string)