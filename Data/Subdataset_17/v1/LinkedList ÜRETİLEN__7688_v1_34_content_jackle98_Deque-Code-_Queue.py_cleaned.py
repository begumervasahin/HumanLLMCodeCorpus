
from collections import deque
def get_deque(size):
    return deque(maxlen=size)
class Queue:
    def __init__(self):
        self._dq = get_deque(1)
    def __str__(self):
        return str(self._dq)
    def __len__(self):
        return len(self._dq)
    def enqueue(self, val):
        self._dq.append(val)
    def dequeue(self):
        if len(self._dq) == 0:
            return None
        return self._dq.popleft()
if __name__ == "__main__":
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    print("Queue after enqueuing 10, 20, 30:")
    print(q)
    print("Dequeue element:", q.dequeue())
    print("Queue after dequeue:")
    print(q)
    print("Dequeue element:", q.dequeue())
    print("Queue after dequeue:")
    print(q)
    print("Dequeue element:", q.dequeue())
    print("Queue after dequeue:")
    print(q)
    print("Dequeue element (should return None):", q.dequeue())