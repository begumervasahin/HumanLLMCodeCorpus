import math
class HeapItem:
    def __init__(self, key, value):
        self.key = key
        self.pos = None
        self.value = value
class Heap:
    def __init__(self, dary=2):
        self.heap = []
        self.dary = dary
    def siftdown(self, node, pos):
        child_pos = self.minchild(pos)
        while child_pos is not None and self.heap[child_pos].key < node.key:
            self.heap[pos] = self.heap[child_pos]
            self.heap[pos].pos = pos
            pos = child_pos
            child_pos = self.minchild(child_pos)
        self.heap[pos] = node
        node.pos = pos
    def siftup(self, node, pos):
        parent_pos = self.parent(pos)
        while parent_pos is not None and self.heap[parent_pos].key > node.key:
            self.heap[pos] = self.heap[parent_pos]
            self.heap[pos].pos = pos
            pos = parent_pos
            parent_pos = self.parent(pos)
        self.heap[pos] = node
        node.pos = pos
    def findmin(self):
        return self.heap[0] if self.heap else None
    def extractmin(self):
        if not self.heap:
            return None
        min_item = self.heap[0]
        last_item = self.heap.pop()
        if self.heap:
            self.siftdown(last_item, 0)
        return min_item
    def insert(self, key, value):
        new_item = HeapItem(key, value)
        self.heap.append(new_item)
        self.siftup(new_item, len(self.heap) - 1)
        return new_item
    def decreasekey(self, node, newkey):
        node.key = newkey
        self.siftup(node, node.pos)
    def parent(self, pos):
        if pos == 0:
            return None
        return (pos - 1)
    def children(self, pos):
        return range(self.dary * pos + 1, min(self.dary * (pos + 1) + 1, len(self.heap)))
    def minchild(self, pos):
        min_pos = None
        min_key = None
        for child_pos in self.children(pos):
            if min_key is None or self.heap[child_pos].key < min_key:
                min_key = self.heap[child_pos].key
                min_pos = child_pos
        return min_pos
if __name__ == "__main__":
    heap = Heap(dary=3)
    heap.insert(5, "A")
    heap.insert(3, "B")
    heap.insert(8, "C")
    heap.insert(1, "D")
    print("Minimum:", heap.findmin().key)
    heap.extractmin()
    print("New Minimum:", heap.findmin().key)
