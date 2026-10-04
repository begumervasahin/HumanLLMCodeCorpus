import heapq
class PriorityQueue:
    def __init__(self):
        self.elements = []
    def empty(self):
        return len(self.elements) == 0
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    def get(self):
        if self.empty():
            raise IndexError("get from an empty priority queue")
        return heapq.heappop(self.elements)[1]
if __name__ == "__main__":
    pq = PriorityQueue()
    pq.put("task1", priority=5)
    pq.put("task2", priority=1)
    pq.put("task3", priority=3)
    while not pq.empty():
        item = pq.get()
        print(item)