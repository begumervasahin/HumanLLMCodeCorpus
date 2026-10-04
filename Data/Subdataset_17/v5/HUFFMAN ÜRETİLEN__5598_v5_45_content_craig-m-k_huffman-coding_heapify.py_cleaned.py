class Heap:
    def __init__(self, heap_type: str):
        if heap_type not in {'max', 'min'}:
            raise ValueError("heap_type must be either 'max' or 'min'")
        self.queue = []
        self.heap_type = heap_type
    def __len__(self) -> int:
        return len(self.queue)
    def insert(self, key):
        self.queue.append(key)
        self._perc_up(len(self.queue) - 1)
    def pop(self):
        if not self.queue:
            raise IndexError("pop from empty heap")
        self._swap(0, len(self.queue) - 1)
        popped_key = self.queue.pop()
        if self.queue:
            self._heapify(0)
        return popped_key
    def build_heap(self):
        for i in range((len(self.queue)
            self._heapify(i)
    def _perc_up(self, index: int):
        parent = (index - 1)
        while index > 0 and self._compare(self.queue[parent], self.queue[index]):
            self._swap(index, parent)
            index = parent
            parent = (index - 1)
    def _heapify(self, index: int):
        left = 2 * index + 1
        right = 2 * index + 2
        extreme = index
        if left < len(self.queue) and self._compare(self.queue[extreme], self.queue[left]):
            extreme = left
        if right < len(self.queue) and self._compare(self.queue[extreme], self.queue[right]):
            extreme = right
        if extreme != index:
            self._swap(index, extreme)
            self._heapify(extreme)
    def _compare(self, parent_val, child_val) -> bool:
        if self.heap_type == 'max':
            return parent_val < child_val
        return parent_val > child_val
    def _swap(self, i: int, j: int):
        self.queue[i], self.queue[j] = self.queue[j], self.queue[i]