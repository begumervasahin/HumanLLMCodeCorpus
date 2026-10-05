8. Repository: abpaudel/8-puzzle
   File: iddfs.py
   URL: https:
   Code Content:
import itertools
from solver import Solver
class IDDFS(Solver):
    def __init__(self, initial_state):
        super(IDDFS, self).__init__(initial_state)
        self.frontier = []
    def dls(self, limit):
        self.frontier.append(self.initial_state)
        while self.frontier:
            board = self.frontier.pop()
            self.explored_nodes.add(tuple(board.state))
            if board.goal_test():
                self.set_solution(board)
                return self.solution
            if board.depth < limit:
                for neighbor in board.neighbors()[::-1]:
                    if tuple(neighbor.state) not in self.explored_nodes:
                        self.frontier.append(neighbor)
                        self.explored_nodes.add(tuple(neighbor.state))
                        self.max_depth = max(self.max_depth, neighbor.depth)
        return None
    def solve(self):
        for i in itertools.count():
            self.frontier = []
            self.explored_nodes = set()
            self.max_depth = 0
            self.frontier.append(self.initial_state)
            sol = self.dls(i)
            if sol is not None:
                break
        return
   README Content:
8 puzzle solver using BFS, DFS, IDDFS and A-star algorithm
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
