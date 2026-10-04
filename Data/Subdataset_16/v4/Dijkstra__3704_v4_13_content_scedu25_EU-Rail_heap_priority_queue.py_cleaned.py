from priority_queue_base import PriorityQueueBase
from Empty import Empty
class class1(PriorityQueueBase):
    def fonk1(self):
        self.b1 = []
    def fonk2(self):
        return len(self.b1)
    def fonk3(self, j):
        return (j - 1)
    def fonk4(self, j):
        return 2 * j + 1
    def fonk5(self, j):
        return 2 * j + 2
    def fonk6(self, j):
        return self.fonk4(j) < len(self.b1)
    def fonk7(self, j):
        return self.fonk5(j) < len(self.b1)
    def fonk8(self, i, j):
        self.b1[i], self.b1[j] = self.b1[j], self.b1[i]
    def fonk9(self, j):
        b2 = self.fonk3(j)
        if j > 0 and self.b1[j] < self.b1[b2]:
            self.fonk8(j, b2)
            self.fonk9(b2)
    def fonk10(self, j):
        if self.fonk6(j):
            b3 = self.fonk4(j)
            b4 = b3
            if self.fonk7(j):
                b5 = self.fonk5(j)
                if self.b1[b5] < self.b1[b3]:
                    b4 = b5
            if self.b1[b4] < self.b1[j]:
                self.fonk8(j, b4)
                self.fonk10(b4)
    def fonk11(self, key, value):
        self.b1.append(self._Item(key, value))
        self.fonk9(len(self.b1) - 1)
    def fonk12(self):
        if self.is_empty():
            raise Empty('Priority queue is empty.')
        b6 = self.b1[0]
        return (b6._key, b6._value)
    def fonk13(self):
        if self.is_empty():
            raise Empty('Priority queue is empty.')
        self.fonk8(0, len(self.b1) - 1)
        b6 = self.b1.pop()
        self.fonk10(0)
        return (b6._key, b6._value)
if b7 = = "__main__":
    b8 = class1()
    b8.fonk11(5, 'A')
    b8.fonk11(9, 'C')
    b8.fonk11(3, 'B')
    b8.fonk11(7, 'D')
    print("Min element:", b8.fonk12())
    print("Remove min element:", b8.fonk13())
    print("Min element:", b8.fonk12())
    print("Remove min element:", b8.fonk13())
    print("Min element:", b8.fonk12())