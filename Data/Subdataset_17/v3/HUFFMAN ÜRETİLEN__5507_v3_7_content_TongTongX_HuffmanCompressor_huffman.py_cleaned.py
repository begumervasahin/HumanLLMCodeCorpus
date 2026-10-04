import heapq
from collections import Counter
class TreeLeafEndMessage:
    pass
class TreeLeaf:
    def __init__(self, value):
        self.value = value
class TreeBranch:
    def __init__(self, left, right):
        self.left = left
        self.right = right
class MinHeap:
    def __init__(self):
        self.heap = []
    def add(self, priority, item):
        heapq.heappush(self.heap, (priority, item))
    def pop_min(self):
        return heapq.heappop(self.heap)
    def __len__(self):
        return len(self.heap)
def build_huffman_tree(freq_table):
    heap = MinHeap()
    heap.add(1, TreeLeafEndMessage())
    for symbol, freq in freq_table.items():
        heap.add(freq, TreeLeaf(symbol))
    while len(heap) > 1:
        left_freq, left_node = heap.pop_min()
        right_freq, right_node = heap.pop_min()
        combined_freq = left_freq + right_freq
        heap.add(combined_freq, TreeBranch(left_node, right_node))
    _, huffman_tree = heap.pop_min()
    return huffman_tree
def decode_huffman(tree, bitreader):
    while True:
        if isinstance(tree, TreeLeafEndMessage):
            return None
        elif isinstance(tree, TreeLeaf):
            return tree.value
        elif isinstance(tree, TreeBranch):
            tree = tree.left if bitreader.readbit() == 0 else tree.right
        else:
            raise TypeError(f'Unexpected tree type: {type(tree)}')
def create_encoding_table(huffman_tree):
    encoding_table = {}
    def traverse(tree, path):
        if isinstance(tree, TreeLeafEndMessage):
            encoding_table[None] = path
        elif isinstance(tree, TreeLeaf):
            encoding_table[tree.value] = path
        elif isinstance(tree, TreeBranch):
            traverse(tree.left, path + (False,))
            traverse(tree.right, path + (True,))
        else:
            raise TypeError(f'Unexpected tree type: {type(tree)}')
    traverse(huffman_tree, ())
    return encoding_table
def generate_freq_table(stream):
    frequency_counter = Counter()
    buffer = bytearray(512)
    while True:
        bytes_read = stream.readinto(buffer)
        frequency_counter.update(buffer[:bytes_read])
        if bytes_read < len(buffer):
            break
    return frequency_counter
if __name__ == "__main__":
    data = b"example data for Huffman encoding"
    freq_table = generate_freq_table(iter(data))
    huffman_tree = build_huffman_tree(freq_table)
    encoding_table = create_encoding_table(huffman_tree)
    print("Frequency Table:", freq_table)
    print("Encoding Table:", encoding_table)