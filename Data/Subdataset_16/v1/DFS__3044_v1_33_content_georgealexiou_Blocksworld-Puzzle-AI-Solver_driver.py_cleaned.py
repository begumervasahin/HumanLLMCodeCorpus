from foundation import Node, State, Block
from searchMethods import SearchMethods
def fonk1():
    b1 = [
        Block('A', 0, 0),
        Block('B', 1, 0),
        Block('C', 2, 0)
    ]
    b2 = Block('P', 3, 0)
    b3 = State(b1, b2, None)
    b4 = Node(b3, None, None)
    b5 = [
        Block('A', 1, 2),
        Block('B', 1, 1),
        Block('C', 1, 0)
    ]
    b6 = Block('P', 3, 0)
    b7 = State(b5, b6, None)
    b8 = SearchMethods(b4, b7)
    print('Select Search Method:\n1. DFS\n2. BFS\n3. Iterative Deepening\n4. A*')
    b9 = int(input().strip())
    if b9 = = 1:
        print('DEPTH FIRST SEARCH')
        b8.DFS()
    elif b9 = = 2:
        print('BREADTH FIRST SEARCH')
        b8.BFS()
    elif b9 = = 3:
        print('ITERATIVE DEEPENING SEARCH')
        b8.iterativeDeepening()
    elif b9 = = 4:
        print('A* SEARCH')
        b8.aStar()
    else:
        print('Invalid selection. Please choose a number between 1 and 4.')
if b10 = = "__main__":
    fonk1()