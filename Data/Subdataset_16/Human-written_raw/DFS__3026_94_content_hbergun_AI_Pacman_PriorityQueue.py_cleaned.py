import heapq
class class1:
    def fonk1(self):
        self.b1 = []
    def fonk2(self):
        return len(self.b1) == 0
    def fonk3(self, item, priority):
        heapq.heappush(self.b1, (priority, item))
    def fonk4(self):
        return heapq.heappop(self.b1)[1]