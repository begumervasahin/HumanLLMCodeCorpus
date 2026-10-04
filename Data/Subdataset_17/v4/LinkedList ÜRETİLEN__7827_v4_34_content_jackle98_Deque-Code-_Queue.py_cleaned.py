from Deque_Generator import get_deque
class Queue:
    def __init__(self):
        self._dq = get_deque(1)
    def __str__(self):
        return str(self._dq)
    def __len__(self):
        return len(self._dq)
    def enqueue(self, val):
        self._dq.push_back(val)
    def dequeue(self):
        if len(self._dq) == 0:
            return None
        return self._dq.pop_front()
if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print("Queue after enqueuing 10, 20, 30:", queue)
    print("Length of queue:", len(queue))
    print("Dequeued element:", queue.dequeue())
    print("Queue after dequeuing an element:", queue)
    print("Length of queue:", len(queue))