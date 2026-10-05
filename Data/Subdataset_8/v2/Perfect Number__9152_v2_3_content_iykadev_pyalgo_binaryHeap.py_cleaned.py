class BinaryHeap:
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0
    def percolate_up(self, i):
        while i
            if self.heap_list[i] < self.heap_list[i
                self.heap_list[i], self.heap_list[i
            i = i
    def insert(self, k):
        self.heap_list.append(k)
        self.current_size += 1
        self.percolate_up(self.current_size)
    def percolate_down(self, i):
        while (i * 2) <= self.current_size:
            min_child = self.min_child(i)
            if self.heap_list[i] > self.heap_list[min_child]:
                self.heap_list[i], self.heap_list[min_child] = self.heap_list[min_child], self.heap_list[i]
            i = min_child
    def min_child(self, i):
        left_child = i * 2
        right_child = (i * 2) + 1
        if right_child > self.current_size:
            return left_child
        else:
            if self.heap_list[left_child] < self.heap_list[right_child]:
                return left_child
            else:
                return right_child
    def delete_min(self):
        if self.current_size == 0:
            return None
        min_value = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size -= 1
        self.heap_list.pop()
        self.percolate_down(1)
        return min_value
    def build_heap(self, alist):
        mid_point = len(alist)
        self.current_size = len(alist)
        self.heap_list = [0] + alist[:]
        for i in range(mid_point, 0, -1):
            self.percolate_down(i)
bh = BinaryHeap()
bh.build_heap([9, 5, 6, 2, 3])
print(bh.delete_min())
print(bh.delete_min())
print(bh.delete_min())
print(bh.delete_min())
print(bh.delete_min())