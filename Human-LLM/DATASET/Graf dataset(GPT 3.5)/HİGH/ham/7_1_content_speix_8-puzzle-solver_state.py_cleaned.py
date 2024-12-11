1. Repository: speix/8-puzzle-solver
   File: b1.py
   URL: https:
   Code Content:
class class1:
    def fonk1(self, b1, b2, b3, b4, b5, b6):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
        self.b6 = b6
        if self.b1:
            self.b7 = ''.join(str(e) for e in self.b1)
    def fonk2(self, other):
        return self.b7 = = other.b7
    def fonk3(self, other):
        return self.b7 < other.b7
   README Content:
A.I - Implemented BFS, DFS, A* and IDA* to solve the n-puzzle problem. The script prints the results to output.txt
```
bfs (Breadth-First Search)
dfs (Depth-First Search)
ast (A-Star Search)
ida (Iterative-Deepening-ÎStar Search)
```
```
python driver.py ast 0,8,7,6,5,4,3,2,1
```
```
path_to_goal: ['Right', 'Down', 'Down', 'Right', 'Up', 'Up', 'Left', 'Down', 'Down', 'Left', 'Up', 'Right', 'Down', 'Right', 'Up', 'Up', 'Left', 'Left', 'Down', 'Right', 'Up', 'Right', 'Down', 'Left', 'Down', 'Right', 'Up', 'Up', 'Left', 'Left']
cost_of_path: 30
nodes_expanded: 12893
fringe_size: 6327
max_fringe_size: 6328
search_depth: 30
max_search_depth: 30
running_time: 1.80822521
max_ram_usage: 7.44400000
```
