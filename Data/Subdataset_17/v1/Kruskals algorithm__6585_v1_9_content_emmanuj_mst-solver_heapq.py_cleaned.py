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
        for k in range(self.size() - 1, -1, -1):
            self.siftdown(k)
    def find_min(self):
        return self.data[0] if self.size() > 0 else None
    def delete(self, k):
        if k == self.size() - 1:
            self.data.pop()
        else:
            last = self.data.pop()
            item = self.data[k]
            self.data[k] = last
            if last.weight < item.weight:
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
            parent = (k - 1)
            if self.data[k].weight < self.data[parent].weight:
                self.data[k], self.data[parent] = self.data[parent], self.data[k]
                k = parent
            else:
                break
    def siftdown(self, k):
        while True:
            j = self.minchild(k)
            if j is None or self.data[j].weight >= self.data[k].weight:
                break
            self.data[k], self.data[j] = self.data[j], self.data[k]
            k = j
    def minchild(self, k):
        start = self.d * k + 1
        end = min(self.d * k + self.d, self.size() - 1)
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