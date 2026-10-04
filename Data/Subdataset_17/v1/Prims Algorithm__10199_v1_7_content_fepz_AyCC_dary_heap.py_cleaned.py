import math
class HeapItem(object):
    def __init__(self, key, value):
        self.key = key
        self.pos = None
        self.value = value
class Heap():
    def __init__(self, dary=2):
        self.heap = []
        self.dary = dary
    def siftdown(self, node, pos):
        c = self.minchild(pos)
        while c is not None and self.heap[c].key < node.key:
            self.heap[pos] = self.heap[c]
            self.heap[pos].pos = pos
            pos = c
            c = self.minchild(c)
        self.heap[pos] = node
        node.pos = pos
    def siftup(self, node, pos):
        p = self.parent(pos)
        while p is not None and self.heap[p].key > node.key:
            self.heap[pos] = self.heap[p]
            self.heap[pos].pos = pos
            pos = p
            p = self.parent(pos)
        self.heap[pos] = node
        node.pos = pos
    def findmin(self):
        return self.heap[0] if len(self.heap) > 0 else None
    def extractmin(self):
        if len(self.heap) == 0:
            return None
        i = self.heap[0]
        last = self.heap[-1]
        del self.heap[-1]
        if len(self.heap) > 0:
            self.siftdown(last, 0)
        return i
    def insert(self, key, value):
        self.heap.append(None)
        hi = HeapItem(key, value)
        self.siftup(hi, len(self.heap) - 1)
        return hi
    def decreasekey(self, node, newkey):
        node.key = newkey
        self.siftup(node, node.pos)
    def parent(self, pos):
        if pos == 0:
            return None
        return int(math.ceil(pos / self.dary) - 1)
    def children(self, pos):
        return range(self.dary * pos + 1, min(self.dary * (pos + 1) + 1, len(self.heap)))
    def minchild(self, pos):
        minpos = minkey = None
        for c in self.children(pos):
            if minkey is None or self.heap[c].key < minkey:
                minkey, minpos = self.heap[c].key, c
        return minpos
if __name__ == "__main__":
    heap = Heap(dary=3)
    heap.insert(5, "A")
    heap.insert(3, "B")
    heap.insert(8, "C")
    heap.insert(1, "D")
    print("Minimum:", heap.findmin().key)
    heap.extractmin()
    print("New Minimum:", heap.findmin().key)
