import queue as Queue
class ComparableString(str):
    def __lt__(self, other):
        return len(self) < len(other)
priority_queue = Queue.PriorityQueue()
priority_queue.put(ComparableString('jeej'))
priority_queue.put(ComparableString('kek'))
priority_queue.put(ComparableString('topkek'))
priority_queue.put(ComparableString('non'))
smallest_item = sorted(priority_queue.queue)[0]
print("The smallest item in the PriorityQueue is:", smallest_item)