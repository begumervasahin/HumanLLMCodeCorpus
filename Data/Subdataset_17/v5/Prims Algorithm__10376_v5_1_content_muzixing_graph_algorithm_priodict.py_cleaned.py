from __future__ import generators
class priorityDictionary(dict):
    def __init__(self):
        self.__heap = []
        super().__init__()
    def smallest(self):
        if len(self) == 0:
            raise IndexError("smallest of empty priorityDictionary")
        heap = self.__heap
        while heap and (heap[0][1] not in self or self[heap[0][1]] != heap[0][0]):
            lastItem = heap.pop()
            insertionPoint = 0
            while True:
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
        def iterfn():
            while len(self) > 0:
                smallest_item = self.smallest()
                yield smallest_item
                del self[smallest_item]
        return iterfn()
    def __setitem__(self, key, val):
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
        if key not in self:
            self[key] = val
        return self[key]