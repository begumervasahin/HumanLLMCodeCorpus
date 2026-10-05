from collections import Counter
import queue
def read_text(file_path):
    with open(file_path, 'r') as file:
        return file.read()
def calculate_probabilities(text):
    char_count = Counter(text)
    total_chars = sum(char_count.values())
    return {char: count / total_chars for char, count in char_count.items()}
class HuffmanNode:
    def __init__(self, left=None, right=None, root=None):
        self.left = left
        self.right = right
        self.root = root
def create_tree(frequencies):
    pq = queue.PriorityQueue()
    for value in frequencies:
        pq.put(value)
    while pq.qsize() > 1:
        left, right = pq.get(), pq.get()
        node = HuffmanNode(left, right)
        pq.put((left[0] + right[0], node))
    return pq.get()
def walk_tree(node, prefix="", code={}):
    left, right = node[1].left[1], node[1].right[1]
    if isinstance(left, HuffmanNode):
        walk_tree(left, prefix + "0", code)
    else:
        code[left] = prefix + "0"
    if isinstance(right, HuffmanNode):
        walk_tree(right, prefix + "1", code)
    else:
        code[right] = prefix + "1"
    return code
if __name__ == '__main__':
    text = read_text('rand_file')
    probabilities = calculate_probabilities(text)
    frequencies = [(probabilities[char], char) for char in probabilities]
    root_node = create_tree(frequencies)
    huffman_code = walk_tree(root_node)
    for char, probability in sorted(probabilities.items(), key=lambda x: x[1], reverse=True):
        print(char, '{:6.10f}'.format(probability), huffman_code[char])
    encoded_text = "".join(huffman_code[char] for char in text)
    print(encoded_text)