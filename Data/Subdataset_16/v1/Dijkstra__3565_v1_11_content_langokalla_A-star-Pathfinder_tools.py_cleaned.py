import collections
import heapq
class class1:
    def fonk1(self):
        self.b1 = []
    def fonk2(self) -> bool:
        return len(self.b1) == 0
    def fonk3(self, item, priority):
        heapq.heappush(self.b1, (priority, item))
    def fonk4(self):
        return heapq.heappop(self.b1)[1]
    def fonk5(self) -> int:
        return len(self.b1)
class class2:
    def fonk6(self):
        self.b1 = collections.deque()
    def fonk7(self) -> bool:
        return len(self.b1) == 0
    def fonk8(self, item):
        self.b1.append(item)
    def fonk9(self):
        return self.b1.popleft()
    def fonk10(self) -> int:
        return len(self.b1)
def fonk11(start, end):
    b2 = class2()
    b2.fonk8(start)
    b3 = {start: None}
    while not b2.fonk7():
        b4 = b2.fonk9()
        b4.fonk14()
        if b4 = = end:
            print("WE MADE IT!!!")
            break
        for next_tile in b4.b6:
            if next_tile not in b3:
                b2.fonk8(next_tile)
                b3[next_tile] = b4
    return b3
class class3:
    def fonk12(self, b5):
        self.b5 = b5
        self.b6 = []
    def fonk13(self, neighbor):
        self.b6.append(neighbor)
    def fonk14(self):
        print(f"Visiting {self.b5}")
b7 = class3('A')
b8 = class3('B')
b9 = class3('C')
b10 = class3('D')
b7.fonk13(b8)
b8.fonk13(b9)
b9.fonk13(b10)
b3 = fonk11(b7, b10)
print("\nPath taken:")
b4 = b10
while b4 is not None:
    print(b4.b5)
    b4 = b3[b4]