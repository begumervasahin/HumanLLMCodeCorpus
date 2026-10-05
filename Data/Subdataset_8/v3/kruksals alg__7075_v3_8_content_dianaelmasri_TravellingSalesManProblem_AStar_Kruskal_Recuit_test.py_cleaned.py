import queue as Queue
class ComparableString(str):
    def __lt__(self, other):
        return len(self) < len(other)
priority_queue = Queue.PriorityQueue()
items_to_enqueue = ['jeej', 'kek', 'topkek', 'non']
for item in items_to_enqueue:
    priority_queue.put(ComparableString(item))
smallest_item = priority_queue.get()
print("The smallest item in the PriorityQueue is:", smallest_item)