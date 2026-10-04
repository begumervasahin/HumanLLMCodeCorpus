class HuffmanTree:
    def __init__(self, freq, symbol=None, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
    def get_freq(self):
        return self.freq
    def __repr__(self):
        return f"HuffmanTree(freq={self.freq}, symbol={self.symbol})"
class HuffmanHeap:
    def __init__(self, old=None, new=None):
        self.old = old if old is not None else []
        self.new = new if new is not None else []
    def enqueue(self, item):
        self.new.append(item)
        self.new.sort(key=lambda x: x.get_freq())
    def dequeue(self):
        if not self.old and self.new:
            return self.new.pop(0)
        elif not self.new and self.old:
            return self.old.pop(0)
        elif self.new and self.old:
            if self.old[0].get_freq() <= self.new[0].get_freq():
                return self.old.pop(0)
            else:
                return self.new.pop(0)
        else:
            print("Both old and new lists are empty!")
            return None
if __name__ == "__main__":
    old_list = [HuffmanTree(freq=5), HuffmanTree(freq=10)]
    new_list = [HuffmanTree(freq=2), HuffmanTree(freq=8)]
    huffman_heap = HuffmanHeap(old_list, new_list)
    huffman_heap.enqueue(HuffmanTree(freq=3))
    print("Dequeued:", huffman_heap.dequeue())
    print("Dequeued:", huffman_heap.dequeue())
    while True:
        item = huffman_heap.dequeue()
        if item is None:
            break
        print("Dequeued:", item)