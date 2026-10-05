class BinaryHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0
    def perc_up(self, i):
        while i
            if self.heapList[i] < self.heapList[i
                self.heapList[i], self.heapList[i
            i
    def insert(self, k):
        self.heapList.append(k)
        self.currentSize += 1
        self.perc_up(self.currentSize)
    def perc_down(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.min_child(i)
            if self.heapList[i] > self.heapList[mc]:
                self.heapList[i], self.heapList[mc] = self.heapList[mc], self.heapList[i]
            i = mc
    def min_child(self, i):
        left_child_idx = i * 2
        right_child_idx = left_child_idx + 1
        if right_child_idx > self.currentSize:
            return left_child_idx
        else:
            return left_child_idx if self.heapList[left_child_idx] < self.heapList[right_child_idx] else right_child_idx
    def del_min(self):
        if self.currentSize == 0:
            raise IndexError("Cannot delete from an empty heap")
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -= 1
        self.heapList.pop()
        self.perc_down(1)
        return retval
    def build_heap(self, alist):
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        for i in range(self.currentSize
            self.perc_down(i)
bh = BinaryHeap()
bh.build_heap([9, 5, 6, 2, 3])
print(bh.del_min())
print(bh.del_min())
print(bh.del_min())
print(bh.del_min())
print(bh.del_min())