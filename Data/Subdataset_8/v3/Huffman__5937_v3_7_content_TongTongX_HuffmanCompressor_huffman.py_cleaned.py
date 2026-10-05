from minheap import MinHeap
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
def build_huffman_tree(freq_table):
    trees = MinHeap()
    trees.add(1, TreeLeafEndMessage())
    for symbol, freq in freq_table.items():
        trees.add(freq, TreeLeaf(symbol))
    while len(trees) > 1:
        rfreq, right = trees.pop_min()
        lfreq, left = trees.pop_min()
        trees.add(lfreq + rfreq, TreeBranch(left, right))
    totalfreq, tree = trees.pop_min()
    return tree
def decode_huffman(tree, bitreader):
    while True:
        if isinstance(tree, TreeLeafEndMessage):
            return None
        elif isinstance(tree, TreeLeaf):
            return tree.value
        elif isinstance(tree, TreeBranch):
            if bitreader.readbit() == 0:
                tree = tree.left
            else:
                tree = tree.right
        else:
            raise TypeError('{} is not a tree type'.format(type(tree)))
def build_encoding_table(huffman_tree):
    table = {}
    def traverse_tree(node, path):
        if isinstance(node, TreeLeafEndMessage):
            table[None] = path
        elif isinstance(node, TreeLeaf):
            table[node.value] = path
        elif isinstance(node, TreeBranch):
            traverse_tree(node.left, path + (False,))
            traverse_tree(node.right, path + (True,))
        else:
            raise TypeError('{} is not a tree type'.format(type(node)))
    traverse_tree(huffman_tree, ())
    return table
def build_freq_table(stream):
    freqs = Counter()
    buffer = bytearray(512)
    while True:
        count = stream.readinto(buffer)
        freqs.update(buffer[:count])
        if count < len(buffer):
            break
    return freqs
input_file = 'your_input_file.txt'
with open(input_file, 'rb') as f:
    freq_table = build_freq_table(f)
huffman_tree = build_huffman_tree(freq_table)
encoding_table = build_encoding_table(huffman_tree)
