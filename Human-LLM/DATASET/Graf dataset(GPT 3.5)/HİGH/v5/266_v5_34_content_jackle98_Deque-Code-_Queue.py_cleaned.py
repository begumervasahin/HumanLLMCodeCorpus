from Deque_Generator import get_deque
class class1:
    def fonk1(self):
        self.b1 = get_deque(1)
    def fonk2(self):
        return str(self.b1)
    def fonk3(self):
        return len(self.b1)
    def fonk4(self, value):
        self.b1.push_back(value)
    def fonk5(self):
        if not self.b1:
            return None
        return self.b1.pop_front()