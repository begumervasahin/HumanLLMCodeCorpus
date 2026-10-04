class HeapItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value
    def __repr__(self):
        return f"({self.key}, {self.value})"
class MinHeap:
    def __init__(self):
        self.heap = []
        self.index = {}
    def key(self, value):
        return self.heap[self.index[value]].key
    def left(self, i):
        return 2 * i + 1
    def right(self, i):
        return 2 * (i + 1)
    def parent(self, i):
        return (i - 1)
    def min_heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        smallest = i
        if l < len(self.heap) and self.heap[l].key < self.heap[smallest].key:
            smallest = l
        if r < len(self.heap) and self.heap[r].key < self.heap[smallest].key:
            smallest = r
        if smallest != i:
            self.swap(i, smallest)
            self.min_heapify(smallest)
    def extract_min(self):
        if not self:
            return None
        self.swap(0, len(self.heap) - 1)
        min_item = self.heap.pop()
        del self.index[min_item.value]
        self.min_heapify(0)
        return min_item.key, min_item.value
    def insert(self, key, value):
        self.heap.append(HeapItem(key, value))
        self.index[value] = len(self.heap) - 1
        self.decrease_key(value, key)
    def decrease_key(self, value, new_key):
        i = self.index[value]
        self.heap[i].key = new_key
        while i > 0 and self.heap[i].key < self.heap[self.parent(i)].key:
            self.swap(i, self.parent(i))
            i = self.parent(i)
    def swap(self, i, j):
        self.index[self.heap[i].value], self.index[self.heap[j].value] = j, i
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    def __len__(self):
        return len(self.heap)
    def __bool__(self):
        return bool(self.heap)
    def __contains__(self, value):
        return value in self.index
if __name__ == "__main__":
    heap = MinHeap()
    heap.insert(3, "apple")
    heap.insert(1, "banana")
    heap.insert(2, "cherry")
    print("Heap after inserts:", heap.heap)
    print("Extracting min:", heap.extract_min())
    print("Heap after extracting min:", heap.heap)
    heap.decrease_key("cherry", 0)
    print("Heap after decreasing key:", heap.heap)