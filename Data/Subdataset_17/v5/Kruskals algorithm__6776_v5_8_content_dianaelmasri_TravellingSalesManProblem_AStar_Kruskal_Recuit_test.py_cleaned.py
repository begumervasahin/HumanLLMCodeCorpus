import queue as Q
def string_length_comparator(self, other):
    return len(self) < len(other)
str.__lt__ = string_length_comparator
priority_queue = Q.PriorityQueue()
priority_queue.put('jeej')
priority_queue.put('kek')
priority_queue.put('topkek')
priority_queue.put('non')
shortest_string = priority_queue.get()
print("Shortest string by length:", shortest_string)