
from edge import Edge
class Heapq:
    def __init__(self, d):
        self.data = []
        self.d = d
    def make_heap(self, lst):
        self.data = lst
        for k in range(self.size() - 1, -1, -1):
            self.siftdown(k)
    def find_min(self):
        return self.data[0] if self.data else None
    def delete(self, k):
        if k == self.size() - 1:
            self.data.pop()
        else:
            last_item = self.data.pop()
            self.data[k] = last_item
            if last_item.weight < self.data[k].weight:
                self.siftup(k)
            else:
                self.siftdown(k)
    def delete_min(self):
        if self.size() > 0:
            self.delete(0)
    def size(self):
        return len(self.data)
    def siftup(self, k):
        while k > 0:
            parent_index = (k - 1)
            if self.data[parent_index].weight <= self.data[k].weight:
                break
            self.data[k], self.data[parent_index] = self.data[parent_index], self.data[k]
            k = parent_index
    def siftdown(self, k):
        while True:
            min_child_index = self.minchild(k)
            if min_child_index is None or self.data[k].weight <= self.data[min_child_index].weight:
                break
            self.data[k], self.data[min_child_index] = self.data[min_child_index], self.data[k]
            k = min_child_index
    def minchild(self, k):
        start_child = self.d * k + 1
        end_child = min(self.d * k + self.d, self.size() - 1)
        if start_child >= self.size():
            return None
        min_child_index = start_child
        for i in range(start_child + 1, end_child + 1):
            if self.data[i].weight < self.data[min_child_index].weight:
                min_child_index = i
        return min_child_index
    def __repr__(self):
        return str(self.data)