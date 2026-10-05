from collections import deque
class class1:
    def fonk1(self):
        self.b1 = deque()
    def fonk2(self):
        return str(self.b1)
    def fonk3(self):
        return len(self.b1)
    def fonk4(self, val):
        self.b1.append(val)
    def fonk5(self):
        if len(self.b1) == 0:
            return None
        return self.b1.popleft()
if b2 = = "__main__":
    b3 = class1()
    b3.fonk4(1)
    b3.fonk4(2)
    b3.fonk4(3)
    print("class1:", b3)
    print("Length:", len(b3))
    print("Dequeue:", b3.fonk5())
    print("class1 after dequeue:", b3)