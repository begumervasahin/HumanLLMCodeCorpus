from collections import Counter
import queue
def calculate_probabilities(text, characters):
    count_ = Counter(text)
    total = sum(count_[char] for char in characters)
    probabilities = {char: count_[char] / total for char in characters}
    return probabilities
class HuffmanNode:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right
    def children(self):
        return self.left, self.right
def create_huffman_tree(frequencies):
    pq = queue.PriorityQueue()
    for prob, char in frequencies:
        pq.put((prob, HuffmanNode(char)))
    while pq.qsize() > 1:
        left, right = pq.get(), pq.get()
        node = HuffmanNode(left[1], right[1])
        pq.put((left[0] + right[0], node))
    return pq.get()[1]
def generate_huffman_codes(node, prefix="", code={}):
    if isinstance(node.left, HuffmanNode):
        generate_huffman_codes(node.left, prefix + "0", code)
    else:
        code[node.left] = prefix + "0"
    if isinstance(node.right, HuffmanNode):
        generate_huffman_codes(node.right, prefix + "1", code)
    else:
        code[node.right] = prefix + "1"
    return code
def encode_text(text, huffman_codes):
    return ''.join(huffman_codes[char] for char in text)
def main():
    text = open('rand_file').read()
    characters = ['A', 'B', 'C', 'D', 'E']
    probabilities = calculate_probabilities(text, characters)
    frequencies = sorted(probabilities.items(), key=lambda item: item[1])
    huffman_tree = create_huffman_tree(frequencies)
    huffman_codes = generate_huffman_codes(huffman_tree)
    for char, prob in sorted(frequencies, key=lambda item: item[1], reverse=True):
        print(f"{char}: {prob:.10f}, Code: {huffman_codes[char]}")
    encoded_text = encode_text(text, huffman_codes)
    print(encoded_text)
if __name__ == "__main__":
    main()