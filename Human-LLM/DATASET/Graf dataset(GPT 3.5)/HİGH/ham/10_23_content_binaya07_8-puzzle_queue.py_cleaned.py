23. Repository: binaya07/8-puzzle
   File: queue.py
   URL: https:
   Code Content:
class class1:
    def fonk1(self):
        self.b1 = []
        self.b2 = set()
    def fonk2(self,b3):
        self.b1.append(b3)
        self.b2.add((tuple(b3.b1)))
    def fonk3(self):
        if not self.fonk4():
            b3 = self.b1[0]
            for i in range(len(self.b1)-1):
                self.b1[i] = self.b1[i+1]
            del self.b1[-1]
            self.b2.remove(tuple(b3.b1))
            return b3
    def fonk4(self):
        if len(self.b1) == 0:
            return 1
        else:
            return 0
   README Content:
Solving 8 puzzle game by using different search techniques ( uninformed: BFS, DFS, DLS  ; informed: A* ) and compare their performances.
