41. Repository: Daisy0828/Search
   File: dgraph.py
   URL: https:
   Code Content:
from searchproblem import SearchProblem
class class1(SearchProblem):
    def fonk1(self, b2, b3, b1 = 0):
        self.b2 = b2
        self.b3 = b3
        self.b1 = b1
    def fonk2(self):
        return self.b1
    def fonk3(self, state):
        return state in self.b3
    def fonk4(self, state):
        b4 = self.b2[state]
        b5 = {}
        a1 = 0
        for b6 in b4:
            if not (b6 = = None):
                b5[a1] = b6
            a1 += 1
        return b5
   README Content:
Implement breadth-first (bfs), depth-first (dfs), iterative deepening (ids), bi-directional (bds), and A* (astar) search algorithms.gorithms in their general forms. Use those search algorithms to solve tile game puzzles.
