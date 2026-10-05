from collections import Counter
import queue
text = open('rand_file').read()
count_ = Counter(text)
sum_ = sum(count_.values())
probabilities = {char: count_[char] / sum_ for char in count_}
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
frequencies = [(probabilities[char], char) for char in probabilities]
root_node = create_tree(frequencies)
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
huffman_code = walk_tree(root_node)
for char, probability in sorted(probabilities.items(), key=lambda x: x[1], reverse=True):
    print(char, '{:6.10f}'.format(probability), huffman_code[char])
encoded_text = "".join(huffman_code[char] for char in text)
print(encoded_text)