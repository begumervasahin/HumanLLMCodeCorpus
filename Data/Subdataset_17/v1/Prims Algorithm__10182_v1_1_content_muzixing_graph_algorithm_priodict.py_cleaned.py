class PriorityDictionary(dict):
    def __init__(self):
        '''Initialize PriorityDictionary by creating binary heap
        of pairs (value, key). Note that changing or removing a dict entry will
        not remove the old pair from the heap until it is found by smallest() or
        until the heap is rebuilt.'''
        self.__heap = []
        super().__init__()
    def smallest(self):
        '''Find smallest item after removing deleted items from heap.'''
        if len(self) == 0:
            raise IndexError("smallest of empty PriorityDictionary")
        heap = self.__heap
        while heap[0][1] not in self or self[heap[0][1]] != heap[0][0]:
            lastItem = heap.pop()
            if not heap:
                break
            insertionPoint = 0
            while 1:
                smallChild = 2 * insertionPoint + 1
                if smallChild + 1 < len(heap) and heap[smallChild] > heap[smallChild + 1]:
                    smallChild += 1
                if smallChild >= len(heap) or lastItem <= heap[smallChild]:
                    heap[insertionPoint] = lastItem
                    break
                heap[insertionPoint] = heap[smallChild]
                insertionPoint = smallChild
        return heap[0][1]
    def __iter__(self):
        '''Create destructive sorted iterator of PriorityDictionary.'''
        def iterfn():
            while len(self) > 0:
                x = self.smallest()
                yield x
                del self[x]
        return iterfn()
    def __setitem__(self, key, val):
        '''Change value stored in dictionary and add corresponding
        pair to heap. Rebuilds the heap if the number of deleted items grows
        too large, to avoid memory leakage.'''
        super().__setitem__(key, val)
        heap = self.__heap
        if len(heap) > 2 * len(self):
            self.__heap = [(v, k) for k, v in self.items()]
            self.__heap.sort()
        else:
            newPair = (val, key)
            insertionPoint = len(heap)
            heap.append(None)
            while insertionPoint > 0 and newPair < heap[(insertionPoint - 1)
                heap[insertionPoint] = heap[(insertionPoint - 1)
                insertionPoint = (insertionPoint - 1)
            heap[insertionPoint] = newPair
    def setdefault(self, key, val):
        '''Reimplement setdefault to call our customized __setitem__.'''
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