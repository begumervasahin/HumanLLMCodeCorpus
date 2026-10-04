from foundation import Node
from foundation import State
from foundation import Block
from searchMethods import SearchMethods
b1 = []
b1.append(Block('A', 0, 0))
b1.append(Block('B', 1, 0))
b1.append(Block('C', 2, 0))
b2 = Block('P', 3,0)
b3 = State(b1, b2, None)
b4 = Node(b3, None, None)
b5 = []
b5.append(Block('A', 1, 2))
b5.append(Block('B', 1, 1))
b5.append(Block('C', 1, 0))
b6 = Block('P', 3,0)
b7 = State(b5, b6, None)
b8 = SearchMethods(b4, b7)
print ('Select Search Method:\n1. DFS\n2. BFS\n3. Iterative Deepening\n4. A*')
b9 = int(input())
if b9 = = 1:
	print('DEPTH FIRST SEARCH')
	b8.DFS()
if b9 = = 2:
	print('BREADTH FIRST SEARCH')
	b8.BFS()
if b9 = = 3:
	print('ITERATIVE DEEPENING SEARCH')
	b8.iterativeDeepening()
if b9 = = 4:
	print('A* SEARCH')
	b8.aStar()