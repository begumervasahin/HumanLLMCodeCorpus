import collections
import heapq
class Queue:
    def __init__(self):
        self.elements = collections.deque()
    def empty(self) -> bool:
        return len(self.elements) == 0
    def add(self, x):
        self.elements.append(x)
    def pop(self):
        return self.elements.popleft()
    def __len__(self) -> int:
        return len(self.elements)
class PriorityQueue:
    def __init__(self):
        self.elements = []
    def empty(self) -> bool:
        return len(self.elements) == 0
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    def pop(self):
        return heapq.heappop(self.elements)[1]
    def __len__(self) -> int:
        return len(self.elements)
queue = Queue()
queue.add(1)
queue.add(2)
queue.add(3)
print("Queue contents:")
while not queue.empty():
    print(queue.pop())
priority_queue = PriorityQueue()
priority_queue.put("task1", 1)
priority_queue.put("task2", 2)
priority_queue.put("task3", 0)
print("\nPriorityQueue contents:")
while not priority_queue.empty():
    print(priority_queue.pop())