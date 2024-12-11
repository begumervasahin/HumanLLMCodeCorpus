import queue as Queue
class class1(str):
    def fonk1(self, other):
        return len(self) < len(other)
b1 = Queue.PriorityQueue()
b2 = ['jeej', 'kek', 'topkek', 'non']
for item in b2:
    b1.put(class1(item))
b3 = b1.get()
print("The smallest item in the PriorityQueue is:", b3)