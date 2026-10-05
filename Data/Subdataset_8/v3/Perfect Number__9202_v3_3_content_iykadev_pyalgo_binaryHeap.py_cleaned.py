class BinaryHeap:
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0
    def insert(self, key):
        self.heap_list.append(key)
        self.current_size += 1
        self._percolate_up(self.current_size)
    def delete_min(self):
        if self.current_size == 0:
            return None
        min_value = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size -= 1
        self.heap_list.pop()
        self._percolate_down(1)
        return min_value
    def build_heap(self, alist):
        self.current_size = len(alist)
        self.heap_list = [0] + alist[:]
        mid_point = len(alist)
        for i in range(mid_point, 0, -1):
            self._percolate_down(i)
    def _percolate_up(self, i):
        while i
            if self.heap_list[i] < self.heap_list[i
                self._swap(i, i
            i
    def _percolate_down(self, i):
        while i * 2 <= self.current_size:
            mc = self._min_child(i)
            if self.heap_list[i] > self.heap_list[mc]:
                self._swap(i, mc)
            i = mc
    def _min_child(self, i):
        left_child = i * 2
        right_child = left_child + 1
        if right_child > self.current_size:
            return left_child
        else:
            return left_child if self.heap_list[left_child] < self.heap_list[right_child] else right_child
    def _swap(self, i, j):
        self.heap_list[i], self.heap_list[j] = self.heap_list[j], self.heap_list[i]
bh = BinaryHeap()
bh.build_heap([9, 5, 6, 2, 3])
print(bh.delete_min())
print(bh.delete_min())
print(bh.delete_min())
print(bh.delete_min())
print(bh.delete_min())