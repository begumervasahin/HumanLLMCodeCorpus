class EmptyPriorityQueue(Exception):
    pass
class Item:
    def __init__(self, key, value):
        self.key = key
        self.value = value
class PriorityQueueBase:
    def is_empty(self):
        return len(self) == 0
class HeapPriorityQueue(PriorityQueueBase):
    def __init__(self):
        self.data = []
    def __len__(self):
        return len(self.data)
    def _parent(self, j):
        return (j - 1)
    def _left(self, j):
        return 2 * j + 1
    def _right(self, j):
        return 2 * j + 2
    def _has_left(self, j):
        return self._left(j) < len(self.data)
    def _has_right(self, j):
        return self._right(j) < len(self.data)
    def _swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]
    def _upheap(self, j):
        parent = self._parent(j)
        if j > 0 and self.data[j].key < self.data[parent].key:
            self._swap(j, parent)
            self._upheap(parent)
    def _downheap(self, j):
        if self._has_left(j):
            left = self._left(j)
            small_child = left
            if self._has_right(j):
                right = self._right(j)
                if self.data[right].key < self.data[left].key:
                    small_child = right
            if self.data[small_child].key < self.data[j].key:
                self._swap(j, small_child)
                self._downheap(small_child)
    def add(self, key, value):
        self.data.append(Item(key, value))
        self._upheap(len(self.data) - 1)
    def min(self):
        if self.is_empty():
            raise EmptyPriorityQueue('Priority queue is empty.')
        item = self.data[0]
        return (item.key, item.value)
    def remove_min(self):
        if self.is_empty():
            raise EmptyPriorityQueue('Priority queue is empty.')
        self._swap(0, len(self.data) - 1)
        item = self.data.pop()
        self._downheap(0)
        return (item.key, item.value)
pq = HeapPriorityQueue()
pq.add(4, 'Four')
pq.add(2, 'Two')
pq.add(1, 'One')
print(pq.min())
print(pq.remove_min())
print(len(pq))
