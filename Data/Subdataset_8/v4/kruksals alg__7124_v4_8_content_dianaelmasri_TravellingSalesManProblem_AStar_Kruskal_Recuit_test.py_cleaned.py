import queue as Q
class CustomComparator:
    def __lt__(self, other):
        return len(self) < len(other)
heap = Q.PriorityQueue()
heap.put('jeej')
heap.put('kek')
heap.put('topkek')
heap.put('non')
smallest = sorted(heap.queue)[0]
print(smallest)