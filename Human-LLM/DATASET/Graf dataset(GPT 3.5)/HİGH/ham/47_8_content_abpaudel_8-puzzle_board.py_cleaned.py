8. Repository: abpaudel/8-puzzle
   File: board.py
   URL: https:
   Code Content:
import numpy as np
class class1:
    b1 = None
    b2 = None
    b3 = None
    a1 = 0
    b4 = None
    a2 = 0
    def fonk1(self, b2, b1 = None, b3=None, a1=0):
        self.b1 = b1
        self.b2 = np.array(b2)
        self.b3 = b3
        self.a1 = a1
        self.b4 = self.fonk5()
        self.a2 = self.a1 + self.fonk6()
    def fonk2(self, other):
        if self.a2 != other.a2:
            return self.a2 < other.a2
        else:
            b5 = {'Up': 0, 'Down': 1, 'Left': 2, 'Right': 3}
            return b5[self.b3] < b5[other.b3]
    def fonk3(self):
        return str(self.b2[:3]) + '\n' \
               + str(self.b2[3:6]) + '\n' \
               + str(self.b2[6:]) + ' ' + str(self.a1) + str(self.b3) + '\n'
    def fonk4(self):
        if np.array_equal(self.b2, np.arange(9)):
            return True
        else:
            return False
    def fonk5(self):
        for i in range(9):
            if self.b2[i] == 0:
                return i
    def fonk6(self):
        b2 = self.fonk7(self.b2)
        b6 = self.fonk7(np.arange(9))
        return sum((abs(b2
    @staticmethod
    def fonk7(b2):
        b7 = np.array(range(9))
        for x, y in enumerate(b2):
            b7[y] = x
        return b7
    def fonk8(self, i, j):
        b8 = np.array(self.b2)
        b8[i], b8[j] = b8[j], b8[i]
        return b8
    def fonk9(self):
        if self.b4 > 2:
            return class1(self.fonk8(self.b4, self.b4 - 3), self, 'Up', self.a1 + 1)
        else:
            return None
    def fonk10(self):
        if self.b4 < 6:
            return class1(self.fonk8(self.b4, self.b4 + 3), self, 'Down', self.a1 + 1)
        else:
            return None
    def fonk11(self):
        if self.b4 % 3 != 0:
            return class1(self.fonk8(self.b4, self.b4 - 1), self, 'Left', self.a1 + 1)
        else:
            return None
    def fonk12(self):
        if (self.b4 + 1) % 3 != 0:
            return class1(self.fonk8(self.b4, self.b4 + 1), self, 'Right', self.a1 + 1)
        else:
            return None
    def fonk13(self):
        b9 = [self.fonk9(), self.fonk10(), self.fonk11(), self.fonk12()]
        return list(filter(None, b9))
    b10 = __str__
   README Content:
8 puzzle solver using BFS, DFS, IDDFS and A-star algorithm
*It is assumed that b6 b2 is:*
     0 1 2
     3 4 5
     6 7 8
You can run `main.py` with the name of algorithm - which is `ast` for A*, `bfs`, or `dfs`, or `ids` for iterative deepening dfs - as the first argument and initial b2 as the second one:
```
$ python main.py bfs 1,2,5,3,4,0,6,7,8
$ python main.py dfs 1,2,5,3,4,0,6,7,8
$ python main.py ids 1,2,5,3,4,0,6,7,8
$ python main.py ast 1,2,5,3,4,0,6,7,8
```
Solution and details will be saved to ```{alg-name}_output.txt```.
