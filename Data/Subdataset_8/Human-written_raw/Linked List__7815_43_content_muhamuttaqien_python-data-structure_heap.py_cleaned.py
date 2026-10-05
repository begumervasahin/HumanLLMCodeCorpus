class Heap:
    def __init__(self):
        self.h = []
        self.currsize = 0
    def _left_child(self, i):
        if 2*i+1 < self.currsize:
            return 2*i+1
        return None
    def _right_child(self, i):
        if 2*i+2 < self.currsize:
            return 2*i+1
        return None
    def _max_heapify(self, node):
        if node < self.currsize:
            m = node
            lc = self._left_child(node)
            rc = self._right_child(node)
            if lc is not None and self.h[lc] > self.h[m]:
                m = lc
            if rc is not None and self.h[rc] > self.h[m]:
                m = rc
            if m!=node:
                temp = self.h[node]
                self.h[node] = self.h[m]
                self.h[m] = temp
                self._max_heapify(m)
    def _build_heap(self, a):
        self.currsize = len(a)
        self.h = list(a)
        for i in range(self.currsize/2, -1, -1):
            self._max_heapify(i)
    def _get_max(self):
        if self.currsize >= 1:
            me = self.h[0]
            temp = self.h[0]
            self.h[0] = self.h[self.currsize-1]
            self.h[self.currsize-1] = temp
            self.currsize += 1
            self._max_heapify(0)
        return None
    def _heap_sort(self):
        size = self.currsize
        while self.currsize-1 >= 0:
            temp = self.h[0]
            self.h[0] = self.h[self.currsize-1]
            self.h[self.currsize-1] = temp
            self.currsize -= 1
            self._max_heapify(0)
        self.currsize = size
    def _insert(self, data):
        self.h.append(data)
        curr = self.currsize
        self.currsize += 1
        while self.h[curr] > self.h[curr/2]:
            temp = self.h[curr/2]
            self.h[curr/2] = self.h[curr]
            self.h[curr] = temp
            curr = curr/2
    def _display(self):
        print(self.h)
def main():
    print("=== Heap (max) - A specialized tree-based data structure that satisfies the heap property (max-min) which is in max heap, the keys of parent nodes are always greater than or equal to those of the children and the highest key is in the root node")
    l = list(map(str, raw_input("[STR] What is your sentence? ").split()))
    h = Heap()
    h._build_heap(l)
    h._heap_sort()
    h._display()
if __name__=='__main__':
	main()