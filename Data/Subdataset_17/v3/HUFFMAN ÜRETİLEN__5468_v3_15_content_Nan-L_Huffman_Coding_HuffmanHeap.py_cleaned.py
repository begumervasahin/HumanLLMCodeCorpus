class HuffmanTree:
    def __init__(self, freq, symbol=None, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
    def __repr__(self):
        return f"HuffmanTree(freq={self.freq}, symbol={self.symbol})"
    def get_freq(self):
        return self.freq
class HuffmanHeap:
    def __init__(self, old=None, new=None):
        self.old = old if old is not None else []
        self.new = new if new is not None else []
    def enqueue(self, item):
        self.new.append(item)
        self.new.sort(key=lambda x: x.get_freq())
    def dequeue(self):
        if not self.old and not self.new:
            print("Both old and new lists are empty!")
            return None
        if not self.old:
            return self.new.pop(0)
        if not self.new:
            return self.old.pop(0)
        if self.old[0].get_freq() <= self.new[0].get_freq():
            return self.old.pop(0)
        else:
            return self.new.pop(0)
if __name__ == "__main__":
    old_list = [HuffmanTree(freq=5), HuffmanTree(freq=10)]
    new_list = [HuffmanTree(freq=2), HuffmanTree(freq=8)]
    huffman_heap = HuffmanHeap(old_list, new_list)
    huffman_heap.enqueue(HuffmanTree(freq=3))
    while True:
        item = huffman_heap.dequeue()
        if item is None:
            break
        print("Dequeued:", item)