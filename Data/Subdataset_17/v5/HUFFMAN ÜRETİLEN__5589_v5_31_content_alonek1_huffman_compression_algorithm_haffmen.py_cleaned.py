from collections import Counter
from queue import PriorityQueue
with open('rand_file') as file:
    text = file.read()
char_count = Counter(text)
selected_chars = ['A', 'B', 'C', 'D', 'E']
total_count = sum(char_count[char] for char in selected_chars)
probabilities = {char: char_count[char] / total_count for char in selected_chars}
class HuffmanNode:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right
    def children(self):
        return self.left, self.right
def create_huffman_tree(probabilities):
    pq = PriorityQueue()
    for char, prob in probabilities.items():
        pq.put((prob, char))
    while pq.qsize() > 1:
        left_node, right_node = pq.get(), pq.get()
        node = HuffmanNode(left_node, right_node)
        pq.put((left_node[0] + right_node[0], node))
    return pq.get()
def generate_huffman_codes(node, prefix="", code=None):
    if code is None:
        code = {}
    if isinstance(node[1], HuffmanNode):
        generate_huffman_codes(node[1].left, prefix + "0", code)
        generate_huffman_codes(node[1].right, prefix + "1", code)
    else:
        code[node[1]] = prefix
    return code
huffman_tree = create_huffman_tree(probabilities)
huffman_codes = generate_huffman_codes(huffman_tree)
print("Character  Probability       Huffman Code")
for char in sorted(probabilities, key=probabilities.get, reverse=True):
    print(f"{char}         {probabilities[char]:.10f}     {huffman_codes[char]}")
encoded_text = ''.join(huffman_codes[char] for char in text if char in huffman_codes)
print(f"Encoded text: {encoded_text}")