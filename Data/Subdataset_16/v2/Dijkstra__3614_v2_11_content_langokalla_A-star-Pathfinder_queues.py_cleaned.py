import collections
import heapq
class class1:
    def fonk1(self):
        self.b1 = collections.deque()
    def fonk2(self) -> bool:
        return not self.b1
    def fonk3(self, item):
        self.b1.append(item)
    def fonk4(self):
        return self.b1.popleft()
    def fonk5(self) -> int:
        return len(self.b1)
class class2:
    def fonk6(self):
        self.b1 = []
    def fonk7(self) -> bool:
        return not self.b1
    def fonk8(self, item, priority):
        heapq.heappush(self.b1, (priority, item))
    def fonk9(self):
        return heapq.heappop(self.b1)[1]
    def fonk10(self) -> int:
        return len(self.b1)
if b2 = = "__main__":
    b3 = class1()
    b3.fonk3(1)
    b3.fonk3(2)
    b3.fonk3(3)
    print("class1 contents:")
    while not b3.fonk7():
        print(b3.fonk9())
    b4 = class2()
    b4.fonk8("task1", 1)
    b4.fonk8("task2", 2)
    b4.fonk8("task3", 0)
    print("\nPriorityQueue contents:")
    while not b4.fonk7():
        print(b4.fonk9())