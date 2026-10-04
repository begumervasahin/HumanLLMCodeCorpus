import math
class Edge:
    def __init__(self, weight):
        self.weight = weight
    def __repr__(self):
        return f"Edge({self.weight})"
class Heapq:
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
            current_element = self.data[index]
            self.data[index] = last_element
            if last_element.weight < current_element.weight:
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
            parent = (index - 1)
            if self.data[index].weight < self.data[parent].weight:
                self.data[index], self.data[parent] = self.data[parent], self.data[index]
                index = parent
            else:
                break
    def siftdown(self, index):
        while True:
            child_index = self.minchild(index)
            if child_index is None or self.data[child_index].weight >= self.data[index].weight:
                break
            self.data[index], self.data[child_index] = self.data[child_index], self.data[index]
            index = child_index
    def minchild(self, index):
        start = self.d * index + 1
        end = min(self.d * index + self.d, self.size() - 1)
        if start > end:
            return None
        min_idx = start
        min_weight = self.data[start].weight
        for i in range(start + 1, end + 1):
            if self.data[i].weight < min_weight:
                min_idx = i
                min_weight = self.data[i].weight
        return min_idx
    def __repr__(self):
        return str(self.data)
if __name__ == "__main__":
    edges = [Edge(weight) for weight in [5, 3, 8, 1, 2, 9, 7]]
    heap = Heapq(d=2)
    heap.make_heap(edges)
    print("Heap after creation:", heap)
    print("Minimum element:", heap.find_min())
    heap.delete_min()
    print("Heap after deleting minimum element:", heap)