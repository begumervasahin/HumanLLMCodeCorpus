8. Repository: abpaudel/8-puzzle
   File: iddfs.py
   URL: https:
   Code Content:
import itertools
from solver import Solver
class class1(Solver):
    def fonk1(self, initial_state):
        super(class1, self).fonk1(initial_state)
        self.b1 = []
    def fonk2(self, limit):
        self.b1.append(self.initial_state)
        while self.b1:
            b2 = self.b1.pop()
            self.b4.add(tuple(b2.state))
            if b2.goal_test():
                self.set_solution(b2)
                return self.solution
            if b2.depth < limit:
                for neighbor in b2.neighbors()[::-1]:
                    if tuple(neighbor.state) not in self.b4:
                        self.b1.append(neighbor)
                        self.b4.add(tuple(neighbor.state))
                        self.b3 = max(self.b3, neighbor.depth)
        return None
    def fonk3(self):
        for i in itertools.count():
            self.b1 = []
            self.b4 = set()
            self.b3 = 0
            self.b1.append(self.initial_state)
            b5 = self.fonk2(i)
            if b5 is not None:
                break
        return
   README Content:
8 puzzle solver using BFS, DFS, class1 and A-star algorithm
*It is assumed that goal state is:*
     0 1 2
     3 4 5
     6 7 8
You can run `main.py` with the name of algorithm - which is `ast` for A*, `bfs`, or `dfs`, or `ids` for iterative deepening dfs - as the first argument and initial state as the second one:
```
$ python main.py bfs 1,2,5,3,4,0,6,7,8
$ python main.py dfs 1,2,5,3,4,0,6,7,8
$ python main.py ids 1,2,5,3,4,0,6,7,8
$ python main.py ast 1,2,5,3,4,0,6,7,8
```
Solution and details will be saved to ```{alg-name}_output.txt```.
