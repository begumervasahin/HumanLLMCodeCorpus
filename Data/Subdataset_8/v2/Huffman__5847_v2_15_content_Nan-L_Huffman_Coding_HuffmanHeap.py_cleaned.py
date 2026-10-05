class HuffmanTree:
    def __init__(self, value, freq):
        self.value = value
        self.freq = freq
    def get_freq(self):
        return self.freq
class HuffmanHeap:
    def __init__(self, old, new=None):
        self.old = old
        self.new = new if new is not None else []
    def enqueue(self, item):
        self.new.append(item)
    def dequeue(self):
        if len(self.old) == 0 and len(self.new) != 0:
            item = self.new.pop(0)
        elif len(self.new) == 0 and len(self.old) != 0:
            item = self.old.pop(0)
        elif len(self.new) != 0 and len(self.old) != 0:
            if self.old[0].get_freq() >= self.new[0].get_freq():
                item = self.new.pop(0)
            else:
                item = self.old.pop(0)
        else:
            print("Both old and new lists are empty!")
            return None
        return item
if __name__ == "__main__":
    old_huffman_trees = [HuffmanTree('a', 5), HuffmanTree('b', 3)]
    new_huffman_trees = [HuffmanTree('c', 2), HuffmanTree('d', 4)]
    huffman_heap = HuffmanHeap(old_huffman_trees, new_huffman_trees)
    huffman_heap.enqueue(HuffmanTree('e', 1))
    smallest_tree = huffman_heap.dequeue()
    if smallest_tree:
        print("Smallest tree dequeued:", smallest_tree.value, smallest_tree.freq)