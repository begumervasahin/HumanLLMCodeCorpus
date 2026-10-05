from Deque_Generator import get_deque
class Queue:
  def __init__(self):
    self._dq = get_deque(1)
  def __str__(self):
      string = self._dq.__str__()
      return string
  def __len__(self):
      length = self._dq.__len__()
      return length
  def enqueue(self, val):
    self._dq.push_back(val)
  def dequeue(self):
    if len(self._dq) == 0:
        return None
    dequeued = self._dq.pop_front()
    return dequeued