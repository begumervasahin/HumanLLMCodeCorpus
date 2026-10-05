class MaxHeap(object):
    def __init__(self):
        self.H = [-1]
        self.D = [-1]
        self.n = 0
    def maximum(self):
        return self.H[1]
    def insert(self, name, value):
        self.n += 1
        self.H.append(name)
        self.D.append(value)
        self.heapify(self.n)
    def update(self, name, value):
        for i in range(1, self.n + 1):
            if self.H[i] == name:
                self.D[i] = value
                self.heapify(i)
                break
    def delete(self, h):
        if self.n == 1 or h == self.n:
            self.D.pop()
            self.H.pop()
            self.n -= 1
        else:
            self.D[h] = self.D.pop()
            self.H[h] = self.H.pop()
            self.n -= 1
            self.heapify(h)
    def heapify(self, k):
        if k > 1 and self.D[k] > self.D[k
            h = k
            while h > 1 and self.D[h] > self.D[h
                self.swap(h, h
                h
        else:
            while k <= self.n
                d = 2 * k
                if 2 * k + 1 <= self.n and self.D[2 * k] < self.D[2 * k + 1]:
                    d = 2 * k + 1
                self.swap(k, d)
                k = d
    def swap(self, h, d):
        self.D[h], self.D[d] = self.D[d], self.D[h]
        self.H[h], self.H[d] = self.H[d], self.H[h]
    def heap_sort(self):
        sorted_edges = []
        sorted_weights = []
        while self.n >= 1:
            sorted_edges.append(self.H[1])
            sorted_weights.append(self.D[1])
            self.delete(1)
        return sorted_weights, sorted_edges
mh = MaxHeap()
mh.insert(1, 10)
print('\n', mh.H, mh.D)
mh.insert(2, 30)
print('\n', mh.H, mh.D)
mh.insert(3, 40)
print('\n', mh.H, mh.D)
mh.insert(4, 15)
print('\n', mh.H, mh.D)
mh.insert(5, 60)
print('\n', mh.H, mh.D)
print(mh.maximum())
mh.delete(1)
print('\n', mh.H, mh.D)
print(mh.maximum())
