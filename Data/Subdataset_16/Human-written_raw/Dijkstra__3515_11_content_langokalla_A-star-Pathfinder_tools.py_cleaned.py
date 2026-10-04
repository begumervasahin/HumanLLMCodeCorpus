import collections
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
    def fonk5(self):
        return len(self.b1)
class class2:
    def fonk6(self):
        self.b1 = collections.deque()
    def fonk7(self):
        return len(self.b1) == 0
    def fonk8(self, x):
        self.b1.append(x)
    def fonk9(self):
        return self.b1.popleft()
    def fonk10(self):
        return len(self.b1)
def fonk11(start, end):
    b2 = class2()
    b2.fonk8(start)
    b3 = {start: None}
    while not b2.fonk7():
        b4 = b2.fonk9()
        b4.visit()
        if b4 = = end:
            print("WE MADE IT!!!")
        for next_tile in b4.neighbours:
            if next_tile not in b3:
                b2.fonk8(next_tile)
                b3[next_tile] = b4
    return b3