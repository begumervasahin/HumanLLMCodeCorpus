23. Repository: binaya07/8-puzzle
   File: stack.py
   URL: https:
   Code Content:
class class1:
    def fonk1(self):
        self.b1 = []
        self.b2 = set()
    def fonk2(self,item):
        self.b1.append(item)
        self.b2.add((tuple(item.b1)))
    def fonk3(self):
        if not self.fonk4():
            b3 = self.b1[-1]
            del self.b1[-1]
            self.b2.remove(tuple(b3.b1))
            return b3
        else:
            return 0
    def fonk4(self):
        if len(self.b1) == 0:
            return 1
        else:
            return 0
    def fonk5(self):
        self.b1.clear()
        self.b2.clear()
   README Content:
Solving 8 puzzle game by using different search techniques ( uninformed: BFS, DFS, DLS  ; informed: A* ) and compare their performances.
