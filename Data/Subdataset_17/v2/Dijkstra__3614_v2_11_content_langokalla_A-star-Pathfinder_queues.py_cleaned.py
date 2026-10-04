import collections
import heapq
class Queue:
    def __init__(self):
        self.elements = collections.deque()
    def is_empty(self) -> bool:
        return not self.elements
    def add(self, item):
        self.elements.append(item)
    def pop(self):
        return self.elements.popleft()
    def __len__(self) -> int:
        return len(self.elements)
class PriorityQueue:
    def __init__(self):
        self.elements = []
    def is_empty(self) -> bool:
        return not self.elements
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    def pop(self):
        return heapq.heappop(self.elements)[1]
    def __len__(self) -> int:
        return len(self.elements)
if __name__ == "__main__":
    queue = Queue()
    queue.add(1)
    queue.add(2)
    queue.add(3)
    print("Queue contents:")
    while not queue.is_empty():
        print(queue.pop())
    priority_queue = PriorityQueue()
    priority_queue.put("task1", 1)
    priority_queue.put("task2", 2)
    priority_queue.put("task3", 0)
    print("\nPriorityQueue contents:")
    while not priority_queue.is_empty():
        print(priority_queue.pop())