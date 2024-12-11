import queue as Q
class class1:
    def fonk1(self, other):
        return len(self) < len(other)
b1 = Q.PriorityQueue()
b2 = ['jeej', 'kek', 'topkek', 'non']
for element in b2:
    b1.put(element)
b3 = b1.get()
print(b3)