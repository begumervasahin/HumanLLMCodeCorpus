import queue as Q
def string_length_comparator(self, other):
    return len(self) < len(other)
str.__lt__ = string_length_comparator
heap = Q.PriorityQueue()
heap.put('jeej')
heap.put('kek')
heap.put('topkek')
heap.put('non')
shortest_string = sorted(heap.queue)[0]
print(shortest_string)