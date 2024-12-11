from priority_queue_base import PriorityQueueBase
from Empty import Empty
class class1(PriorityQueueBase):
    def fonk1(self):
        self.b1 = []
    def fonk2(self):
        return len(self.b1)
    def fonk3(self, b3):
        return (b3 - 1)
    def fonk4(self, b3):
        return 2 * b3 + 1
    def fonk5(self, b3):
        return 2 * b3 + 2
    def fonk6(self, b3):
        return self.fonk4(b3) < len(self.b1)
    def fonk7(self, b3):
        return self.fonk5(b3) < len(self.b1)
    def fonk8(self, i, b3):
        self.b1[i], self.b1[b3] = self.b1[b3], self.b1[i]
    def fonk9(self, b3):
        b2 = self.fonk3(b3)
        while b3 > 0 and self.b1[b3] < self.b1[b2]:
            self.fonk8(b3, b2)
            b3 = b2
            b2 = self.fonk3(b3)
    def fonk10(self, b3):
        while self.fonk6(b3):
            b4 = self.fonk4(b3)
            b5 = b4
            if self.fonk7(b3):
                b6 = self.fonk5(b3)
                if self.b1[b6] < self.b1[b4]:
                    b5 = b6
            if self.b1[b5] < self.b1[b3]:
                self.fonk8(b3, b5)
                b3 = b5
            else:
                break
    def fonk11(self, key, value):
        self.b1.append(self._Item(key, value))
        self.fonk9(len(self.b1) - 1)
    def fonk12(self):
        if self.is_empty():
            raise Empty('Priority queue is empty.')
        b7 = self.b1[0]
        return (b7._key, b7._value)
    def fonk13(self):
        if self.is_empty():
            raise Empty('Priority queue is empty.')
        self.fonk8(0, len(self.b1) - 1)
        b7 = self.b1.pop()
        if len(self.b1) > 0:
            self.fonk10(0)
        return (b7._key, b7._value)