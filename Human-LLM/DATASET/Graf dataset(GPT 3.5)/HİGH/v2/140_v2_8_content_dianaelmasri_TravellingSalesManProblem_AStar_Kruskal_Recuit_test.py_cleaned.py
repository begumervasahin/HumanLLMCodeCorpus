import queue as Queue
class class1(str):
    def fonk1(self, other):
        return len(self) < len(other)
b1 = Queue.PriorityQueue()
b1.put(class1('jeej'))
b1.put(class1('kek'))
b1.put(class1('topkek'))
b1.put(class1('non'))
b2 = sorted(b1.queue)[0]
print("The smallest item in the PriorityQueue is:", b2)