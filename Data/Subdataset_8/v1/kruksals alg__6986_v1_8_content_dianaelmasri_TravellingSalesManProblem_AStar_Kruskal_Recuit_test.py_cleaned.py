import queue as Q
class ComparableString(str):
    def __lt__(self, other):
        return len(self) < len(other)
heap = Q.PriorityQueue()
heap.put(ComparableString('jeej'))
heap.put(ComparableString('kek'))
heap.put(ComparableString('topkek'))
heap.put(ComparableString('non'))
smallest_item = sorted(heap.queue)[0]
print(smallest_item)