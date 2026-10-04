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
    def get_key(self, value):
        return self.heap[self.index[value]].key
    def left_child(self, index):
        return 2 * index + 1
    def right_child(self, index):
        return 2 * (index + 1)
    def parent(self, index):
        return (index - 1)
    def min_heapify(self, index):
        left = self.left_child(index)
        right = self.right_child(index)
        smallest = index
        if left < len(self.heap) and self.heap[left].key < self.heap[smallest].key:
            smallest = left
        if right < len(self.heap) and self.heap[right].key < self.heap[smallest].key:
            smallest = right
        if smallest != index:
            self.swap(index, smallest)
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
        index = self.index[value]
        self.heap[index].key = new_key
        while index > 0 and self.heap[index].key < self.heap[self.parent(index)].key:
            self.swap(index, self.parent(index))
            index = self.parent(index)
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