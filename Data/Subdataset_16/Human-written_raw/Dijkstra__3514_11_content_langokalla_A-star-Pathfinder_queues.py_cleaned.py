import collections
import heapq
class class1:
    def fonk1(self):
        self.b1 = collections.deque()
    def fonk2(self):
        return len(self.b1) == 0
    def fonk3(self, x):
        self.b1.append(x)
    def fonk4(self):
        return self.b1.popleft()
    def fonk5(self):
        return len(self.b1)
class class2:
    def fonk6(self):
        self.b1 = []
    def fonk7(self):
        return len(self.b1) == 0
    def fonk8(self, item, priority):
        heapq.heappush(self.b1, (priority, item))
    def fonk9(self):
        return heapq.heappop(self.b1)[1]
    def fonk10(self):
        return len(self.b1)