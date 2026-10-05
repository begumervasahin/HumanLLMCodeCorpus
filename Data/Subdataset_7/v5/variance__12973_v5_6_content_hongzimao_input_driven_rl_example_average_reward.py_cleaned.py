from collections import deque
class class1:
    def fonk1(self, size):
        self.b1 = deque(maxlen=size)
        self.b2 = deque(maxlen=size)
        self.a1 = 0
        self.a2 = 0
    def fonk2(self, b5, time):
        if len(self.b1) >= self.b1.maxlen:
            b3 = self.b1.popleft()
            b4 = self.b2.popleft()
            self.a1 -= b3
            self.a2 -= b4
        self.b1.append(b5)
        self.b2.append(time)
        self.a1 += b5
        self.a2 += time
    def fonk3(self, list_reward, list_time):
        assert len(list_reward) == len(list_time)
        for b5, time in zip(list_reward, list_time):
            self.fonk2(b5, time)
    def fonk4(self, list_reward, list_time):
        assert len(list_reward) == len(list_time)
        for b5, time in zip(list_reward, list_time):
            if time != 0:
                self.fonk2(b5, time)
            else:
                assert b5 = = 0
    def fonk5(self):
        return float(self.a1) / float(self.a2)