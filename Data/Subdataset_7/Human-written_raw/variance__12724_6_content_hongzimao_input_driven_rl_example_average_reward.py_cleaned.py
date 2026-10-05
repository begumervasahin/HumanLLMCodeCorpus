from collections import deque
class class1(object):
    def fonk1(self, size):
        self.b1 = deque(maxlen=size)
        self.b2 = deque(maxlen=size)
        self.a1 = 0
        self.a2 = 0
    def fonk2(self, reward, time):
        if len(self.b1) >= self.b1.maxlen:
            b3 = self.b1.popleft()
            b4 = self.b2.popleft()
            self.a1 -= b3
            self.a2 -= b4
        self.b1.append(reward)
        self.b2.append(time)
        self.a1 += reward
        self.a2 += time
    def fonk3(self, list_reward, list_time):
        assert len(list_reward) == len(list_time)
        for i in range(len(list_reward)):
            self.fonk2(list_reward[i], list_time[i])
    def fonk4(self, list_reward, list_time):
        assert len(list_reward) == len(list_time)
        for i in range(len(list_reward)):
            if list_time[i] != 0:
                self.fonk2(list_reward[i], list_time[i])
            else:
                assert list_reward[i] == 0
    def fonk5(self):
        return float(self.a1) / float(self.a2)