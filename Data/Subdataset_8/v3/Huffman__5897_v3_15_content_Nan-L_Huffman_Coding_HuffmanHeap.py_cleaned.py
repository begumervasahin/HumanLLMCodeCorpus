class HuffmanTree:
    def __init__(self, value, freq):
        self.value = value
        self.freq = freq
    def get_freq(self):
        return self.freq
class HuffmanHeap:
    def __init__(self, old_trees, new_trees=None):
        self.old_trees = old_trees
        self.new_trees = new_trees if new_trees is not None else []
    def enqueue(self, tree):
        self.new_trees.append(tree)
    def dequeue(self):
        if not self.old_trees and self.new_trees:
            smallest_tree = self.new_trees.pop(0)
        elif not self.new_trees and self.old_trees:
            smallest_tree = self.old_trees.pop(0)
        elif self.old_trees and self.new_trees:
            if self.old_trees[0].get_freq() >= self.new_trees[0].get_freq():
                smallest_tree = self.new_trees.pop(0)
            else:
                smallest_tree = self.old_trees.pop(0)
        else:
            print("Both old and new lists are empty!")
            return None
        return smallest_tree
if __name__ == "__main__":
    old_trees = [HuffmanTree('a', 5), HuffmanTree('b', 3)]
    new_trees = [HuffmanTree('c', 2), HuffmanTree('d', 4)]
    huffman_heap = HuffmanHeap(old_trees, new_trees)
    huffman_heap.enqueue(HuffmanTree('e', 1))
    smallest_tree = huffman_heap.dequeue()
    if smallest_tree:
        print("Smallest tree dequeued:", smallest_tree.value, smallest_tree.freq)