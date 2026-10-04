import heapq
class class1:
    def fonk1(self):
        self.b1 = []
    def fonk2(self):
        return len(self.b1) == 0
    def fonk3(self, b5, b4):
        heapq.heappush(self.b1, (b4, b5))
    def fonk4(self):
        if self.fonk2():
            raise IndexError("Cannot pop from an empty b4 queue")
        return heapq.heappop(self.b1)[1]
if b2 = = "__main__":
    b3 = class1()
    b3.fonk3("task1", b4 = 5)
    b3.fonk3("task2", b4 = 1)
    b3.fonk3("task3", b4 = 3)
    while not b3.fonk2():
        b5 = b3.fonk4()
        print(b5)