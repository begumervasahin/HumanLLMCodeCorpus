import queue
from collections import Counter
def read_text(filename):
    with open(filename, 'r') as file:
        return file.read()
def calculate_frequencies(text):
    return Counter(text)
def calculate_probabilities(frequencies):
    total_sum = sum(frequencies.values())
    return {char: freq / total_sum for char, freq in frequencies.items()}
class HuffmanNode:
    def __init__(self, left=None, right=None, root=None):
        self.left = left
        self.right = right
        self.root = root
    def children(self):
        return self.left, self.right
def create_tree(frequencies):
    priority_queue = queue.PriorityQueue()
    for char, freq in frequencies.items():
        priority_queue.put((freq, HuffmanNode(None, None, char)))
    while priority_queue.qsize() > 1:
        left, right = priority_queue.get(), priority_queue.get()
        node = HuffmanNode(left, right)
        priority_queue.put((left[0] + right[0], node))
    return priority_queue.get()
def walk_tree(node, prefix="", code={}):
    if isinstance(node[1].left[1], HuffmanNode):
        walk_tree(node[1].left, prefix + "0", code)
    else:
        code[node[1].left[1]] = prefix + "0"
    if isinstance(node[1].right[1], HuffmanNode):
        walk_tree(node[1].right, prefix + "1", code)
    else:
        code[node[1].right[1]] = prefix + "1"
    return code
def encode_text(text, code):
    return ''.join(code[char] for char in text)
if __name__ == '__main__':
    text = read_text('rand_file')
    frequencies = calculate_frequencies(text)
    probabilities = calculate_probabilities(frequencies)
    huffman_tree = create_tree(probabilities)
    huffman_codes = walk_tree(huffman_tree)
    for char, freq in sorted(probabilities.items(), key=lambda x: x[1], reverse=True):
        print(char, '{:.10f}'.format(freq), huffman_codes[char])
    encoded_text = encode_text(text, huffman_codes)
    print(encoded_text)