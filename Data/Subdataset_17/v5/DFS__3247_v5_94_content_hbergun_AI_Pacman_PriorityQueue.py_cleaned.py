import heapq
class PriorityQueue:
    def __init__(self):
        self._elements = []
    def is_empty(self):
        return len(self._elements) == 0
    def add(self, item, priority):
        heapq.heappush(self._elements, (priority, item))
    def pop(self):
        if self.is_empty():
            raise IndexError("Cannot pop from an empty priority queue")
        return heapq.heappop(self._elements)[1]
if __name__ == "__main__":
    pq = PriorityQueue()
    pq.add("task1", priority=5)
    pq.add("task2", priority=1)
    pq.add("task3", priority=3)
    while not pq.is_empty():
        item = pq.pop()
        print(item)