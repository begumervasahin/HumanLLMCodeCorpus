from Deque_Generator import get_deque
class Queue:
    def __init__(self):
        self._deque = get_deque(1)
    def __str__(self):
        return str(self._deque)
    def __len__(self):
        return len(self._deque)
    def enqueue(self, value):
        self._deque.push_back(value)
    def dequeue(self):
        if len(self._deque) == 0:
            return None
        return self._deque.pop_front()