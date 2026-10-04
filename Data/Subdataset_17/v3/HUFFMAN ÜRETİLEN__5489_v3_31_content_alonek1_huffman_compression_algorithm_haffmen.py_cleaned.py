from collections import Counter
from queue import PriorityQueue
def calculate_probabilities(text, characters):
    char_count = Counter(text)
    total_count = sum(char_count[char] for char in characters)
    return {char: char_count[char] / total_count for char in characters}
class HuffmanNode:
    def __init__(self, char=None, left=None, right=None):
        self.char = char
        self.left = left
        self.right = right
    def is_leaf(self):
        return self.char is not None
def create_huffman_tree(frequencies):
    pq = PriorityQueue()
    for char, prob in frequencies:
        pq.put((prob, HuffmanNode(char=char)))
    while pq.qsize() > 1:
        left_prob, left_node = pq.get()
        right_prob, right_node = pq.get()
        combined_node = HuffmanNode(left=left_node, right=right_node)
        pq.put((left_prob + right_prob, combined_node))
    return pq.get()[1]
def generate_huffman_codes(node, prefix="", code=None):
    if code is None:
        code = {}
    if node.is_leaf():
        code[node.char] = prefix
    else:
        generate_huffman_codes(node.left, prefix + "0", code)
        generate_huffman_codes(node.right, prefix + "1", code)
    return code
def encode_text(text, huffman_codes):
    return ''.join(huffman_codes[char] for char in text)
def main():
    with open('rand_file', 'r') as file:
        text = file.read()
    characters = ['A', 'B', 'C', 'D', 'E']
    probabilities = calculate_probabilities(text, characters)
    frequencies = sorted(probabilities.items(), key=lambda item: item[1])
    huffman_tree = create_huffman_tree(frequencies)
    huffman_codes = generate_huffman_codes(huffman_tree)
    print("Character Frequencies and Huffman Codes:")
    for char, prob in sorted(frequencies, key=lambda item: item[1], reverse=True):
        print(f"Character: {char}, Probability: {prob:.10f}, Code: {huffman_codes[char]}")
    encoded_text = encode_text(text, huffman_codes)
    print("\nEncoded Text:")
    print(encoded_text)
if __name__ == "__main__":
    main()