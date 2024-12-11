import queue as Q
class class1(str):
    def fonk1(self, other):
        return len(self) < len(other)
b1 = Q.PriorityQueue()
b1.put(class1('jeej'))
b1.put(class1('kek'))
b1.put(class1('topkek'))
b1.put(class1('non'))
b2 = sorted(b1.queue)[0]
print(b2)