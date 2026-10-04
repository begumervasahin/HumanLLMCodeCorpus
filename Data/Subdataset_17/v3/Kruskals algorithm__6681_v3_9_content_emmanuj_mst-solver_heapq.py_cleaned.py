import math
class Edge:
    def __init__(self, weight):
        self.weight = weight
    def __repr__(self):
        return f"Edge({self.weight})"
class DaryHeap:
    def __init__(self, d):
        self.data = []
        self.d = d
    def make_heap(self, lst):
        self.data = lst
        for index in range(self.size() - 1, -1, -1):
            self.siftdown(index)
    def find_min(self):
        return self.data[0] if self.size() > 0 else None
    def delete(self, index):
        if index == self.size() - 1:
            self.data.pop()
        else:
            last_element = self.data.pop()
            self.data[index] = last_element
            if last_element.weight < self.data[index].weight:
                self.siftup(index)
            else:
                self.siftdown(index)
    def delete_min(self):
        if self.size() > 0:
            self.delete(0)
    def size(self):
        return len(self.data)
    def siftup(self, index):
        while index > 0:
            parent_index = (index - 1)
            if self.data[index].weight < self.data[parent_index].weight:
                self.data[index], self.data[parent_index] = self.data[parent_index], self.data[index]
                index = parent_index
            else:
                break
    def siftdown(self, index):
        while True:
            child_index = self._find_min_child(index)
            if child_index is None or self.data[child_index].weight >= self.data[index].weight:
                break
            self.data[index], self.data[child_index] = self.data[child_index], self.data[index]
            index = child_index
    def _find_min_child(self, index):
        start = self.d * index + 1
        end = min(self.d * index + self.d, self.size() - 1)
        if start > end:
            return None
        min_index = start
        min_weight = self.data[start].weight
        for i in range(start + 1, end + 1):
            if self.data[i].weight < min_weight:
                min_index = i
                min_weight = self.data[i].weight
        return min_index
    def __repr__(self):
        return str(self.data)
if __name__ == "__main__":
    edges = [Edge(weight) for weight in [5, 3, 8, 1, 2, 9, 7]]
    heap = DaryHeap(d=2)
    heap.make_heap(edges)
    print("Heap after creation:", heap)
    print("Minimum element:", heap.find_min())
    heap.delete_min()
    print("Heap after deleting minimum element:", heap)