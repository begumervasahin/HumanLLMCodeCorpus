import queue as Q
class CustomComparator:
    def __lt__(self, other):
        return len(self) < len(other)
priority_queue = Q.PriorityQueue()
elements = ['jeej', 'kek', 'topkek', 'non']
for element in elements:
    priority_queue.put(element)
smallest = priority_queue.get()
print(smallest)