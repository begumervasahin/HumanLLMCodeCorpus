class PriorityDictionary(dict):
    def __init__(self):
        self.__heap = []
        super().__init__()
    def smallest(self):
        if not self:
            raise IndexError("smallest of empty PriorityDictionary")
        heap = self.__heap
        while heap:
            value, key = heap[0]
            if key in self and self[key] == value:
                return key
            lastItem = heap.pop()
            if not heap:
                break
            insertion_point = 0
            while True:
                small_child = 2 * insertion_point + 1
                if small_child + 1 < len(heap) and heap[small_child] > heap[small_child + 1]:
                    small_child += 1
                if small_child >= len(heap) or lastItem <= heap[small_child]:
                    heap[insertion_point] = lastItem
                    break
                heap[insertion_point] = heap[small_child]
                insertion_point = small_child
        raise IndexError("Heap exhausted without finding valid smallest element")
    def __iter__(self):
        def iter_fn():
            while self:
                smallest_item = self.smallest()
                yield smallest_item
                del self[smallest_item]
        return iter_fn()
    def __setitem__(self, key, val):
        super().__setitem__(key, val)
        heap = self.__heap
        if len(heap) > 2 * len(self):
            self.__rebuild_heap()
        else:
            self.__add_to_heap(val, key)
    def __rebuild_heap(self):
        self.__heap = [(v, k) for k, v in self.items()]
        self.__heap.sort()
    def __add_to_heap(self, val, key):
        new_pair = (val, key)
        heap = self.__heap
        insertion_point = len(heap)
        heap.append(None)
        while insertion_point > 0 and new_pair < heap[(insertion_point - 1)
            heap[insertion_point] = heap[(insertion_point - 1)
            insertion_point = (insertion_point - 1)
        heap[insertion_point] = new_pair
    def setdefault(self, key, val):
        if key not in self:
            self[key] = val
        return self[key]
if __name__ == "__main__":
    pd = PriorityDictionary()
    pd[1] = 5
    pd[2] = 9
    pd[3] = 3
    pd[4] = 7
    print("Priority Dictionary elements in sorted order:")
    for key in pd:
        print(key)