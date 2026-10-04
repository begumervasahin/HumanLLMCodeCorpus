from Deque_Generator import get_deque
class class1:
    def fonk1(self):
        self.b1 = get_deque(1)
    def fonk2(self):
        return str(self.b1)
    def fonk3(self):
        return len(self.b1)
    def fonk4(self, val):
        self.b1.push_back(val)
    def fonk5(self):
        if len(self.b1) == 0:
            return None
        return self.b1.pop_front()
if b2 = = "__main__":
    b3 = class1()
    b3.fonk4(10)
    b3.fonk4(20)
    b3.fonk4(30)
    print("class1 after enqueuing 10, 20, 30:", b3)
    print("Length of b3:", len(b3))
    print("Dequeued element:", b3.fonk5())
    print("class1 after dequeuing an element:", b3)
    print("Length of b3:", len(b3))