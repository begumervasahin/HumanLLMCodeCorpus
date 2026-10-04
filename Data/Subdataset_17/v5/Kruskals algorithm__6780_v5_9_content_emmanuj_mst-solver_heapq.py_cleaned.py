
from edge import Edge
class DaryHeap:
    def __init__(self, d):
        self.data = []
        self.d = d
    def make_heap(self, lst):
        self.data = lst
        for i in range(self.size() - 1, -1, -1):
            self.sift_down(i)
    def find_min(self):
        return self.data[0] if self.data else None
    def delete(self, index):
        if index == self.size() - 1:
            self.data.pop()
        else:
            last_item = self.data.pop()
            self.data[index] = last_item
            if last_item.weight < self.data[index].weight:
                self.sift_up(index)
            else:
                self.sift_down(index)
    def delete_min(self):
        if self.size() > 0:
            self.delete(0)
    def size(self):
        return len(self.data)
    def sift_up(self, index):
        while index > 0:
            parent_index = (index - 1)
            if self.data[parent_index].weight <= self.data[index].weight:
                break
            self.data[index], self.data[parent_index] = self.data[parent_index], self.data[index]
            index = parent_index
    def sift_down(self, index):
        while True:
            min_child_index = self.find_min_child(index)
            if min_child_index is None or self.data[index].weight <= self.data[min_child_index].weight:
                break
            self.data[index], self.data[min_child_index] = self.data[min_child_index], self.data[index]
            index = min_child_index
    def find_min_child(self, index):
        start_child = self.d * index + 1
        end_child = min(self.d * index + self.d, self.size() - 1)
        if start_child >= self.size():
            return None
        min_child_index = start_child
        for i in range(start_child + 1, end_child + 1):
            if self.data[i].weight < self.data[min_child_index].weight:
                min_child_index = i
        return min_child_index
    def __repr__(self):
        return f"DaryHeap({self.d}): " + str(self.data)