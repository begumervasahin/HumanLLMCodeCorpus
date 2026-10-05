1. Repository: speix/8-puzzle-solver
   File: state.py
   URL: https:
   Code Content:
class State:
    def __init__(self, state, parent, move, depth, cost, key):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth
        self.cost = cost
        self.key = key
        if self.state:
            self.map = ''.join(str(e) for e in self.state)
    def __eq__(self, other):
        return self.map == other.map
    def __lt__(self, other):
        return self.map < other.map
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
