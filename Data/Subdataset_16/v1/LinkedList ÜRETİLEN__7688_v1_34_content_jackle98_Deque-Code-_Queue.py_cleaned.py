
from collections import deque
def fonk1(size):
    return deque(b1 = size)
class class1:
    def fonk2(self):
        self.b2 = fonk1(1)
    def fonk3(self):
        return str(self.b2)
    def fonk4(self):
        return len(self.b2)
    def fonk5(self, val):
        self.b2.append(val)
    def fonk6(self):
        if len(self.b2) == 0:
            return None
        return self.b2.popleft()
if b3 = = "__main__":
    b4 = class1()
    b4.fonk5(10)
    b4.fonk5(20)
    b4.fonk5(30)
    print("class1 after enqueuing 10, 20, 30:")
    print(b4)
    print("Dequeue element:", b4.fonk6())
    print("class1 after dequeue:")
    print(b4)
    print("Dequeue element:", b4.fonk6())
    print("class1 after dequeue:")
    print(b4)
    print("Dequeue element:", b4.fonk6())
    print("class1 after dequeue:")
    print(b4)
    print("Dequeue element (should return None):", b4.fonk6())