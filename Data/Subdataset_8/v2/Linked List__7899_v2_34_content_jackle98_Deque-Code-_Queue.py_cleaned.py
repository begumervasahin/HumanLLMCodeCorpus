from collections import deque
class Queue:
    def __init__(self):
        self._queue = deque()
    def __str__(self):
        return str(self._queue)
    def __len__(self):
        return len(self._queue)
    def enqueue(self, value):
        self._queue.append(value)
    def dequeue(self):
        if len(self._queue) == 0:
            return None
        return self._queue.popleft()
if __name__ == "__main__":
    my_queue = Queue()
    my_queue.enqueue(1)
    my_queue.enqueue(2)
    my_queue.enqueue(3)
    print("Queue:", my_queue)
    print("Length:", len(my_queue))
    dequeued_value = my_queue.dequeue()
    print("Dequeued value:", dequeued_value)
    print("Queue after dequeue:", my_queue)